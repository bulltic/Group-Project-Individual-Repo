import serial
import struct

# Open UART0 on GPIO 14/15
ser = serial.Serial('/dev/ttyAMA0', 256000, timeout=1)
print("Listening for radar data (syncing to stream)...")

def parse_target_data(full_frame):
    # Unpack Target 1 data (Bytes 4 to 11)
    # '<h' means little-endian signed 16-bit integer
    target1_x = struct.unpack('<h', full_frame[4:6])[0]
    target1_y = struct.unpack('<h', full_frame[6:8])[0]
    target1_speed = struct.unpack('<h', full_frame[8:10])[0]
    
    # Only print if a target is actually detected (Y distance > 0)
    if target1_y > 0: 
        print(f"Target 1 -> X: {target1_x}mm, Y: {target1_y}mm, Speed: {target1_speed}")

try:
    while True:
        # Search for the AA FF 03 00 header byte-by-byte
        if ser.read(1) == b'\xaa':
            if ser.read(1) == b'\xff':
                if ser.read(1) == b'\x03':
                    if ser.read(1) == b'\x00':
                        # Header found! Read the remaining 26 bytes
                        payload = ser.read(26)
                        
                        if len(payload) == 26:
                            # Reconstruct the 30-byte frame and parse it
                            full_frame = b'\xaa\xff\x03\x00' + payload
                            parse_target_data(full_frame)
                            
except KeyboardInterrupt:
    ser.close()
