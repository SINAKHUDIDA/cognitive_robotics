from controller import Robot
import csv

robot = Robot()
timestep = int(robot.getBasicTimeStep())

# Sensor als Laser aktivieren
sensor = robot.getDevice('ps0')
sensor.enable(timestep)

# Motoren
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(2.0)
right_motor.setVelocity(2.0)

with open('..distance_laser.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['time', 'distance'])

    t = 0
    while robot.step(timestep) != -1:
        value = sensor.getValue()
        writer.writerow([t, value])
        print(f"Zeit: {t}, Distanz: {value}")
        t += timestep