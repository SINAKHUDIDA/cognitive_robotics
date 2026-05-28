import csv
import matplotlib.pyplot as plt

time = []
comp_x = []
comp_y = []

with open('data/compass_data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        time.append(float(row[0])) # Zeit
        comp_x.append(float(row[1])) # X-Wert
        comp_y.append(float(row[2])) # Y-Wert

plt.figure(figsize=(10, 5))
plt.plot(time, comp_x, color='blue', linewidth=1.5, label='Kompass X-Achse')
plt.plot(time, comp_y, color='red', linewidth=1.5, linestyle='--', label='Kompass Y-Achse')

plt.title('Compass Sensor - Rotation auf der Stelle')
plt.xlabel('Zeit (ms)')
plt.ylabel('Magnetische Ausrichtung (Sensoreinheit)')
plt.grid(True)
plt.legend() # Legende anzeigen
plt.tight_layout()
plt.savefig('compass_plot.png')
plt.show()