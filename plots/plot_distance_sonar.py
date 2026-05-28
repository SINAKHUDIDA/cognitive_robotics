import csv
import matplotlib.pyplot as plt

time = []
distance = []

with open('../controllers/distance_sonar/distance_sonar.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        time.append(int(row[0]))
        distance.append(float(row[1]))

plt.figure(figsize=(10, 5))
plt.plot(time, distance, color='orange', linewidth=1)
plt.title('DistanceSensor Sonar - Annäherung an Wand')
plt.xlabel('Zeit (ms)')
plt.ylabel('Distanz (Sensoreinheit)')
plt.grid(True)
plt.tight_layout()
plt.savefig('distance_sonar_plot.png')
plt.show()