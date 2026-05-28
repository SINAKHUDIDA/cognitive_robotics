from controller import Robot
import csv

robot = Robot()
timestep = int(robot.getBasicTimeStep())

# Kompass aktivieren
compass = robot.getDevice("compass")
compass.enable(timestep)

# Motoren initialisieren
left_motor = robot.getDevice("motor.left")
right_motor = robot.getDevice("motor.right")
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Roboter dreht sich auf der Stelle
left_motor.setVelocity(3.0)
right_motor.setVelocity(-3.0)

# CSV Datei öffnen und beschreiben
with open('compass_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['time', 'compass_x', 'compass_y'])

    while robot.step(timestep) != -1 and robot.getTime() < 10.0:
        current_time = robot.getTime()
        
        # Kompass liefert [X, Y, Z]
        heading = compass.getValues()
        comp_x = heading[0]
        comp_y = heading[1] 
        
        # Daten speichern
        writer.writerow([current_time, comp_x, comp_y])
        
        # Ausgabe in der Konsole
        print(f"Zeit: {current_time:.2f}s, X: {comp_x:.2f}, Y: {comp_y:.2f}")
