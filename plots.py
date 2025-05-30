import matplotlib.pyplot as plt
import numpy as np

def plot_simulation_results(results, dt):
    """
    Crée les graphiques de la simulation
    
    Args:
        results (dict): Dictionnaire contenant les résultats de la simulation
        dt (float): Pas de temps
    """
    time_points = np.arange(len(results['stock_prices'])) * dt
    
    # Création de la figure avec 4 sous-graphiques
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
    
    # Graphique 1: Prix du sous-jacent
    ax1.plot(time_points, results['stock_prices'], 'b-', label='Prix du sous-jacent')
    ax1.set_title('Évolution du prix du sous-jacent')
    ax1.set_xlabel('Temps (années)')
    ax1.set_ylabel('Prix')
    ax1.grid(True)
    ax1.legend()
    
    # Graphique 2: Valeur du portefeuille vs Prix de l'option
    ax2.plot(time_points, results['portfolio_values'], 'g-', label='Valeur du portefeuille')
    ax2.plot(time_points, results['option_prices'], 'r--', label='Prix de l\'option')
    ax2.set_title('Valeur du portefeuille vs Prix de l\'option')
    ax2.set_xlabel('Temps (années)')
    ax2.set_ylabel('Valeur')
    ax2.grid(True)
    ax2.legend()
    
    # Graphique 3: Delta
    ax3.plot(time_points, results['deltas'], 'b-', label='Delta')
    ax3.set_title('Évolution du Delta')
    ax3.set_xlabel('Temps (années)')
    ax3.set_ylabel('Delta')
    ax3.grid(True)
    ax3.legend()
    
    # Graphique 4: Erreur de couverture
    ax4.plot(time_points, results['hedge_errors'], 'r-', label='Erreur de couverture')
    ax4.set_title('Erreur de couverture')
    ax4.set_xlabel('Temps (années)')
    ax4.set_ylabel('Erreur')
    ax4.grid(True)
    ax4.legend()
    
    plt.tight_layout()
    plt.show()

def plot_hedging_error_distribution(results):
    """
    Crée un histogramme de la distribution des erreurs de couverture
    
    Args:
        results (dict): Dictionnaire contenant les résultats de la simulation
    """
    plt.figure(figsize=(10, 6))
    plt.hist(results['hedge_errors'], bins=50, density=True, alpha=0.7)
    plt.title('Distribution des erreurs de couverture')
    plt.xlabel('Erreur de couverture')
    plt.ylabel('Fréquence')
    plt.grid(True)
    plt.show() 