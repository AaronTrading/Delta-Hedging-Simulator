import numpy as np
from black_scholes import black_scholes_call, calculate_delta

class DeltaHedgingSimulator:
    def __init__(self, S0, K, T, r, sigma, n_steps, n_options):
        """
        Initialise le simulateur de Delta Hedging
        
        Args:
            S0 (float): Prix initial du sous-jacent
            K (float): Prix d'exercice (strike)
            T (float): Maturité en années
            r (float): Taux d'intérêt sans risque
            sigma (float): Volatilité du sous-jacent
            n_steps (int): Nombre de pas de temps pour la simulation
            n_options (int): Nombre d'options dans le portefeuille
        """
        self.S0 = S0
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        self.n_steps = n_steps
        self.n_options = n_options
        self.dt = T / n_steps
        
        # Initialisation des tableaux pour stocker les résultats
        self.stock_prices = np.zeros(n_steps + 1)
        self.option_prices = np.zeros(n_steps + 1)
        self.deltas = np.zeros(n_steps + 1)
        self.portfolio_values = np.zeros(n_steps + 1)
        self.cash_positions = np.zeros(n_steps + 1)
        self.hedge_errors = np.zeros(n_steps + 1)
        
    def generate_stock_path(self):
        """Génère un chemin de prix pour le sous-jacent via un GBM"""
        self.stock_prices[0] = self.S0
        for i in range(1, self.n_steps + 1):
            z = np.random.normal(0, 1)
            self.stock_prices[i] = self.stock_prices[i-1] * np.exp(
                (self.r - 0.5 * self.sigma**2) * self.dt + 
                self.sigma * np.sqrt(self.dt) * z
            )
    
    def run_simulation(self):
        """Exécute la simulation complète du Delta Hedging"""
        # Génération du chemin de prix
        self.generate_stock_path()
        
        # Calcul des prix initiaux
        self.option_prices[0] = black_scholes_call(
            self.S0, self.K, self.T, self.r, self.sigma
        ) * self.n_options
        
        self.deltas[0] = calculate_delta(
            self.S0, self.K, self.T, self.r, self.sigma
        ) * self.n_options
        
        # Position initiale en cash
        self.cash_positions[0] = self.option_prices[0] - self.deltas[0] * self.S0
        self.portfolio_values[0] = self.option_prices[0]
        
        # Simulation des rebalancements
        for i in range(1, self.n_steps + 1):
            # Calcul du temps restant
            time_to_maturity = self.T - i * self.dt
            
            # Calcul du nouveau prix de l'option et du delta
            self.option_prices[i] = black_scholes_call(
                self.stock_prices[i], self.K, time_to_maturity, self.r, self.sigma
            ) * self.n_options
            
            self.deltas[i] = calculate_delta(
                self.stock_prices[i], self.K, time_to_maturity, self.r, self.sigma
            ) * self.n_options
            
            # Calcul du PnL du portefeuille
            stock_pnl = (self.deltas[i-1] * (self.stock_prices[i] - self.stock_prices[i-1]))
            cash_pnl = self.cash_positions[i-1] * (np.exp(self.r * self.dt) - 1)
            
            # Mise à jour des positions
            self.cash_positions[i] = self.cash_positions[i-1] * np.exp(self.r * self.dt) - \
                                   (self.deltas[i] - self.deltas[i-1]) * self.stock_prices[i]
            
            self.portfolio_values[i] = self.deltas[i] * self.stock_prices[i] + self.cash_positions[i]
            
            # Calcul de l'erreur de couverture
            self.hedge_errors[i] = self.portfolio_values[i] - self.option_prices[i]
    
    def get_results(self):
        """Retourne les résultats de la simulation"""
        return {
            'stock_prices': self.stock_prices,
            'option_prices': self.option_prices,
            'deltas': self.deltas,
            'portfolio_values': self.portfolio_values,
            'cash_positions': self.cash_positions,
            'hedge_errors': self.hedge_errors
        } 