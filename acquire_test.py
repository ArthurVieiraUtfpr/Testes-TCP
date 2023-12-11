import socket
import struct
import time

# Connect to Acquire (Panther) server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 4444))

# Send command and parameters
# Action ID: 166 = SetParamAcceptance
s.send(struct.pack('>h', 166))

# SubAction ID: 7 = SetNumericalGain
s.send(struct.pack('>h', 7))

# Parameter: Salvo number = 0 (first salvo)
s.send(struct.pack('>h', 0))

# Parameter: Gain value in dB
s.send(struct.pack('>d', 15))

# Wait for 0.1 seconds
time.sleep(0.1)

# Receive return value
# Receive status
result = s.recv(2)
status = struct.unpack('>h', result)[0]
print("Status =", status)

# Close the socket
s.close()
