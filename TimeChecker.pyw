from datetime import datetime

file = open(r"#Type the path here", "a")
file.write(datetime.now(), "\n")
file.close()
