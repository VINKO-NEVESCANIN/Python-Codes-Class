import math

# Redondeo estándar hacia el entero más cercano
print(round(4.2))   # 4
print(round(4.7))   # 5

# Redondeo con decimales
print(round(3.14159, 2))  # 3.14
print(round(3.14159, 3))  # 3.142

# Redondeo hacia abajo (floor)
print(math.floor(4.9))  # 4
print(math.floor(-4.9)) # -5 (ojo con negativos)

# Redondeo hacia arriba (ceil)
print(math.ceil(4.1))   # 5
print(math.ceil(-4.1))  # -4 (ojo con negativos)

# Truncar (quita decimales, no redondea)
print(math.trunc(4.9))   # 4
print(math.trunc(-4.9))  # -4
