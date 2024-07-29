

for botellas in range(99, 0, -1):
    if botellas == 1:
        print(f"{botellas} botella de cerveza en la pared, {botellas} botella de cerveza")
        print("Toma una, pásala, no quedan más botellas de cerveza en la pared")
    else:
        print(f"{botellas} botellas de cerveza en la pared, {botellas} botellas de cerveza")
        print(f"Toma una, pásala, {botellas-1} botellas de cerveza en la pared")
