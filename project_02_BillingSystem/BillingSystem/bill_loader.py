import datetime
import os
import pymysql
import json

# Update the data to set qty for all products to 1
# update Products set qty = 1;
# commit;


#
l_bills_path = "E:/code/PYTHON_TRAINING/Training/Feb20201/InventoryManagementSystem/bills/"
l_processed_path = "E:/code/PYTHON_TRAINING/Training/Feb20201/InventoryManagementSystem/processed_bills/"
l_errors_path = "E:/code/PYTHON_TRAINING/Training/Feb20201/InventoryManagementSystem/error_bills/"

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='tinitiate', db='inventorymanagement')
cursor = conn.cursor()

l_bill_insert = "insert into billdata ( bill_id, store_id, bill_date) values ({0},{1},STR_TO_DATE('{2}','%Y-%m-%d %H:%i%s'));"
l_bill_det_insert = "insert into billdetails (billdetail_id, bill_id, prod_id,qty) values ({0},{1},{2},{3});"

# while True:
    # entries = os.listdir(l_bills_path)
entries = ["20210310212340.json","20210310212343.json"]
print(entries)
for file_name in entries:
    with open(l_bills_path + file_name, 'r') as f:
        data = f.read()
        print(data)
        dataj = json.loads(data)
        print(dataj["bill_id"])
        print(dataj["store_id"])
        print(dataj["bill_date"])
        
        # Validate Data, generate errors if any
        # If errors Move "l_bills_path + file_name" into "l_errors_path"
        
        # Load the "data" into DB Tables, Bill / Bill Details
        # insert into Bill
        # insert into BillDetails
        # Update billdetails.line_total and bill.bill_total
        try:
            print(l_bill_insert.format(dataj["bill_id"],dataj["store_id"],dataj["bill_date"]))
            # cursor.execute(l_bill_insert.format(dataj["bill_id"],dataj["store_id"],dataj["bill_date"]))
        except:
            log.critical('JSON File '+ file_name + ' load failed!!')
            # Move "l_bills_path + file_name" into "l_errors_path + file_name"
        else:    
            x = 0
            for product_id, qty in dataj["bill_details"].items():
                x+=1
                try:
                    print(l_bill_det_insert.format(int(dataj["bill_id"])+x,dataj["bill_id"],product_id,qty))
                    # cursor.execute(l_bill_det_insert.format(int(dataj["bill_id"])+x,dataj["bill_id"],product_id,qty))
                    
                    #delete from billdetails where bill_id = dataj["bill_id"];
                    #delete from bill where bill_id = dataj["bill_id"];

                except:
                    log.critical('JSON File '+ file_name + ' load failed!!')
                    # Move "l_bills_path + file_name" into "l_errors_path + file_name"
                else:
                    # Move "l_bills_path + file_name" into "l_processed_path + file_name"

    -- update line total
    -- update bill total
    
    # time.sleep(60)