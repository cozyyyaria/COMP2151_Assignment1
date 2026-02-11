"""
Author: Ariana Cruz
Assignment: #1
"""
# string
gym_member = "Ariana Cruz"

# float
preferred_weight_kg = 20.5

# integer
highest_reps = 25

# boolean
membership_active = True

# Dictionary: key = friend name, value = tuple of workout minutes
workout_stats = {
    "Ariana": (30, 45, 20),
    "Jamie": (40, 30, 35),
    "Taylor": (50, 20, 25)
}

print("Dictionary created!")

for friend, minutes in list(workout_stats.items()):
    if isinstance(minutes, tuple):
        total = sum(minutes)
        workout_stats[friend + "_Total"] = total

print(workout_stats)

# 2D (nested) list: each row is a friend's workout minutes for 3 activities
workout_list = []

for friend, minutes in workout_stats.items():
    if isinstance(minutes, tuple):
        workout_list.append(list(minutes))

print(workout_list)

print("Yoga and Running (all friends):")
for row in workout_list:
    print(row[0:2])

print("Weightlifting (last two friends):")
for row in workout_list[-2:]:
    print(row[2])

for key, value in workout_stats.items():
    if "Total" in key and value >= 120:
        name = key.replace("_Total", "")
        print(f"Great job staying active, {name}!")

name = input("Enter a friend's name: ").strip()

if name in workout_stats:
    minutes = workout_stats[name]
    total = workout_stats[name + "_Total"]
    print(f"{name}'s workout minutes (yoga, running, weightlifting): {minutes}")
    print(f"{name}'s total workout minutes: {total}")
else:
    print(f"Friend {name} not found in the records.")    

# Build a totals-only dictionary
totals = {}
for key, value in workout_stats.items():
    if "Total" in key:
        friend_name = key.replace("_Total", "")
        totals[friend_name] = value

highest_friend = max(totals, key=totals.get)
lowest_friend = min(totals, key=totals.get)

print("Friend with the highest total workout minutes:", highest_friend, "-", totals[highest_friend])
print("Friend with the lowest total workout minutes:", lowest_friend, "-", totals[lowest_friend])