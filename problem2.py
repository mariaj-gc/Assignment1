def calc_esperanzamat_v():
    esperanza_mat = 0
    for n in range(1, 21):
        probabilidad = ((n / 20) ** 2 - ((n - 1) / 20) ** 2)
        esperanza_mat += n * probabilidad

    return esperanza_mat

print(calc_esperanzamat_v())