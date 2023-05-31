import serial
import threading
import json


class SensorDataCollector:

    def __init__(self, ports):
        self.ports = ports
        self.sensors_data = {}
        self._stop_event = threading.Event()

    def start(self):
        self.threads = []
        for i, port in enumerate(self.ports):
            thread = threading.Thread(target=self._collect_data,
                                      args=(f'sensor{i + 1}', port))
            thread.start()
            self.threads.append(thread)

    def stop(self):
        self._stop_event.set()
        for thread in self.threads:
            thread.join()

    def _collect_data(self, sensor_id, port):
        with serial.Serial(port, 9600, timeout=1) as ser:
            while not self._stop_event.is_set():
                line = ser.readline().decode('utf-8').strip()
                if line:
                    temperature, humidity = self._parse_data(line)
                    self.sensors_data[sensor_id] = {
                        'temperature': temperature,
                        'humidity': humidity,
                    }

    @staticmethod
    def _parse_data(line):
        parts = line.split('\t')
        temperature = float(parts[0].split(': ')[1].split(' *C')[0])
        humidity = float(parts[1].split(': ')[1].split(' %')[0])
        return temperature, humidity