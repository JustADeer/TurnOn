from datetime import datetime

file = open(r"C:\Users\Yume\Desktop\Times\Time.txt", "a")
file.write(datetime.now(), "\n")
file.close()
