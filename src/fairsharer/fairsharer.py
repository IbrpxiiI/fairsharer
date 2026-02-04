def fair_sharer(values, num_iterations, share=0.1):
    """
    Führt Umverteilungsalgorithmus aus.

    In jeder Iteration gibt der größte Wert einen Anteil -share-
    an seinen linken & rechten Nachbarn ab. Das erste & letzte
    Element gelten ebenfalls als Nachbarn.

    Beispiele:
    fair_sharer([0, 1000, 800, 0], 1) --> [100, 800, 900, 0]
    fair_sharer([0, 1000, 800, 0], 2) --> [100, 890, 720, 90]

    Parameter:
        values (list): Liste numerischer Werte
        num_iterations (int): Anzahl der Iterationen
        share (float): Anteil pro Nachbar
    """
    values = list(values)

    for _ in range(num_iterations):
        max_index = values.index(max(values))
        amount = values[max_index] * share

        left = (max_index - 1) % len(values)
        right = (max_index + 1) % len(values)

        new_values = values.copy()
        new_values[max_index] -= 2 * amount
        new_values[left] += amount
        new_values[right] += amount

        values = new_values

    return values
