# Simulateur de Delta Hedging

Ce projet simule une stratégie de Delta Hedging dynamique pour une option européenne de type "call". Il permet de visualiser l'efficacité de la couverture delta en comparant la valeur théorique de l'option avec la valeur du portefeuille de couverture.

## Fonctionnalités

- Simulation d'un mouvement brownien géométrique pour le prix du sous-jacent
- Calcul dynamique du delta de l'option via le modèle Black-Scholes
- Rebalancement automatique du portefeuille selon le delta
- Calcul des PnL et des erreurs de couverture
- Visualisations multiples :
  - Évolution du prix du sous-jacent
  - Valeur du portefeuille vs Prix de l'option
  - Évolution du delta
  - Erreur de couverture
  - Distribution des erreurs de couverture

## Screens

Rentrez les valeurs dans la fenêtre dédiée:

![Screen1](https://media.discordapp.net/attachments/1280431720679870475/1377964010984701984/Screenshot_1.png?ex=683ae07d&is=68398efd&hm=58af165f30df2c9660922322f3c8a3e27d363e4c37f75d9df541b704a9ad028e&=&format=webp&quality=lossless&width=499&height=661)

![Graphique1](https://media.discordapp.net/attachments/1280431720679870475/1377964011240427540/Screenshot_2.png?ex=683ae07d&is=68398efd&hm=91008ca83c205c203e2cd962f30f6aac9e634a79f4de1e20de509085e428c7de&=&format=webp&quality=lossless&width=1760&height=1218)

![Graphique2](https://media.discordapp.net/attachments/1280431720679870475/1377964010649161819/Screenshot_3.png?ex=683ae07d&is=68398efd&hm=22cb8f642d941f79231e95df6c67a0cb31c1b49f4663761a5598651895026477&=&format=webp&quality=lossless&width=1249&height=781)

## Installation

1. Clonez le repository
2. Installez les dépendances :

```bash
pip install -r requirements.txt
```

## Utilisation

Exécutez le script principal :

```bash
python app.py
```

## Paramètres modifiables

Les paramètres de la simulation peuvent être ajustés dans le fichier `app.py` :

- Prix initial du sous-jacent (S0)
- Prix d'exercice (K)
- Maturité (T)
- Taux d'intérêt sans risque (r)
- Volatilité (sigma)
- Nombre de pas de temps (n_steps)
- Nombre d'options (n_options)

## Structure du projet

- `app.py` : Point d'entrée de l'application
- `black_scholes.py` : Implémentation du modèle Black-Scholes et calcul des Greeks
- `delta_hedging.py` : Logique de simulation du Delta Hedging
- `plots.py` : Fonctions de visualisation
- `requirements.txt` : Dépendances du projet

## Dependencies

- numpy
- pandas
- matplotlib
- scipy
- tk

## Auteur

Aaron Z.

## Licence

MIT
