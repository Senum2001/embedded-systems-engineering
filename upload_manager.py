from datetime import datetime

class UploadManager:
    def __init__(self):
        self.upload_count = 0
        
    def upload_data(self, data):
        """Simulates uploading data to EcoWatt Cloud"""
        self.upload_count += 1
        
        # Prepare payload
        payload = {
            'device_id': 'ecowatt_001',
            'upload_timestamp': datetime.now().isoformat(),
            'data_points': data,
            'count': len(data)
        }
        
        # Simulate cloud upload
        print(f"\n[UPLOAD #{self.upload_count}] Sending {len(data)} data points to cloud:")
        print(f"  Time Range: {data[0]['timestamp']} to {data[-1]['timestamp']}")
        print(f"  Avg Voltage: {sum(d['voltage'] for d in data) / len(data):.2f}V")
        print(f"  Avg Current: {sum(d['current'] for d in data) / len(data):.2f}A")
        print(f"  Total Power: {sum(d['power'] for d in data):.2f}W")
        print("  Upload Status: SUCCESS\n")
        
        return True
