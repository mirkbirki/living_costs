Living_cost = float(input("Ange boendekostnad i siffror (Hyra, avgift, bolåneränta (ej ammortering), uppvärmningskostnad, kallvatten, avfall, ej elkostnad)"":"))
Civil_status = input("Is the applicant single?")
if Civil_status == "yes":
    Civil_status = float(5200)
elif Civil_status == "no":
    Civil_status = float(8520)
print(type(Civil_status))
Children = input("Does the applicant have any children?")
if Children == "yes":
    ch_age_1 = input("Is any of the children 0-6 years old?")
    if ch_age_1 == "yes":
        ch_age_1  = int(input("How many?"))
        ch_age_1  = float(ch_age_1  * 2800)
    else:
        ch_age_1 = 0
    ch_age_2 = input("Is any of the children 7-13 years old?")
    if ch_age_2 == "yes":
        ch_age_2 = int(input("How many?"))
        ch_age_2 = float(ch_age_2  * 3000)
    else:
        ch_age_2 = 0
    ch_age_3 = input("Is any of the children over 14 years old?")
    if ch_age_3 == "yes":
        ch_age_3 = int(input("How many?"))
        ch_age_3 = float(ch_age_3  * 3200)
    else:
        ch_age_3 = 0
Total = Living_cost + Civil_status + ch_age_1 + ch_age_2 + ch_age_3
print(Total)