def insertion_sort(arquivo):
    try:
        with open(arquivo, 'r') as file:
            numeros = [int(linha.strip()) for linha in file if linha.strip().isdigit()]

        for i in range(1, len(numeros)):
            chave = numeros[i]
            j = i - 1
            while j >= 0 and numeros[j] > chave:
                numeros[j + 1] = numeros[j]
                j -= 1
            numeros[j + 1] = chave
        
        print("Numeros ordenados:", numeros)
    
    except FileNotFoundError:
        print("Arquivo nao encontrado.")
    except ValueError:
        print("O arquivo contem valores nao numericos.")

arquivo = 'extra.txt'
insertion_sort(arquivo)
