# Inventory Management System

Stores
    Billing Data

Products  (25 Rows)
    prod_id     (PK)
    prod_type (food, frozen, office, cleaning supplies, apparel)
    prod_name
    qty
    price
    price_eff_st_date  20000101
    price_eff_ed_date  30000101

Store                   (4 Stores)
    store_id      (pk)
    store_address
    
billdata
    bill_id     (PK)
    store_id    (fk)
    bill_date
    bill_total   ?

billdetails
    billdetail_id  (PK) 
    bill_id        (FK)
    prod_id         (FK)
    qty
    line_total   ?


Bill Generator

billid,storeid,date
prod_id qty
prod_id qty
prod_id qty
prod_id qty
prod_id qty
prod_id qty


    
    