total = float(input("Cuanto fue el total de la cuenta?   "))

propina_15 = total * 0.15
propina_18 = total * 0.18
propina_20 = total * 0.20

print(f"Si quieres dejar una propina del 15% deberias dejar ${propina_15:.2f}")
print(f"Si quieres dejar una propina del 18% deberias dejar ${propina_18:.2f}")
print(f"Si quieres dejar una propina del 20% deberias dejar ${propina_20:.2f}")
