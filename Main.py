#Validation Is Based On LUHN Algorithm

print("\n### ###### CARD AUTHENTICATION ###### ###")

import re
from datetime import date

while True:

    card = input("\nPlease Enter Card Number In Order To Validate :\t")

    type_1 = r'^[0-9]{4,4} [0-9]{4,4} [0-9]{4,4} [0-9]{4,4}$'
    type_2 = r'^[0-9]{4,4}-[0-9]{4,4}-[0-9]{4,4}-[0-9]{4,4}$'
    type_3 = (14<=len(card)<=16 and card.isdigit())

    if any([re.search(type_1, card), re.search(type_2, card), type_3]):
        break
    else:
        print("\nSorry! Its Invalid Input")

exp_mm = int(input("\nPls Enter The Expiry Month In MM :\t"))
        
exp_yy = int(input("\nPls Enter The Expiry Year In YYYY :\t"))

if exp_mm < 1 or exp_mm > 12 :
    print("\nInvalid Month Entry\n")
    quit()

elif exp_yy < 1950 or exp_yy > 2050 :
    print("\nInvalid Year Entry\n")
    quit()

now_date = date.today()
current_mm = now_date.month
current_yy = now_date.year

if exp_yy<current_yy:
    print("\nThis Card Has Been Expired Previous Year :/ \n")
    quit()

elif exp_yy==current_yy and exp_mm<current_mm :
    print("\nThis Card Has Been Expired Few Months Back :/ \n")
    quit()
    
if card.startswith("4"):
    card_type = "VISA"
elif 51 <= int(card[:2]) <= 55:
    card_type = "MasterCard"
elif card.startswith("34") or card.startswith("37") :
    card_type = "AmEx"
elif card.startswith("35"):
    card_type = "RuPay"
else:
    card_type = "UnKnown"

#seprators if any
card = card.replace(" ", "").replace("-","").replace(".","")

#mapping the string into list 
card = list(map(int,card))

#extracting the validator  //added later
valid_digit = card[-1]

#digits after extracting validator
card = card[:-1]

#reversing the order of remaining 15 
card.reverse()

#doubling the every even indices
for i in range(len(card)):
    if i%2==0:
        card[i] = card[i]*2
        if card[i]>9:
            card[i] = card[i]-9

#validating the sum%10==0 

if(sum(card) + valid_digit) %10 ==0:
    print("\nCard Is Valid :) ")
    print("\nCard Type : ", card_type,"\n")
    print("No Credentials Were Saved...Thanks For Using Our Service\n")
else:
    print("\n :/ Invalid One..Please Check Again\n")