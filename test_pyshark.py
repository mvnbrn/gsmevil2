import pyshark
print("start work")
capture = pyshark.LiveCapture(interface='lo')
capture.sniff(timeout=1)
#capture
print(capture)
for packet in capture:
    print(packet.highest_layer)
