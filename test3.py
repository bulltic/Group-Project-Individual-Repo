import serial
import time

ser = serial.Serial('/dev/ttyAMA0', 256000, timeout=1)
print("Listening for radar data (Sleeping 2s between reads)...")

def decode_hlk(byte_data):
    val = byte_data[0] + (byte_data[1] << 8)
    if val == 0:
        return 0
    if val & 0x8000:
        return val & 0x7FFF
    else:
        return -val

try:
    while True:
        # 1. Pause the script completely for 2 seconds
        time.sleep(2)
        
        # 2. Dump all old radar frames that piled up during the 2-second sleep
        ser.reset_input_buffer()
        
        # 3. Grab the very next fresh frame that comes in
        while True:
            if ser.read(1) == b'\xaa':
                if ser.read(1) == b'\xff' and ser.read(1) == b'\x03' and ser.read(1) == b'\x00':
                    payload = ser.read(26)
                    if len(payload) == 26:
                        t1_x_ft = decode_hlk(payload[0:2]) / 304.8
                        t1_y_ft = decode_hlk(payload[2:4]) / 304.8
                        t1_speed_fps = decode_hlk(payload[4:6]) / 30.48
                        
                        print(f"Target 1 -> X: {t1_x_ft:.2f} ft, Y: {t1_y_ft:.2f} ft, Speed: {t1_speed_fps:.2f} ft/s")
                        break # Exit inner loop and go back to sleep for 2s
                        
except KeyboardInterrupt:
    ser.close()
