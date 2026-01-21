import qrcode

users = []

print("Enter user details\n")

# Step 1: Take user inputs
while True:
    user_id = input("Enter ID: ")
    name = input("Enter Name: ")
    subject = input("Enter Subject: ")

    users.append({
        "id": user_id,
        "name": name,
        "subject": subject
    })

    choice = input("\nDo you want to add more users? (yes/no): ").lower()

    if choice == "no":
        print("\nexit\n")
        break
    elif choice != "yes":
        print("\nInvalid choice. Exiting...\n")
        break

# Step 2: Generate QR codes
print("Generating QR codes...\n")

for user in users:
    qr_data = f"""CERTIFICATE

ID: {user['id']}
Name: {user['name']}
Subject: {user['subject']}
"""

    # Make filename safe (remove extra spaces)
    safe_name = user['name'].strip().replace(" ", "_")
    filename = f"{safe_name}_Certificate.png"

    qr = qrcode.make(qr_data)
    qr.save(filename)

    print(f"QR code generated → {filename}")

print("\nAll certificate QR codes generated successfully!")