# 4) Descubra a lógica e complete o próximo elemento:
# a) 1, 3, 5, 7, ___
# b) 2, 4, 8, 16, 32, 64, ____
# c) 0, 1, 4, 9, 16, 25, 36, ____
# d) 4, 16, 36, 64, ____
# e) 1, 1, 2, 3, 5, 8, ____
# f) 2,10, 12, 16, 17, 18, 19, ____


seq_a = [1, 3, 5, 7]
seq_a.append(seq_a[-1] + 2)

seq_b = [2, 4, 8, 16, 32, 64]
seq_b.append(seq_b[-1] * 2)

seq_c = [0, 1, 4, 9, 16, 25, 36]
seq_c.append((len(seq_c)) ** 2)

seq_d = [4, 16, 36, 64]
seq_d.append((len(seq_d) * 2) ** 2)

seq_e = [1, 1, 2, 3, 5, 8]
seq_e.append(seq_e[-1] + seq_e[-2])

seq_f = [2, 10, 12, 16, 17, 18, 19]
seq_f.append(seq_f[-1] + 1)

print(seq_a, seq_b, seq_c, seq_d, seq_e, seq_f)

