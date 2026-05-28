from controller import Robot
import csv

robot = Robot()
timestep = int(robot.getBasicTimeStep())

# GPS aktivieren
gps = robot.getDevice("gps")
gps.enable(timestep)

# Motoren für Thymio II initialisieren
left_motor = robot.getDevice("motor.left")
right_motor = robot.getDevice("motor.right")
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Roboter fährt geradeaus
left_motor.setVelocity(3.0)
right_motor.setVelocity(3.0)

# CSV direkt öffnen und während der Simulation beschreiben
with open('gps_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['time', 'gps_x', 'gps_y'])

    t = 0
    while robot.step(timestep) != -1:
        # GPS Werte auslesen (X und Y Koordinaten)
        position = gps.getValues()
        x = position[0]
        y = position[1] 
        
        # In die Datei schreiben
        writer.writerow([t, x, y])
        
        # Ausgabe in der Konsole
        print(f"Zeit: {t}, X: {x:.4f}, Y: {y:.4f}")
        
        t += timestep