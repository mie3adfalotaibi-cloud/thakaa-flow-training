def step(altitude, velocity, fuel, thrust):
    velocity = velocity + 1.62 - thrust * 0.5
    altitude = altitude - velocity
    fuel = fuel - thrust
    return altitude, velocity, fuel


def autopilot(altitude, velocity, fuel):
    # safe speed gets smaller as we get closer to the ground
    target = max(2, (2 * altitude) ** 0.5)
    thrust = round((velocity + 1.62 - target) / 0.5)
    if thrust < 0:
        thrust = 0
    if thrust > 10:
        thrust = 10
    if thrust > fuel:
        thrust = fuel
    return thrust


def play(auto=False):
    altitude = 1000
    velocity = 0
    fuel = 200
    t = 0
    while altitude > 0:
        print(f"t={t}s | altitude: {altitude:.1f} m | speed: {velocity:.1f} m/s | fuel: {fuel}")
        if auto:
            thrust = autopilot(altitude, velocity, fuel)
            print("Autopilot thrust:", thrust)
        else:
            text = input("Thrust (0-10): ")
            if not text.isdigit():
                print("Please enter a number")
                continue
            thrust = int(text)
            if thrust > 10:
                print("Thrust must be from 0 to 10")
                continue
            if thrust > fuel:
                print("Not enough fuel, you have", fuel)
                continue
        altitude, velocity, fuel = step(altitude, velocity, fuel, thrust)
        t = t + 1

    if velocity <= 3:
        print(f"Safe landing at {velocity:.1f} m/s | fuel left: {fuel} | flight time: {t} s")
    else:
        print(f"Crashed at {velocity:.1f} m/s | fuel left: {fuel} | flight time: {t} s")


mode = input("Play yourself (1) or autopilot (2)? ")
if mode == "2":
    play(auto=True)
else:
    play()

# Autopilot idea: the safe speed depends on the height: target = square root of (2 x altitude),
# and never less than 2 m/s. Far from the ground we can fall fast, near the ground we must be slow.
# Each second it calculates the thrust that brings the speed to the target (from 0 to 10). 