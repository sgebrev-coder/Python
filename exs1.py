start=input("Начало на работното време:")
start_hour,start_minute=map(int, start.split(':'))
end=input("Край на работното време:")
end_hour,end_minute=map(int, end.split(':'))
work_hours=(end_hour+end_minute/60)-(start_hour+start_minute/60)
salary_per_hour=float(input("Заплата на час:"))
total_salary=work_hours*salary_per_hour
print("Часове за деня", work_hours, "часа")
print("Заплата за деня:", total_salary, "лева")
