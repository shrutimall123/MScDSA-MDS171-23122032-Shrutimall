import random
import csv
from datetime import datetime

def generate_traffic_data():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    speed = random.randint(0, 60)  
    vehicles = random.randint(0, 50)  
    return [timestamp, speed, vehicles]

def write_data_to_csv(data, file_name):
    with open(file_name, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data)

def calculate_average(data):
    total_speed = sum(float(row[1]) for row in data)
    total_vehicles = sum(float(row[2]) for row in data)
    average_speed = total_speed / len(data)
    average_vehicles = total_vehicles / len(data)
    return average_speed, average_vehicles

def analyze_traffic_data(data):
    average_speed, average_vehicles = calculate_average(data)
    print("Average Speed:", average_speed, "mph")
    print("Average Number of Vehicles:", average_vehicles)

def main():
    file_name = "traffic_data.csv"
    while True:
        choice = input("Press '1' to generate traffic data, '2' to analyze data, or 'q' to quit: ")
        if choice == '1':
            traffic_data = generate_traffic_data()
            write_data_to_csv(traffic_data, file_name)
            print("Data captured:", traffic_data)
        elif choice == '2':
            try:
                with open(file_name, mode="r") as file:
                    data = list(csv.reader(file))
                    analyze_traffic_data(data[1:])  
            except FileNotFoundError:
                print("No data available.")
        elif choice.lower() == 'q':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
