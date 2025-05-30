import tkinter as tk
from tkinter import ttk
from delta_hedging import DeltaHedgingSimulator
from plots import plot_simulation_results, plot_hedging_error_distribution

class DeltaHedgingGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Simulateur de Delta Hedging")
        self.root.geometry("400x500")
        
        # Variables pour stocker les valeurs
        self.S0 = tk.DoubleVar(value=100.0)
        self.K = tk.DoubleVar(value=100.0)
        self.T = tk.DoubleVar(value=1.0)
        self.r = tk.DoubleVar(value=0.05)
        self.sigma = tk.DoubleVar(value=0.2)
        self.n_steps = tk.IntVar(value=252)
        self.n_options = tk.IntVar(value=100)
        
        self.create_widgets()
        
    def create_widgets(self):
        # Style
        style = ttk.Style()
        style.configure("TLabel", padding=5)
        style.configure("TEntry", padding=5)
        
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Titre
        title_label = ttk.Label(main_frame, text="Paramètres de la simulation", font=('Helvetica', 14, 'bold'))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Champs de saisie
        self.create_input_field(main_frame, "Prix initial (S0):", self.S0, 1)
        self.create_input_field(main_frame, "Prix d'exercice (K):", self.K, 2)
        self.create_input_field(main_frame, "Maturité (T) en années:", self.T, 3)
        self.create_input_field(main_frame, "Taux sans risque (r):", self.r, 4)
        self.create_input_field(main_frame, "Volatilité (σ):", self.sigma, 5)
        self.create_input_field(main_frame, "Nombre de pas de temps:", self.n_steps, 6)
        self.create_input_field(main_frame, "Nombre d'options:", self.n_options, 7)
        
        # Bouton de lancement
        launch_button = ttk.Button(main_frame, text="Lancer la simulation", command=self.run_simulation)
        launch_button.grid(row=8, column=0, columnspan=2, pady=20)
        
    def create_input_field(self, parent, label_text, variable, row):
        label = ttk.Label(parent, text=label_text)
        label.grid(row=row, column=0, sticky=tk.W, pady=2)
        
        entry = ttk.Entry(parent, textvariable=variable)
        entry.grid(row=row, column=1, sticky=(tk.W, tk.E), pady=2)
        
    def run_simulation(self):
        # Récupération des valeurs
        params = {
            'S0': self.S0.get(),
            'K': self.K.get(),
            'T': self.T.get(),
            'r': self.r.get(),
            'sigma': self.sigma.get(),
            'n_steps': self.n_steps.get(),
            'n_options': self.n_options.get()
        }
        
        # Création et exécution de la simulation
        simulator = DeltaHedgingSimulator(**params)
        simulator.run_simulation()
        results = simulator.get_results()
        
        # Affichage des résultats
        print("\nRésultats de la simulation de Delta Hedging:")
        print(f"Prix initial du sous-jacent: {params['S0']:.2f}")
        print(f"Prix d'exercice: {params['K']:.2f}")
        print(f"Maturité: {params['T']:.2f} années")
        print(f"Taux sans risque: {params['r']:.2%}")
        print(f"Volatilité: {params['sigma']:.2%}")
        print(f"Nombre de pas de temps: {params['n_steps']}")
        print(f"Nombre d'options: {params['n_options']}")
        
        print("\nRésultats finaux:")
        print(f"Prix final du sous-jacent: {results['stock_prices'][-1]:.2f}")
        print(f"Valeur finale du portefeuille: {results['portfolio_values'][-1]:.2f}")
        print(f"Prix final de l'option: {results['option_prices'][-1]:.2f}")
        print(f"Erreur de couverture finale: {results['hedge_errors'][-1]:.2f}")
        
        # Affichage des graphiques
        plot_simulation_results(results, params['T']/params['n_steps'])
        plot_hedging_error_distribution(results)
        
        # Fermeture de la fenêtre
        self.root.destroy()

def main():
    app = DeltaHedgingGUI()
    app.root.mainloop()

if __name__ == "__main__":
    main() 