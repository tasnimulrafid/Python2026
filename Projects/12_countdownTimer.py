import time

print("----- Digital CountDown Timer -----")
total_seconds = int(input("enter countdown time in seconds: "))

print("\nTimer Starts!")
print("="*10)

for x in range(total_seconds, -1, -1):
    hrs = x // 3600
    mins = (x // 60) % 60
    secs = x % 60

    print(f"{hrs:02}:{mins:02}:{secs:02}")
    time.sleep(1)
print("\nTime's Up!")