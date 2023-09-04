def calculate_fitness(wi, fin, fout):
    if fin == 0 and fout == 0:
        return 0.0  
    return wi * fin / (fin + fout) ** 2
