import random
import datetime
import os
import time
import json

l_target_path = "C:\\Users\\Hemaxi\\Desktop\\Programing\\python\\project-02\\bills\\"


l_store_id = random.randint(1, 4)
now = datetime.datetime.now()
l_bill_id = now.strftime("%Y%m%d%H%M%S")


#generate random date:

start_date =  datetime.date(2000, 1, 1)
end_date = datetime.date(2020, 1, 1)
time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days
random_number_of_days = random.randrange(days_between_dates)
l_date = str( start_date + datetime.timedelta(days=random_number_of_days))

l_bill_details = {}

for i in range(random.randint(1, 25)):

        l_prod_id = random.randint(1,25)
        l_qty = random.randint(1,20)
        l_bill_details[l_prod_id] = l_qty

l_data = { "bill_id": l_bill_id
              ,"store_id":l_store_id
              ,"bill_date":l_date
              ,"bill_details":l_bill_details}

              
#print(json.dumps(l_data))
new_file = open(l_target_path + l_bill_id + ".json", "w")
new_file.write(json.dumps(l_data))
new_file.close()




