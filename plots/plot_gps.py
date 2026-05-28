import csv
import matplotlib.pyplot as plt

gps_x = []
gps_y = []

with open('data/gps_data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Kopfzeile überspringen
    for row in reader:
        # Index 1 ist X, Index 2 ist Y (Index 0 wäre die Zeit)
        gps_x.append(float(row[1]))
        gps_y.append(float(row[2]))

plt.figure(figsize=(8, 8))
plt.plot(gps_x, gps_y, color='green', linewidth=2)
plt.title('GPS Sensor - Gefahrene Trajektorie (Kreisbahn)')
plt.xlabel('Globale X-Koordinate (m)')
plt.ylabel('Globale Y-Koordinate (m)')
plt.grid(True)
plt.tight_layout()
plt.savefig('gps_plot.png')
plt.show()