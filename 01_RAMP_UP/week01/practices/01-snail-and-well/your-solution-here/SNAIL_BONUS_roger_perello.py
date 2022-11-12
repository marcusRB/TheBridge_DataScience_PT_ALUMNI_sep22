well_lenght = 125
total_distance = 0
days = 0
advances = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]
advances_mean = round(sum(advances) / len(advances), 2)
temporary_list = []


for advance in advances:
    if total_distance < well_lenght:
        total_distance = total_distance + advance
        days += 1
    temporary_list.append((advance - advances_mean) ** 2)


standard_deviation = round((sum(temporary_list) // len(advances)) ** 0.5, 2)


print(f"""El caracol tarda {days} días en subir el pozo.
En un día, avanza un máximo de {max(advances)} cm y un mínimo de {min(advances)} cm.
Su media de velocidad es de {advances_mean} cm diarios.
Su desviación típica es de {standard_deviation} cm.
""")
