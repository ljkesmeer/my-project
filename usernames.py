
with open("/Users/kes/Downloads/S5K1R5S0SQ6E0Xiq8CthJA_fb407db2e4964801bdfa2e5b508281f1_tutorialdata/www1/secure_copy.txt", "r") as file:
    text_file = file.read()

new_users = "ljkesmeer, lulose, faly, Abner, jose"
with open("/Users/kes/Downloads/S5K1R5S0SQ6E0Xiq8CthJA_fb407db2e4964801bdfa2e5b508281f1_tutorialdata/www1/secure_copy.txt", "a") as file:
    username = file.write(new_users)
    usernames = file.split()

def count_user(login_list, current_user):
    counter = 0
    for login in login_list:
        if login == current_user:
            counter = counter + 1
    #if counter >= 3:
      #  return "You have tried to login three or more times. Your account has been locked."
    #else:
     #   return " You can log in!"
    print(current_user, counter)
    print("line 8, inside conditionnal")
        
    
count_user(usernames, "ppiere")

