from datetime import datetime #imported datetime library

invoices = [
    {"party": "ABC Traders", "bill no": "B101", "bill_date": "2025-01-01", "amount": 12000},
    {"party": "XYZ Logistics", "bill_no": "B102", "bill_date": "2025-03-01", "amount": 8000},
    {"party": "PQR Industries", "bill_no": "B103", "bill_date": "2024-12-15", "amount": 15000}
] #local database of outstanding can be replaced with actual one

credit_days = {
    "ABC Traders" : 30,
    "XYZ Logistics" : 60,
    "PQR Industries" : 45
} #credit days data for each customer

today = datetime.strptime("2025-04-28","%Y-%m-%d") #strptime converts today variable into datetime object

overdue_list=[] #actual output list that contains data of late paying customers.

for inv in invoices: #inv iterator for invoices array
    bill_date = datetime.strptime(inv["bill_date"],"%Y-%m-%d") #bill_date is also converted to datetime object.
    days_due = (today - bill_date).days #calculating days_due by subtracting bill_date from today to get the days due .days is used to convert the subtracted variable into int format else it will be in timedelta format and we cant perform operations on it 
    if days_due < 0: #managing edge case of days_due of being less than 0 that is bill_date > today
        continue #it is used to skip this iteration and move to next line in code..
    if inv["amount"] < 1000: #managing edge case of amount < 1000, but i feel there is no need of it.. i mean even 1rs. outstanding has to be cleared.
        continue
    if days_due > credit_days.get(inv["party"], 45): #checking whether days_due is greater than the credit days of the customer by using get function of a dictionary passing the party name as first param but dont know why is there need of 2nd param as 45.. 
        inv["days_due"] = days_due #if a customer has not paid past the credit days then its day_due are being added to the original invoices array.. this can be seen when invoices is printed.
        overdue_list.append(inv) #such invoices whose due_days > credit days are appended to overdue_list array which contains invoices dict.

overdue_list = sorted(overdue_list, key=lambda x:x["days_due"], reverse=True) #this is used to sort the invoices in descending order.. 1st param is the list on which sorting is to be applied, 2nd param is the comparison param like on which key the comparison should be performed, 3rd param is to decide whether to get asc or dsc..

for item in overdue_list:
    print(item) #outpurtting the final overdue_list.