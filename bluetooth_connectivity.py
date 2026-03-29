import random
from datetime import datetime

pairing_logs = []

# Data Collection Layer
def bluetooth_pairing_attempt():
    result = random.choice(["Success", "Failure"])
    pairing_logs.append({
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "result": result
    })
    print("Pairing Attempt:", result)

# Data Processing Layer
def calculate_success_failure():
    success = sum(1 for log in pairing_logs if log["result"] == "Success")
    failure = len(pairing_logs) - success
    return success, failure

# Predictive / Evaluation Layer
def connectivity_quality_score():
    success, failure = calculate_success_failure()
    if len(pairing_logs) == 0:
        return 0
    score = (success / len(pairing_logs)) * 100
    return round(score, 2)

# Display Results
def show_results():
    success, failure = calculate_success_failure()
    score = connectivity_quality_score()

    print("\nBluetooth Test Summary")
    print("Total Attempts:", len(pairing_logs))
    print("Successful Pairings:", success)
    print("Failed Pairings:", failure)
    print("Connectivity Quality Score:", score, "%")

# Simulation
for _ in range(6):
    bluetooth_pairing_attempt()

show_results()