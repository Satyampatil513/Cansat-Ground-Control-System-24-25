import time
import random
from multiprocessing import Queue

class DummySerialPort:
    def __init__(self, port, baudrate, interval=1):
        self.port = port
        self.baudrate = baudrate
        self.interval = interval
        self.buffer = Queue()
        self.start_time = time.time()
        self.packet_count = 0

    def open(self):
        print(f"Opening dummy serial port {self.port} with baudrate {self.baudrate}")

    def close(self):
        print(f"Closing dummy serial port {self.port}")

    def generate_data(self):
        self.packet_count += 1
        timestamp = time.time()
        data = {
            "Team ID": "2024ASI-CANSAT-XXX",
            "Timestamp": timestamp,
            "Packet Count": self.packet_count,
            "Altitude": round(random.uniform(0, 1000), 1),
            "Pressure": random.randint(90000, 110000),
            "Temperature": round(random.uniform(-20, 40), 1),
            "Voltage": round(random.uniform(3.0, 4.2), 2),
            "GNSS Time": timestamp,
            "GNSS Latitude": round(random.uniform(-90.0, 90.0), 4),
            "GNSS Longitude": round(random.uniform(-180.0, 180.0), 4),
            "GNSS Altitude": round(random.uniform(0, 10000), 1),
            "GNSS Satellites": random.randint(0, 12),
            "Accelerometer Data": round(random.uniform(-10, 10), 2),
            "Gyro Spin Rate": round(random.uniform(-500, 500), 2),
            "Flight Software State": random.choice(["BOOT", "TEST_MODE", "LAUNCH_PAD", "ASCENT", "ROCKET_DEPLOY", "DESCENT", "AEROBREAK_RELEASE", "IMPACT"])
        }
        self.buffer.put(data)

    def read(self):
        if not self.buffer.empty():
            return self.buffer.get()
        else:
            return None

def data_generation_process(queue, interval):
    port = DummySerialPort(port="COM1", baudrate=9600, interval=interval)
    port.open()
    try:
        while True:
            port.generate_data()
            queue.put(port.read())
            time.sleep(port.interval)
    except KeyboardInterrupt:
        port.close()
        print("Data generation process terminated")
