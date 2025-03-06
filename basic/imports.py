import math
import random
from datetime import datetime

print(math.pow(10, 3))
print(random.randint(100, 500))
print(f"Report generated on: {datetime.now()}")
current_time = datetime.now()
print(f"Report generated on: {current_time.strftime('%d/%m/%Y %H:%M:%S')}")


