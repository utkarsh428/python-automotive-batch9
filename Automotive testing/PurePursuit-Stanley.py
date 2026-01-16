import math

#Pure Pursuit
def pure_pursuit(vehicle_x, vehicle_y, target_x, target_y):
    dx = target_x - vehicle_x
    dy = target_y - vehicle_y
    # Simple angle to target
    steering_angle = math.atan2(dy, dx)
    return steering_angle

#Stanley
def stanley(vehicle_x, vehicle_y, vehicle_yaw, target_x, target_y, k=0.1):
    dx = target_x - vehicle_x
    dy = target_y - vehicle_y
    heading_to_target = math.atan2(dy, dx)

# Adding little cross-track correction
    cross_track = math.hypot(dx, dy) * k
    steering_angle = heading_to_target + cross_track
    return steering_angle

#taking example
vehicle_x, vehicle_y, vehicle_yaw = 0, 0, 0
target_x, target_y = 10, 5

pp_angle = pure_pursuit(vehicle_x, vehicle_y, target_x, target_y)
st_angle = stanley(vehicle_x, vehicle_y, vehicle_yaw, target_x, target_y)

print("Pure Pursuit Steering Angle:", pp_angle)
print("Stanley Steering Angle:", st_angle)