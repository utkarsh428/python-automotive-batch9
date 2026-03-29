import csv
from datetime import datetime

# Sensor limits based on AUTOSAR ECU specifications
SENSOR_LIMITS = {
    "speed": (0, 200),
    "temperature": (-40, 150),
    "pressure": (0, 300)
}

def validate_sensor(sensor, value):
    min_val, max_val = SENSOR_LIMITS[sensor]

    if min_val <= value <= max_val:
        status = "PASS"
        ecu_reaction = "ECU operates normally"
        reason = "Sensor value is within the valid AUTOSAR range"
    else:
        status = "FAIL"
        ecu_reaction = "ECU enters safe mode / fault state"
        reason = "Sensor value is outside the valid AUTOSAR range"

    return status, ecu_reaction, reason

def log_result(sensor, value, status, ecu_reaction):
    with open("sensor_test_log.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.now(),
            sensor,
            value,
            status,
            ecu_reaction
        ])

def run_test():
    print("\n=== AUTOSAR SENSOR VALIDATION TEST ===")
    print("Available sensors: speed, temperature, pressure")

    sensor = input("Enter sensor name: ").lower()

    if sensor not in SENSOR_LIMITS:
        print("Invalid sensor name!")
        return

    try:
        value = float(input("Enter sensor value: "))
    except ValueError:
        print("Invalid value entered!")
        return

    status, ecu_reaction, reason = validate_sensor(sensor, value)
    log_result(sensor, value, status, ecu_reaction)

    print("\n--- TEST RESULT ---")
    print(f"Sensor Name      : {sensor.upper()}")
    print(f"Sensor Value     : {value}")
    print(f"Test Status      : {status}")
    print(f"Reason           : {reason}")
    print(f"Expected ECU Act : {ecu_reaction}")
    print("-------------------\n")

# Create CSV header once
with open("sensor_test_log.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Timestamp",
        "Sensor",
        "Value",
        "Result",
        "ECU Reaction"
    ])

while True:
    run_test()
    choice = input("Do you want to test another sensor? (yes/no): ").lower()
    if choice != "yes":
        print("\nRegression testing completed. Exiting...")
        break