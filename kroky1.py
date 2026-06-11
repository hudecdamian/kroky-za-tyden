celkem_kroku = 0

for den in range(1, 8):
    kroky_den = int(input(f"Kolik kroků jsi ušel {den}. den? "))
    celkem_kroku += kroky_den

print("---")
print(f"Celkový počet kroků za celý týden: {celkem_kroku}")

if celkem_kroku < 50000:
    print("„Máš málo pohybu“")
elif 50000 <= celkem_kroku <= 80000:
    print("„Tvoje aktivita je dobrá“")
else:
    print("„Skvělá práce!“")
