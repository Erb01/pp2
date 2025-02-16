#task1
from datetime import datetime, timedelta
current_date = datetime.now()
new_date = current_date - timedelta(days=5)
print("Date after subtracting 5 days:", new_date.strftime("%Y-%m-%d"))

#task2
from datetime import datetime, timedelta
today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
print("Today:", today.strftime("%Y-%m-%d"))
print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))

#task3
from datetime import datetime
current_time = datetime.now().replace(microsecond=0)
print(current_time)

#task4
from datetime import datetime
date1 = datetime(2024, 2, 10, 12, 30, 15)
date2 = datetime(2024, 2, 15, 14, 45, 30)
difference = abs((date2 - date1).total_seconds())
print(date1)
print(date2)
print(difference)
