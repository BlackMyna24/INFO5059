def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1  # Si l'élément n'est pas trouvé

def main():
    # Liste triée d'exemple
    sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]

    # Valeurs à rechercher
    targets = [18, 1, 17, 24, 50, 5, 13]  

    # Exécution des recherches et affichage des résultats
    for target in targets:
        result = binary_search(sorted_list, target)
        if result != -1:
            print(f"Valeur {target} trouvée à l'index {result}.")
        else:
            print(f"Valeur {target} non trouvée dans la liste.")

# Exécute le programme
if __name__ == "__main__":
    main()

# La recherche linéaire par contre 
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
