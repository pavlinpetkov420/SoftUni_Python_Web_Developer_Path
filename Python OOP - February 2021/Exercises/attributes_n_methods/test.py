from datetime import *
from calendar import month_name

date = "12.10.1987"

date_obj = datetime.strptime(date, "%d.%m.%Y")
# date_obj = datetime.strptime(date, "%d.%m.%Y")
date_f = date_obj.strftime("%d.%B.%Y")
y = date_obj.year

print(date_obj, date_f)
print(date_f.split('.'))

