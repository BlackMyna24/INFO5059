# Exercice 3 : 
""" Vous travaillez avec une entreprise d’emballage qui doit optimiser la manière dont les produits sont emballés dans des conteneurs.
L’objectif est de maximiser la valeur totale des produits emballés tout en respectant une limite de poids"""

# 1. Représentons les articles sous forme d'une liste de tuples
liste = [('pain', 50), ('cahier', 180), ('riz', 25000), ('portable', 300)] # avec le poids en grammes.

# 2. Implémentons l'algorithme du sac à dos 0/1 avec programmation dynamique
"""i sera le nbre d'articles considérés, c la capacité actuelle du sac, tab[i][w] stocke la valeur maximale atteignable avec les i premiers articles et une capacité max de c."""

def sac_à_dos(i, c):
    n = len(i)
    dp = [[0] * (c + 1) for _ in range(n + 1)]

    # Remplissage de la table DP
    for i in range(1, n + 1):
        value, weight = i[i - 1]
        for w in range(c + 1):
            if weight > w:
                dp[i][w] = dp[i - 1][w]  # On ne prend pas l'objet
            else:
                dp[i][w] = max(dp[i - 1][w], value + dp[i - 1][w - weight])  # On choisit la meilleure option

    # Trouver les objets sélectionnés
    w = c
    selected_i = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:  # Si la valeur change, l'objet a été pris
            selected_i.append(i[i - 1])
            w -= i[i - 1][1]  # Réduire la capacité restante

    selected_i.reverse()  # Pour garder l'ordre initial
    return dp[n][c], selected_i

def main():
    # Définition des articles (valeur, poids)
    i = [(60, 10), (100, 20), (120, 30)]
    c = 50  # Capacité maximale du sac à dos

    # Résolution du problème
    max_value, selected_i = sac_à_dos(i, c)

    # Affichage des résultats
    print("Valeur maximale obtenue :", max_value)
    print("Articles sélectionnés :")
    for value, weight in selected_i:
        print(f"- Valeur : {value}, Poids : {weight}")

if __name__ == "__main__":
    main()
