import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def ForwardKinematics(theta0, theta1, theta2, theta3):
    p2 = np.array([
        A1 * np.cos(theta1) * np.cos(theta0),
        A1 * np.cos(theta1) * np.sin(theta0),
        A1 * np.sin(theta1)
    ])
    p3 = p2 + np.array([
        A2 * np.cos(theta1 + theta2) * np.cos(theta0),
        A2 * np.cos(theta1 + theta2) * np.sin(theta0),
        A2 * np.sin(theta1 + theta2)
    ])
    p4 = p3 + np.array([
        A3 * np.cos(theta1 + theta2 + theta3) * np.cos(theta0),
        A3 * np.cos(theta1 + theta2 + theta3) * np.sin(theta0),
        A3 * np.sin(theta1 + theta2 + theta3)
    ])
    return np.array([p2, p3, p4])

def InverseKinematics(x, y, z, gripper_angle):
    gripper_angle = np.radians(gripper_angle)

    # Base rotation
    theta0 = np.atan(z / x)
    xa = x / np.cos(theta0)

    # Wrist position
    x3 = xa - A3 * np.cos(gripper_angle)
    y3 = y - A3 * np.sin(gripper_angle)
    d = np.sqrt(x3 ** 2 + y3 ** 2)

    # Elbow pitch
    alpha = np.acos((A1 ** 2 + A2 ** 2 - d ** 2) / (2 * A1 * A2))
    theta2 = np.pi - alpha #180 - alpha

    # Shoulder pitch
    lambda1 = np.atan((A2 * np.sin(theta2)) / (A1 + A2 * np.cos(theta2)))
    beta1 = np.atan(y3 / x3)
    theta1 = lambda1 + beta1

    # Wrist pitch
    theta3 = - theta1 - theta2 + gripper_angle

    return np.array([theta0, theta1, theta2, theta3])

# arm section lengths [mm]
# A0 = 0 // first section is the base and only rotates, hence no length
A1 = 200 # shoulder
A2 = 180 # elbow
A3 = 50 # gripper

# 3d plot animation
angle_range = 90
angle_step = 2
angles = list(range(-angle_range, angle_range + 1, angle_step)) + list(range(angle_range-1, -angle_range - 1, -angle_step))
for i in range(5):
    angle = angles + angles
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for gripper_angle in angles:
    #----InverseKinematics----
    #coordinates
    x = 100
    y = 100
    z = 50
    #gripper_angle = -30 # gripper angle changes
    joint_angles = InverseKinematics(x, y, z, gripper_angle)
    print(np.degrees(joint_angles))

    #----ForwardKinematics----
    positions = ForwardKinematics(*joint_angles)

    points = np.array([
        [0, 0, 0], #base
        positions[0], #Joint 2
        positions[1], #Joint 3
        positions[2] #gripper
    ])

    # Line plotting
    ax.cla()
    ax.scatter(points[0,0], points[0,1], points[0,2], color='red', label='Base')
    ax.plot(points[:,0], points[:,1], points[:,2], marker='o', linestyle='-')
    plt.gca().set_aspect('equal')

    # Graph labels
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    plt.pause(0.05)

plt.show()
