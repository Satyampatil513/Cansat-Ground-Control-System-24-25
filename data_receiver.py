import csv
import os
from multiprocessing import Queue, Process
from data_generator import data_generation_process

def data_receiver_process(queue, csv_file, tsv_file):
    fieldnames = [
        "Team ID", "Timestamp", "Packet Count", "Altitude", "Pressure", "Temperature", 
        "Voltage", "GNSS Time", "GNSS Latitude", "GNSS Longitude", "GNSS Altitude", 
        "GNSS Satellites", "Accelerometer Data", "Gyro Spin Rate", "Flight Software State"
    ]
    
    try:
        with open(csv_file, mode='w', newline='') as csv_f, open(tsv_file, mode='w', newline='') as tsv_f:
            csv_writer = csv.DictWriter(csv_f, fieldnames=fieldnames)
            tsv_writer = csv.DictWriter(tsv_f, fieldnames=fieldnames, delimiter='\t')

            csv_writer.writeheader()
            tsv_writer.writeheader()

            while True:
                if not queue.empty():
                    data = queue.get()
                    if data:
                        print(f"Received data: {data}")
                        csv_writer.writerow(data)
                        tsv_writer.writerow(data)
    except KeyboardInterrupt:
        print("Data receiver process terminated")

if __name__ == "__main__":
    data_queue = Queue()
    
    csv_file = 'data_output.csv'
    tsv_file = 'data_output.tsv'
    
    data_gen_process = Process(target=data_generation_process, args=(data_queue, 1))
    data_gen_process.start()

    try:
        data_receiver_process(data_queue, csv_file, tsv_file)
    except KeyboardInterrupt:
        data_gen_process.terminate()
        data_gen_process.join()
        print("Main program terminated")
