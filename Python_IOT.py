# hourly program

hourly_rate=float(input("Enter a Hours: "))
rate = float(input("Enter rate for each hour: "))

if hourly_rate<=40:
    total_pay=hourly_rate*rate

elif hourly_rate>40:
    regular_pay=40*rate
    overtime_hours=hourly_rate-40
    overtime_pay=overtime_hours*(rate*1.5)
    net_pay=overtime_pay+regular_pay

    print("Net_salary If he gave overtime",net_pay)
    print("without overtime: ",regular_pay)
    

