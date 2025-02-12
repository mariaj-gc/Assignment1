def calc_esperanzamat_v():
    esperanza_mat = 0
    for n in range(1, 101):
        probabilidad = ((n / 100) ** 4 - ((n - 1) / 100) ** 4)
        esperanza_mat += n * probabilidad
    return esperanza_mat

print(calc_esperanzamat_v())