import csv
from datetime import datetime

dtc_list = []

#data collection layer
def sensor_report(code, description):
    dtc_list.append({
        "code": code,
        "description": description,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    print(code, "added")

#data processing layer
def show_dtcs():
    if not dtc_list:
        print("No DTCs")
        return
    for dtc in dtc_list:
        print(dtc["code"], "-", dtc["description"], "(", dtc["time"], ")")
def clear_dtcs():
            dtc_list.clear()
            print("ALL DTCs CLEARED")

#predictive layer
def export_csv(filename = "dtc_report.csv"):
    if not dtc_list:
        print("No DTCs to export")
        return
    with open(filename, "w", newline="") as f:
     writer = csv.DictWriter(f, fieldnames=["code","description","time"])
     writer.writeheader()
     writer.writerows(dtc_list)
    print("saved as", filename)

sensor_report("PO123", "Throttle Sensor")
sensor_report("PO456", "Evap System")
show_dtcs()
export_csv()
clear_dtcs()
show_dtcs()