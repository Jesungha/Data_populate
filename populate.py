import math
import random
def printout():
    f = open("order_table.csv" ,"w")
    f.write("c_order_id, c_order_date, c_order_time, c_order_subtotal, c_order_tax, c_order_total, c_order_payment_type\n")
    total_sales = 0

    i = 0
    for month in range(2,13):
        if month in [1,3,5,7,8,10,12]:
            days = 31
        elif month == 2:
            days = 28
        else:
            days = 30
        for day in range(1,days+1):
            day_sale = 0
            if month == 8 and day == 23:
                day_limit = 8000
            elif month == 1 and day == 17:
                day_limit = 8000
            else:
                day_limit = 2750
            while day_sale < day_limit:
                if month in [2,3,4,5,6,7,8,9,10,11,12]:
                    year = "2023-"
                else:
                    year = "2024-"
                f.write(str(i)+", "+ year+ str(month)+ "-" + str(day)+ ", ")
                f.write(str(random.randrange(11,23))+ ":" + str(random.randrange(0,60))+ ":" + str(random.randrange(0,60))+ ", ") # 11am to pm
                subtotal = random.randrange(5,30)
                tax = subtotal * .0825
                total = subtotal + tax
                total_sales += subtotal
                day_sale += subtotal
                f.write(str(subtotal)+ ", ") # subtotal
                f.write(str(format(tax, '.2f'))+ ", ")# tax
                f.write(str(format(total, '.2f'))+ ", ")   # total
                payments = ["cash", "credit", "debit"]
                f.write(payments[random.randrange(0,3)]+ "\n")
                i += 1
 
    for day in range(1,32):
        day_sale = 0
        if day == 17:
            day_limit = 8000
        else:
            day_limit = 2750
        while day_sale < day_limit:
            f.write(str(i)+", "+ "2024-"+ str(1)+ "-" + str(day)+ ", ")
            f.write(str(random.randrange(11,23))+ ":" + str(random.randrange(0,60))+ ":" + str(random.randrange(0,60))+ ", ") # 11am to pm
            subtotal = random.randrange(5,30)
            tax = subtotal * .0825
            total = subtotal + tax
            total_sales += subtotal
            day_sale += subtotal
            f.write(str(subtotal)+ ", ") # subtotal
            f.write(str(format(tax, '.2f'))+ ", ")# tax
            f.write(str(format(total, '.2f'))+ ", ")   # total
            payments = ["cash", "credit", "debit"]
            f.write(payments[random.randrange(0,3)]+ "\n")
            i += 1
    print (total_sales)
    f.close()


if __name__ == "__main__":
    printout()