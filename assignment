Lagura_Patients = { 
    "CJ": [80, 90, 85, 120, 40, 68, 70], 
    "Charles": [80, 130, 91, 70, 56, 100, 130], 
    "Clark": [90, 90, 120, 130, 140, 80, 99] 
}

tally = 0
highestreading = 0
all_readings = []  # List to store all readings for the final summary

print("Blood sugar summary -")

for name, readings in Lagura_Patients.items():
    print(f"\nPatient: {name}")
    for item in readings:
        all_readings.append(item)  # Collect metric data
        
        # Track the actual absolute highest reading
        if item > highestreading:
            highestreading = item
            
        # Determine status
        if item >= 120:
            print(f"{item}: High")
            tally += 1
        else:
            print(f"{item}: Normal")

# Overall metrics calculation
min_reading = min(all_readings)
max_reading = max(all_readings)
avg_reading = sum(all_readings) / len(all_readings)
diff_reading = max_reading - min_reading

print("\n" + "="*30)
print(f"Total High Readings: {tally}")
print(f"Highest Individual Reading: {highestreading}")
print("-"*30)
print(f"Minimum Reading: {min_reading}")
print(f"Maximum Reading: {max_reading}")
print(f"Average Reading: {avg_reading:.2f}")
print(f"Difference (Max - Min): {diff_reading}")
print("="*30)
