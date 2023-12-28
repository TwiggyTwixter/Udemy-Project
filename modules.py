import time as t

t.localtime()

time_now = t.localtime()
print("Transaction completed at", str(time_now.tm_hour) + "h" +str(time_now.tm_min) + "m")

time_now = t.time()
delivery_time = time_now + (86400 * 7)
print("Delivery day", str(t.localtime(delivery_time).tm_mon) + "/" + str(t.localtime(delivery_time).tm_mday) + "/" + str(t.localtime(delivery_time).tm_year))
print("Countdown:")
print("5")
t.sleep(1)
print("4")
t.sleep(1)
print("3")
t.sleep(1)
print("2")
t.sleep(1)
print("1")
t.sleep(1)
print("Program ending")