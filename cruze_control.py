# Cruise Control Speed Alert System
SPEED_LIMIT = 70

def check_speed(speed):

  print(f"Current Speed: {speed} kmph")
  if speed > SPEED_LIMIT:
   print("ALERT! Speed exceeded 70 kmph")
  else:
   print("Speed is within safe limit")
if __name__ == "__main__":

  speed = int(input("Enter current vehicle speed (kmph): "))
  check_speed(speed)