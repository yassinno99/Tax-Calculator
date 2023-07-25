print("Welcome to my Tax Calculator (2023)!\nAvailable regions: Italy & Netherlands\n")
def reseting():
    region = input("Select your region (Type: 'italy'/'netherlands'): ").lower()
    if region == 'italy':
        money = input("You have selected Italy\nEnter your yearly income (In Euros, Example: 69455.65): ")
        float_money = float(money)
        if 0 <= float_money <= 15000:
            print("Your taxes in percentage: 23%")
            tax = float_money * 0.23
            final_income = float_money * 0.77
            print("Your taxes amount: %.2f€" % tax)
            print("Your final income: %.2f€" % final_income)
        elif 15000 < float_money >= 28000:
            print("Your tax in percentage: 25%")
            tax = float_money * 0.25
            final_income = float_money * 0.75
            print("Your taxes amount: %.2f€" % tax)
            print("Your final income: %.2f€" % final_income)
        elif 28000 < float_money >= 50000:
            print("Your tax in percentage: 35%")
            tax = float_money * 0.35
            final_income = float_money * 0.65
            print("Your taxes amount: %.2f€" % tax)
            print("Your final income: %.2f€" % final_income)
        elif 50000 < float_money:
            print("Your tax in percentage: 43%")
            tax = float_money * 0.43
            final_income = float_money * 0.57
            print("Your taxes amount: %.2f€" % tax)
            print("Your final income: %.2f€" % final_income)
        else:
            print("Error... Typed Negative Income... Resets Program...")
            reseting()

    elif region == 'netherlands':
        money = input("You have selected Netherlands\nEnter your yearly income (In Euros, Example: 69455.65€): ")
        float_money = float(money)
        if 0 <= float_money <= 34712:
            print("Your taxes in percentage: 9.7%")
            tax = float_money * 0.097
            final_income = float_money * 0.903
            print("Your taxes amount: %.2f€" % tax)
            print("Your final income: %.2f€" % final_income)
        elif 34712 < float_money >= 68507:
            print("Your tax in percentage: 37.35%")
            tax = float_money * 0.3735
            final_income = float_money * 0.6265
            print("Your taxes amount: %.2f€" % tax)
            print("Your final income: %.2f€" % final_income)
        elif 68508 <= float_money:
            print("Your tax in percentage: 49.5%")
            tax = float_money * 0.495
            final_income = float_money * 0.505
            print("Your taxes amount: %.2f€" % tax)
            print("Your final income: %.2f€" % final_income)
        else:
            print("Error... Typed Negative Income... Resets Program...")
            reseting()
    else:
        print("Invalid input ... error ... RESETS THE PROGRAM ... ENTER AN AVAILABLE REGION REGION!")
        reseting()

reseting()