def calc_esperanzamat():
    esperanza_mat = 0
    for n in range(1, 21):
        probabilidad = ((21 - n) / 20) ** 2 - ((20 - n) / 20) ** 2
        esperanza_mat += n * probabilidad
    return esperanza_mat

print(calc_esperanzamat())