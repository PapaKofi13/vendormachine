
acct_bal = 30  #fixed ammount in the users acocunt
user_ammt  =  int(input("how much are you spending today?  : " ))


# code works fine, exits when user balance is zero 
# program works well and terminates when user enters 100
#fix iteration issue
#push to github

while acct_bal < user_ammt and acct_bal != 0 and user_ammt != 100:  #check ammount entered by user
    print(f"{user_ammt}ghc is more than {acct_bal}ghc kindly enter another ammount ") #ammount inputed by user is more than ammount in balance
    user_ammt = int(input("kindly enter another ammount : "  ))
    print("your account balance is 0. kindly top up") 
    break
else:
    if user_ammt == 100:
        print(f" you entered 100 program terminating")
    elif user_ammt == 30:
        print(" you spent all 30ghs thank you")
if acct_bal > user_ammt:  
    new_bal = acct_bal - user_ammt #subtract user inout from account if ammount is less than acc
    print(f" you had {acct_bal}ghc and spent {user_ammt}ghc so you now have {new_bal}ghc\n ")
    decide = input(f"you have {new_bal}ghc left would you like to make another purchase ? Y for YES or N for NO :\n" ).lower()
    if decide == "n":
        print(f"I hope you enjoyed our services. See you soon your balance is now {new_bal}ghs ")
    elif decide == "y" and new_bal != 0:
        print(f"you have {new_bal}ghs left how much would you like to spend? ")
        user_ammt = int(input(f"how much more are spending out of {new_bal}ghs ? : "))
        final_balance = new_bal - user_ammt #subtract further transactions from user 
        print(f"you spent {user_ammt}ghs and have {final_balance}ghs left")
        
        
        
    
        

# while user_ammt == 0:
#     print(f" sorry you entered {user_ammt}. no food for your broke ass. Bye!")
#     break
# while user_ammt == 100:
#     print(f"{user_ammt} is your maximun bro you are done spending for the day")
#     break
    
    

# vend = ""
# bal = 30 

# spend = int(input("how much are you going to spend today? :"))
# running = False
# while True:
#     if bal < 30:
#         deduct = bal - spend
#         print(f"you had {bal}ghs and spent {spend}ghs so you now have {deduct}ghs ")
#     elif spend == 100:
#         print(f"you chose to terminate theprogram. goodbye your balance is {deduct}ghs")
#         break
#     else:
#         print("you didnt enter any ammount")


