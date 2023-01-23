def calculate_rate(resting_heart_rate, age):
    for intensity in range(55, 100, 5):
        target_heart_rate = (((220 - age) - resting_heart_rate) * (intensity * .01)) + resting_heart_rate
        yield intensity, round(target_heart_rate)


user_resting_heart_rate = int(input("Resting pulse: "))
user_age = int(input("Age: "))
print("Intensity\tRate")
print("*********\t****")
for percentage, bpm in calculate_rate(user_resting_heart_rate, user_age):
    print(f"{percentage}%\t\t\t{bpm} bpm")

