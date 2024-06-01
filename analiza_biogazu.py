import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Przykładowe dane dotyczące składu biogazu (w procentach objętościowych)
# Zakresy wartości dla CH4 i CO2
data = {
    'CH4 (%)': np.random.uniform(50, 70, 100),  # Zakres od 50% do 70%
    'CO2 (%)': np.random.uniform(30, 50, 100)   # Zakres od 30% do 50%
}

# Tworzenie DataFrame z danymi
df = pd.DataFrame(data)

# Obliczanie ciepła spalania biogazu (MJ/m3)
# Przykładowe wartości ciepła spalania: CH4 = 35.8 MJ/m3, CO2 = 0 MJ/m3
df['Ciepło spalania (MJ/m3)'] = df['CH4 (%)'] * 35.8 / 100

# Zakładana sprawność silnika
sprawnosc_silnika = 0.35

# Obliczanie wydajności energetycznej silnika (MJ)
df['Wydajność silnika (MJ)'] = df['Ciepło spalania (MJ/m3)'] * sprawnosc_silnika

# Przykładowe obliczenia emisji CO2 (kg/m3)
# Zakładamy, że cała zawartość CO2 w biogazie jest emitowana
df['Emisja CO2 (kg/m3)'] = df['CO2 (%)'] * 1.98 / 100  # 1.98 kg/m3 to waga molowa CO2

# Podsumowanie statystyczne danych
summary_stats = df.describe()

# Wykresy
plt.figure(figsize=(12, 8))

# Histogram ciepła spalania
plt.subplot(2, 2, 1)
plt.hist(df['Ciepło spalania (MJ/m3)'], bins=20, color='blue', edgecolor='black')
plt.title('Rozkład ciepła spalania biogazu')
plt.xlabel('Ciepło spalania (MJ/m3)')
plt.ylabel('Liczba próbek')

# Histogram wydajności silnika
plt.subplot(2, 2, 2)
plt.hist(df['Wydajność silnika (MJ)'], bins=20, color='green', edgecolor='black')
plt.title('Rozkład wydajności energetycznej silnika')
plt.xlabel('Wydajność silnika (MJ)')
plt.ylabel('Liczba próbek')

# Wykres emisji CO2
plt.subplot(2, 2, 3)
plt.scatter(df['CH4 (%)'], df['Emisja CO2 (kg/m3)'], color='red')
plt.title('Emisja CO2 w zależności od zawartości CH4')
plt.xlabel('Zawartość CH4 (%)')
plt.ylabel('Emisja CO2 (kg/m3)')

# Wykres ciepła spalania w zależności od zawartości CH4
plt.subplot(2, 2, 4)
plt.scatter(df['CH4 (%)'], df['Ciepło spalania (MJ/m3)'], color='purple')
plt.title('Ciepło spalania w zależności od zawartości CH4')
plt.xlabel('Zawartość CH4 (%)')
plt.ylabel('Ciepło spalania (MJ/m3)')

plt.tight_layout()
plt.show()

# Wyświetlanie podsumowania statystycznego
print("Podsumowanie statystyczne danych:")
print(summary_stats)
