salaries = {
    "Ani": int(input("enetr ani's salary ")),
    "Rahul": int(input("enetr rahul's salary ")),
    "Sneha": int(input("enetr Sneha's salary ")),
    "Raj": int(input("enetr Raj's salary "))
}
x = int(input("enetr basic must salary "))
for key, value in salaries.items():
    if(salaries[key] < x):
        salaries[key] +=500
print(salaries)