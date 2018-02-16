import Data

# serialize telemetry
tlm = Data.Telemetry(10, 20, 30, 40, 0xee)
open("tlm.bin", "wb").write(tlm.serialize())

# deserialize telemetry
data = open("tlm.bin", "rb").read()
tlm2 = Data.Telemetry.deserialize(data[0:Data.Telemetry.recordSize()])

print tlm
print tlm2
