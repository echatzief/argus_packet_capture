import os

while True:
  os.system("ra -r packet.argus -s dur proto ")
  os.system("ra -r packet.argus -s dur proto state spkts dpkts rate sttl dttl sload dload sjit djit swin stcpb dtcpb tcprtt smeansz dmeansz")
