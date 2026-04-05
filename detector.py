from collections import Counter

with open("login_logs.txt", "r") as file:
    logs = file.readlines()

failed_users = []

for line in logs:
    if "FAILED" in line:
        user = line.split()[-1]
        failed_users.append(user)

count = Counter(failed_users)

for user, attempts in count.items():
    if attempts >= 5:
        print("Possible brute force attack on", user)
