import pyvisa
import time

rm = pyvisa.ResourceManager("@py")
ports = rm.list_resources()
print(ports)

device = rm.open_resource(
    "ASRL8::INSTR", read_termination="\r\n", write_termination="\n")

while True:
    device.query(f"OUT:CH0 {1023}")
    time.sleep(0.1)
    device.query(f"OUT:CH0 {0}")
    time.sleep(0.1)