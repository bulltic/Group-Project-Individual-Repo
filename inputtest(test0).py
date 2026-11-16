import serial

ser = serial.Serial('/dev/ttyAMA0',256000, timeout=1)

print("listening for HLK-LD2450 data...")
try:
	while True:
		if ser.in_waiting > 0:
			data = ser.read(ser.in_waiting)
			print(data.hex())
except KeyboardInterrupt:
	ser.close()
