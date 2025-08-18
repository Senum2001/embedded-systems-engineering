import random
import time
from datetime import datetime

class AcquisitionManager:
    def __init__(self):
        self.poll_interval = 2  
        
    def poll_inverter(self):
        """Simulates polling the inverter SIM for voltage/current data"""  
        voltage = round(220 + random.uniform(-10, 10), 2)  # 220V ± 10V
        current = round(5 + random.uniform(-1, 1), 2)      # 5A ± 1A
        
        data = {
            'timestamp': datetime.now().isoformat(),
            'voltage': voltage,
            'current': current,
            'power': round(voltage * current, 2)
        }
        
        print(f"[POLL] {data['timestamp']}: V={data['voltage']}V, I={data['current']}A, P={data['power']}W")
        return data
