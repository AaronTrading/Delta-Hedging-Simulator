import numpy as np
from scipy.stats import norm

def black_scholes_call(S, K, T, r, sigma):
    """
    Calcule le prix d'une option call européenne selon le modèle Black-Scholes
    
    Args:
        S (float): Prix actuel du sous-jacent
        K (float): Prix d'exercice (strike)
        T (float): Temps jusqu'à la maturité (en années)
        r (float): Taux d'intérêt sans risque
        sigma (float): Volatilité du sous-jacent
    
    Returns:
        float: Prix de l'option call
    """
    d1 = (np.log(S/K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    return call_price

def calculate_delta(S, K, T, r, sigma):
    """
    Calcule le delta d'une option call européenne
    
    Args:
        S (float): Prix actuel du sous-jacent
        K (float): Prix d'exercice (strike)
        T (float): Temps jusqu'à la maturité (en années)
        r (float): Taux d'intérêt sans risque
        sigma (float): Volatilité du sous-jacent
    
    Returns:
        float: Delta de l'option call
    """
    d1 = (np.log(S/K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    delta = norm.cdf(d1)
    return delta

def calculate_gamma(S, K, T, r, sigma):
    """
    Calcule le gamma d'une option call européenne
    
    Args:
        S (float): Prix actuel du sous-jacent
        K (float): Prix d'exercice (strike)
        T (float): Temps jusqu'à la maturité (en années)
        r (float): Taux d'intérêt sans risque
        sigma (float): Volatilité du sous-jacent
    
    Returns:
        float: Gamma de l'option call
    """
    d1 = (np.log(S/K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
    return gamma 