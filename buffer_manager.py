import threading

class BufferManager:
    def __init__(self):
        self.data_buffer = []
        self.lock = threading.Lock() 
        
    def add_data(self, data):
        """Add new data point to buffer"""
        with self.lock:
            self.data_buffer.append(data)
            print(f"[BUFFER] Added data. Buffer size: {len(self.data_buffer)}")
            
    def get_all_data(self):
        """Get all buffered data"""
        with self.lock:
            return self.data_buffer.copy()
            
    def clear(self):
        """Clear the buffer after upload"""
        with self.lock:
            count = len(self.data_buffer)
            self.data_buffer.clear()
            print(f"[BUFFER] Cleared {count} data points")
