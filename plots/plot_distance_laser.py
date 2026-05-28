import csv
import matplotlib.pyplot as plt

time = []
distance = []

with open('../data/distance_laser.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Kopfzeile überspringen
    for row in reader:
        time.append(int(row[0]))
        distance.append(float(row[1]))

plt.figure(figsize=(10, 5))
plt.plot(time, distance, color='blue', linewidth=1)
plt.title('DistanceSensor Laser - Annäherung an Wand')
plt.xlabel('Zeit (ms)')
plt.ylabel('Distanz (Sensoreinheit)')
plt.grid(True)
plt.axvline(x=4512, color='red', linestyle='--', label='Annäherung beginnt')
plt.legend()
plt.tight_layout()
plt.savefig('distance_laser_plot.png')
plt.show()