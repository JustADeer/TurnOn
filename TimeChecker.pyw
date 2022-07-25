from datetime import datetime

file = open(r"C:\Users\Yume\Desktop\Time.txt", "a")
file.write(datetime.now(), "\n")
file.close()
