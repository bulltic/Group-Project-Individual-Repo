import serial

# Open UART0 on GPIO 14/15
ser = serial.Serial('/dev/ttyAMA0', 256000, timeout=1)
print("Listening for radar data (All Filters Disabled)...")

def decode_hlk(byte_data):
    # HLK sensors use the highest bit (Bit 15) purely as a sign bit
    val = byte_data[0] + (byte_data[1] << 8)
    if val & 0x8000: # If the 15th bit is a 1, it's negative
        return -(val & 0x7FFF)
    return val

try:
    while True:
        # Sync to the header
        if ser.read(1) == b'\xaa':
            if ser.read(1) == b'\xff' and ser.read(1) == b'\x03' and ser.read(1) == b'\x00':
                payload = ser.read(26)
                
                if len(payload) == 26:
                    # Extract bytes for Target 1
                    t1_x = decode_hlk(payload[0:2])
                    t1_y = decode_hlk(payload[2:4])
                    t1_speed = decode_hlk(payload[4:6])
                    
                    # Print unconditionally, even if values are 0
                    print(f"Target 1 -> X: {t1_x} mm, Y: {t1_y} mm, Speed: {t1_speed}")
                    
except KeyboardInterrupt:
    ser.close()
