import csv
from datetime import datetime

class DTCManager:
    def __init__(self):
        self.dtc_db = {}

    def insert_dtc(self, dtc_code, description, status="ACTIVE"):
        self.dtc_db[dtc_code] = {
            "Description": description,
            "Status": status,
            "Timestamp": datetime.now()
        }
        print(f"DTC {dtc_code} inserted.")

    def read_dtcs(self):
        if not self.dtc_db:
            print("No DTCs stored.")
            return

        for code, details in self.dtc_db.items():
            print(f"DTC: {code}")
            print(f" Description : {details['Description']}")
            print(f" Status      : {details['Status']}")
            print(f" Timestamp   : {details['Timestamp']}")
            print("-----------------------------")

    def clear_dtc(self, dtc_code):
        if dtc_code in self.dtc_db:
            del self.dtc_db[dtc_code]
            print(f"DTC {dtc_code} cleared.")
        else:
            print("DTC not found.")

    def export_dtc_report(self, filename="DTC_Report.csv"):
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["DTC Code", "Description", "Status", "Timestamp"])

            for code, details in self.dtc_db.items():
                writer.writerow([
                    code,
                    details["Description"],
                    details["Status"],
                    details["Timestamp"]
                ])

        print("DTC report exported to CSV.")



if __name__ == "__main__":
    dtc = DTCManager()

    dtc.insert_dtc("P0100", "Mass Air Flow Sensor Fault")
    dtc.insert_dtc("P0200", "Injector Circuit Malfunction")

    print("\n--- READING DTCs ---")
    dtc.read_dtcs()

    print("\n--- CLEARING ONE DTC ---")
    dtc.clear_dtc("P0100")

    print("\n--- EXPORTING REPORT ---")
    dtc.export_dtc_report()