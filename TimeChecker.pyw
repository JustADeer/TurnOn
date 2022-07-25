from datetime import datetime
from pathlib import Path
f = Path(__file__).with_name("TimeChecker.txt").open("a")
f.write(str(datetime.now()) + "\n")
f.close()
