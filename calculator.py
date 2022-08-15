salary = float(input("What is the applicant's monthly net salary?: "))
other_income = float(input("How much does the applicant have in other monthly net income?: "))
income_from_business = float(input("How much does the applicant have in monthly net income from an owned business?: "))
fortune = float(input("How much does the applicant have in net fortune?: "))
monthly_income = salary + other_income + income_from_business + fortune/48

rent_charge = float(input("How much is the applicants monthly rent/charge?: "))
operating_cost = float(input("How much is the applicants monthly operating cost?: "))
interest_expense = float(input("How much is the applicants monthly interest expense?: "))
living_cost = rent_charge + operating_cost + interest_expense

civil_status = input("Is the applicant single? (yes/no): ")
if civil_status == "yes":
    civil_status = float(5158)
elif civil_status == "no":
    civil_status = float(8520)
children = input("Does the applicant have children? (yes/no): ")
if children == "yes":
    ch_age_1 = input("Are any of the children 0-6 years old? (yes/no): ")
    if ch_age_1 == "yes":
        ch_age_1 = int(input("How many? (Number): "))
        count_1 = ch_age_1
        ch_age_1 = float(ch_age_1  * 2756)
    else:
        ch_age_1 = 0
        count_1 = 0
    ch_age_2 = input("Are any of the children 7-10 years old? (yes/no): ")
    if ch_age_2 == "yes":
        ch_age_2 = int(input("How many? (Number): "))
        count_2 = ch_age_2
        ch_age_2 = float(ch_age_2  * 3308)
    else:
        ch_age_2 = 0
        count_2 = 0
    ch_age_3 = input("Are any of the children 11-14 years old? (yes/no): ")
    if ch_age_3 == "yes":
        ch_age_3 = int(input("How many? (Number): "))
        count_3 = ch_age_3
        ch_age_3 = float(ch_age_3  * 3860)
    else:
        ch_age_3 = 0
        count_3 = 0
    ch_age_4 = input("Are any of the children 15 years old? (yes/no): ")
    if ch_age_4 == "yes":
        ch_age_4 = int(input("How many? (Number): "))
        count_4 = ch_age_4
        ch_age_4 = float(ch_age_4 * 4411)
    else:
        ch_age_4 = 0
        count_4 = 0
else:
    if children == "no":
        ch_age_1, ch_age_2, ch_age_3, ch_age_4 = 0, 0, 0, 0
        count_1, count_2, count_3, count_4 = 0, 0, 0, 0
normal_amount = civil_status + ch_age_1 + ch_age_2 + ch_age_3 + ch_age_4
count = count_1 + count_2 + count_3 + count_4
if count == 2:
    mcb = 150
elif count == 3:
    mcb = 730
elif count == 4:
    mcb = 1740
elif count == 5:
    mcb = 2990
elif count >= 6:
    mcb = 4240
else:
    mcb = 0
child_benefit = count * 1250 + mcb

maintenance_support = input("Does the applicant receive maintenance support? (yes/no): ")
if maintenance_support == "yes":
    maintenance_support = float(input("How much does the applicant receive in monthly maintenance support?: "))
else:
    maintenance_support = 0

reserved_amount = normal_amount + living_cost

result = monthly_income + child_benefit + maintenance_support - reserved_amount

print("Net salary:", salary)
print("Other income:", other_income)
print("Income from business:", income_from_business)
print("Fortune/month:", fortune/48)
print("Monthly household income:", monthly_income)

if civil_status == float(5158):
    print("Normal amount for single:", civil_status)
elif civil_status == float(8520):
    print("Normal amount for partnership:", civil_status)

if count_1 > 0:
    print("Amount of children 0-6 years old:", count_1, "Normal amount for children 0-6 years old:", count_1 * 2756)
if count_2 > 0:
    print("Amount of children 7-10 years old:", count_2, "Normal amount for children 7-10 years old:", count_2 * 3308)
if count_3 > 0:
    print("Amount of children 11-14 years old:", count_3, "Normal amount for children 11-14 years old:", count_3 * 3860)
if count_4 > 0:
    print("Amount of children 15 years old:", count_4, "Normal amount for children 15 years old:", count_4 * 4411)

print ("Normal amount):", civil_status + ch_age_1 + ch_age_2 + ch_age_3 + ch_age_4)

print("Rent/charge:", rent_charge)
print("Operating cost:", operating_cost)
print("Interest expense:", interest_expense)
print("Living cost:", living_cost)

if count_1 > 0:
    print("Amount of children 0-6 years old:", count_1, "Child benefit children 0-6 years old:", count_1 * 1250)
if count_2 > 0:
    print("Amount of children 7-10 years old:", count_2, "Child benefit children 7-10 years old:", count_2 * 1250)
if count_3 > 0:
    print("Amount of children 11-14 years old:", count_3, "Child benefit children 11-14 years old:", count_3 * 1250)
if count_4 > 0:
    print("Amount of children 15 years old:", count_4, "Child benefit children 15 years old:", count_4 * 1250)
if count >=2:
    print("Multiple child benefit:", mcb)
print ("Sum child benefit (incl. eventual multiple child benefit):", child_benefit)
print("Maintenance support:", maintenance_support)

print("Reserved amount:", reserved_amount)

if result >= 0:
    print("STATUS: Maintenance requirement fulfilled, with a marginal of:", result)
else:
    print("STATUS: Maintenance requirement NOT fulfilled, with a deficit of:", result)







