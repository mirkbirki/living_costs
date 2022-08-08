living_cost = float(input("Ange faktisk boendekostnad i siffror (Hyra/avgift bostadsrätt/bolåneränta (ej ammortering)/uppvärmningskostnad/"
                          "kall-/varmvatten/avfall, EJ elkostnad!)"": "))
civil_status = input("Är den sökande ensamstående? (ja/nej): ")
if civil_status == "ja":
    civil_status = float(5158)
elif civil_status == "nej":
    civil_status = float(8520)
children = input("Har den sökande barn? (ja/nej): ")
if children == "ja":
    ch_age_1 = input("Är något av barnen 0-6 år? (ja/nej): ")
    if ch_age_1 == "ja":
        ch_age_1 = int(input("Hur många? (Siffra/siffror): "))
        count_1 = ch_age_1
        ch_age_1 = float(ch_age_1  * 2756)
    else:
        ch_age_1 = 0
        count_1 = 0
    ch_age_2 = input("Är något av barnen 7-10 år? (ja/nej): ")
    if ch_age_2 == "ja":
        ch_age_2 = int(input("Hur många? (Siffra/siffror): "))
        count_2 = ch_age_2
        ch_age_2 = float(ch_age_2  * 3308)
    else:
        ch_age_2 = 0
        count_2 = 0
    ch_age_3 = input("Är något av barnen 11-14 år? (ja/nej): ")
    if ch_age_3 == "ja":
        ch_age_3 = int(input("Hur många? (Siffra/siffror): "))
        count_3 = ch_age_3
        ch_age_3 = float(ch_age_3  * 3860)
    else:
        ch_age_3 = 0
        count_3 = 0
    ch_age_4 = input("Är något av barnen 15 år? (ja/nej): ")
    if ch_age_4 == "ja":
        ch_age_4 = int(input("Hur många? (Siffra/siffror): "))
        count_4 = ch_age_4
        ch_age_4 = float(ch_age_4 * 4411)
    else:
        ch_age_4 = 0
        count_4 = 0
else:
    if children == "nej":
        ch_age_1, ch_age_2, ch_age_3, ch_age_4 = 0, 0, 0, 0
        count_1, count_2, count_3, count_4 = 0, 0, 0, 0
total = living_cost + civil_status + ch_age_1 + ch_age_2 + ch_age_3 + ch_age_4
normalbelopp = civil_status + ch_age_1 + ch_age_2 + ch_age_3 + ch_age_4
count = count_1 + count_2 + count_3 + count_4
if count == 2:
    flb = 150
elif count == 3:
    flb = 730
elif count == 4:
    flb = 1740
elif count == 5:
    flb = 2990
elif count >= 6:
    flb = 4240
else:
    flb = 0
child_benefit = count * 1250 + flb
income = float(input("Ange sammanlagd månadsinkomst från lön, annan arbetsrelaterad inkomst, förmögenhet, make/sambo, övrigt (Siffror): "))
result = income + child_benefit - total

print("Månadsinkomst:", income)
if count_1 > 0:
    print("Antal barn 0-6 år:", count_1, "Barnbidrag:", count_1 * 1250)
if count_2 > 0:
    print("Antal barn 7-10 år:", count_2, "Barnbidrag:", count_2 * 1250)
if count_3 > 0:
    print("Antal barn 11-14 år:", count_3, "Barnbidrag:", count_3 * 1250)
if count_4 > 0:
    print("Antal barn 15 år:", count_4, "Barnbidrag:", count_4 * 1250)
if count >=2:
    print("Flerbarnstillägg:", flb)
print ("Avdrag för barnbidrag (Inkl. ev. flerbarnstillägg):", child_benefit)
print("Normalbelopp:", normalbelopp)
print("Boendekostnad:", living_cost)
print("Förbehållsbelopp:", total)
if result >= 0:
    print("RESULTAT: Försörjningskrav uppfyllt, med marginal:", result)
else:
    print("RESULTAT: Försörjningskrav ej uppfyllt, underskott:", result)







