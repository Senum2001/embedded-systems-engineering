# File: main.py - Main entry point
from acquisition_manager import AcquisitionManager
from buffer_manager import BufferManager
from upload_manager import UploadManager
import time
import threading

class EcoWattScaffold:
    def __init__(self):
        print("EcoWatt Started")
        self.acquisition = AcquisitionManager()
        self.buffer = BufferManager()
        self.uploader = UploadManager()
        self.running = True
        
    def start(self):
        # acquisition thread
        acquisition_thread = threading.Thread(target=self.acquisition_loop)
        acquisition_thread.daemon = True
        acquisition_thread.start()
        
        # upload thread  
        upload_thread = threading.Thread(target=self.upload_loop)
        upload_thread.daemon = True
        upload_thread.start()
               
        # Keep main thread alive
        try:
            while self.running:
                time.sleep(1)
        except KeyboardInterrupt:
            self.running = False
            
    def acquisition_loop(self):
        """Continuously poll inverter and buffer data"""
        while self.running:
            try:
                # Poll inverter 
                data = self.acquisition.poll_inverter() 
                
                # Buffer the data 
                self.buffer.add_data(data)
                
                # Sleep until next poll
                time.sleep(self.acquisition.poll_interval)
            except Exception as e:
                print(f"[ERROR] Acquisition failed: {e}")
                time.sleep(1)
            
    def upload_loop(self):
        """Upload buffered data every 15 seconds"""
        while self.running:
            try:
                # Wait for upload interval 
                time.sleep(15) # 15s
                
                # Get buffered data
                buffered_data = self.buffer.get_all_data()
                
                if buffered_data:
                    # Upload to cloud 
                    success = self.uploader.upload_data(buffered_data)
                    
                    if success:
                        # Clear buffer
                        self.buffer.clear()
                else:
                    print("No data to upload")
                    
            except Exception as e:
                print(f"Upload failed: {e}")

if __name__ == "__main__":
    device = EcoWattScaffold()
    device.start()
