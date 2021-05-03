import json

with open('C:\\Users\\Hemaxi\\Desktop\\Programing\\python\\project-02\\bills\\20210429151710.json') as bill_path:
 with open('C:\\Users\\Hemaxi\\Desktop\\Programing\\python\\project-02\\pricesheet.json') as price_path:
 
  bill_data = json.load(bill_path)
  price_data = json.load(price_path) 



bill_details = [{
                "productId": []
                ,"quantity": []
                ,"price":[]}
               ,{"productId": []
                ,"quantity": []
                ,"price":[]}
               ]


P_bill_id = (bill_data["bill_id"])
print(P_bill_id)
p_store_id = (bill_data["store_id"])
print(p_store_id)
p_bill_date = (bill_data["bill_date"])  
print(p_bill_date)
# P_bill_total = (bill_data["bill_total"])
# print(P_bill_total)
P_bill_details = (bill_data["bill_details"])
print(P_bill_details)


p_data = { "bill_id":P_bill_id
           ,"store_id":p_store_id
           ,"bill_date":p_bill_date
          #  ,"bill_total":P_bill_total
           ,"bill_details":P_bill_details
         }
print(p_data)


p_target_path = "C:\\Users\\Hemaxi\\Desktop\\Programing\\python\\project-02\\processed_bills\\"

new_file = open(p_target_path + P_bill_id + ".json", "w")
new_file.write(json.dumps(p_data))
new_file.close()


