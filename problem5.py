def esperanza_matematica_total(n, m, adv):
    esperanza_mat = 0
    for a in range(1, m + 1):
        if adv:
            probabilidad = ((a / m) ** n - ((a - 1) / m) ** n)
        else:
            probabilidad = ((m + 1 - a) / m) ** n - ((m - a) / m) ** n

        esperanza_mat += a * probabilidad

    return esperanza_mat

n, m, adv = eval(input())
print(esperanza_matematica_total(n, m, adv))