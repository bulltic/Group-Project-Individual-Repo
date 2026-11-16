import serial
import time

# Open UART0 on GPIO 14/15
ser = serial.Serial('/dev/ttyAMA0', 256000, timeout=1)
print("Listening for radar data (Updating every 0.5 seconds)...")

def decode_hlk(byte_data):
    val = byte_data[0] + (byte_data[1] << 8)
    if val == 0:
        return 0
    if val & 0x8000:
        return val & 0x7FFF
    else:
        return -val

last_print_time = 0

try:
    while True:
        # Continuously sync to the AA FF 03 00 header to keep data live
        if ser.read(1) == b'\xaa':
            if ser.read(1) == b'\xff' and ser.read(1) == b'\x03' and ser.read(1) == b'\x00':
                payload = ser.read(26)
                
                if len(payload) == 26:
                    current_time = time.time()
                    
                    # Output every 0.5 seconds
                    if current_time - last_print_time >= 0.5:
                        t1_x_ft = decode_hlk(payload[0:2]) / 304.8
                        t1_y_ft = decode_hlk(payload[2:4]) / 304.8
                        t1_speed_fps = decode_hlk(payload[4:6]) / 30.48
                        
                        # Check if anyone is actually detected
                        if t1_y_ft == 0 and t1_x_ft == 0:
                            print("No target detected")
                        else:
                            # 1. Translate Left / Right / Center (within ~1 inch of 0 is Center)
                            if abs(t1_x_ft) < 0.10:
                                position_str = "Center"
                            elif t1_x_ft < 0:
                                position_str = f"{abs(t1_x_ft):.2f} ft Left"
                            else:
                                position_str = f"{t1_x_ft:.2f} ft Right"
                                
                            # 2. Translate Speed (Approaching vs. Moving Away)
                            if abs(t1_speed_fps) < 0.05:
                                speed_str = "Stationary (0.00 ft/s)"
                            elif t1_speed_fps < 0:
                                speed_str = f"Approaching at {abs(t1_speed_fps):.2f} ft/s"
                            else:
                                speed_str = f"Moving Away at {t1_speed_fps:.2f} ft/s"
                                
                            print(f"Distance: {t1_y_ft:.2f} ft out | Position: {position_str} | Motion: {speed_str}")
                        
                        last_print_time = current_time
                    
except KeyboardInterrupt:
    ser.close()
