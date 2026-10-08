import random
import time
import sys
import winsound  # Added sound framework

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)
    print()

def run_game():
    speed = 0
    fuel = 100
    car_health = 100
    distance_covered = 0
    target_distance = 120  
    rival_distance = 0     

    print_slow("==========================================")
    print_slow("    HIGH-SPEED STREET RACING SIMULATOR    ")
    print_slow("==========================================")
    print_slow("Objective: Reach 120 miles before the rival without destroying your car.\n")

    while distance_covered < target_distance:
        if fuel <= 0:
            print_slow("\n[💥 GAME OVER] Out of fuel!")
            return
        if car_health <= 0:
            print_slow("\n[💥 GAME OVER] Engine totaled!")
            return

        print(f"\n📍 Distance: {distance_covered}/{target_distance} miles")
        print(f"🏁 Rival    : {rival_distance}/{target_distance} miles")
        print(f"⚡ Speed    : {speed} MPH | ⛽ Fuel: {fuel}% | 🔧 Health: {car_health}%")
        print("------------------------")
        print("1. Accelerate  2. Coast  3. Brake  4. Pit Stop")
        choice = input("Choice (1-4): ").strip()

        if choice == "1":
            speed += random.randint(15, 30)
            winsound.Beep(600, 200)  # Acceleration tone
            fuel -= random.randint(8, 15)
            distance_covered += int(speed / 4)
        elif choice == "2":
            speed = max(0, speed - 10)
            fuel -= 3
            distance_covered += int(speed / 4)
        elif choice == "3":
            speed = max(0, speed - 30)
            winsound.Beep(250, 400)  # Braking tone
            distance_covered += int(speed / 4)
        elif choice == "4":
            speed = 0
            fuel = 100
            car_health = min(100, car_health + 25)
            print_slow("🔧 Pit stop complete! Refueled and repaired.")
            winsound.Beep(440, 150)  # Pit stop chimes
            winsound.Beep(880, 150)

        # Move Rival
        rival_distance += random.randint(6, 9)
        if rival_distance >= target_distance and rival_distance > distance_covered:
            print_slow("\n[💥 GAME OVER] The rival crossed the finish line first!")
            return

        time.sleep(0.3)

    print_slow("\n🏁 VICTORY! You won the race!")

if __name__ == "__main__":
    run_game()
