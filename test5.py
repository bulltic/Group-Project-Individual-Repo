import serial
import time
import csv
import sys

label_map = {"0": "Empty Room", "1": "Pet", "2": "Walking", "3": "Falling"}

# Check if you passed a valid number when starting the script
if len(sys.argv) < 2 or sys.argv[1] not in label_map:
    print("Error: Please provide a valid action number when starting the script.")
    print("Example: python3 data_logger.py 2")
    print("--- Available Codes ---")
    for key, name in label_map.items():
        print(f"  {key} -> {name}")
    sys.exit(1)

user_input = sys.argv[1]
current_label = int(user_input)
filename = f"radar_data_{label_map[user_input].replace(' ', '_')}_{int(time.time())}.csv"

# Open UART0 on GPIO 14/15
ser = serial.Serial('/dev/ttyAMA0', 256000, timeout=1)

def decode_hlk(byte_data):
    val = byte_data[0] + (byte_data[1] << 8)
    if val == 0: return 0
    return (val & 0x7FFF) if (val & 0x8000) else -val

print(f"Recording '{label_map[user_input]}' data to {filename}...")
print("Press Ctrl+C to stop recording when finished.")

# Open CSV and write headers
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "X_ft", "Y_ft", "Speed_fps", "Label"])

    try:
        while True:
            if ser.read(1) == b'\xaa' and ser.read(1) == b'\xff' and ser.read(1) == b'\x03' and ser.read(1) == b'\x00':
                payload = ser.read(26)
                if len(payload) == 26:
                    t1_x_ft = decode_hlk(payload[0:2]) / 304.8
                    t1_y_ft = decode_hlk(payload[2:4]) / 304.8
                    t1_speed_fps = decode_hlk(payload[4:6]) / 30.48
                    
                    # Log the exact moment, the coordinates, and the label to the CSV
                    writer.writerow([time.time(), t1_x_ft, t1_y_ft, t1_speed_fps, current_label])
                    
    except KeyboardInterrupt:
        print(f"\nSaved {filename}. Ready for the next recording!")
        ser.close()
