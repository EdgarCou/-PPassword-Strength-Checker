from colorama import Fore, init
import getpass

init(autoreset=True)

def Password_Check(password):
    
    score = 0
    
    if len(password) >= 12 :
            score += 1
    else:
        print(Fore.RED + "\nYour password is too small. At least 12 characters")
        
    if any(c.isupper() for c in password):
        score += 1
    else:
        print(Fore.RED + "\nYou must have at least one capital letter.")
        
    if any(c.islower() for c in password):
        score += 1
    else:
        print(Fore.RED + "\nYou must have at least one lowercase letter.")
        
    if any(c.isdigit() for c in password):
        score += 1
    else:
        print(Fore.RED + "\nYou must have at least one digit.")
        
    special_char = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
    if any(c in special_char for c in password):
        score += 1
    else:
        print(Fore.RED + "\nYou must have at least one special character.")
        
    return score

def evaluate_score(score):
    if score <= 2:
        return Fore.RED + "\nThe password is too weak\n"
    elif 2 < score < 5 :
        return Fore.YELLOW + "\nThe password is not good enough, try to make it stronger\n"
    elif score == 5:
        return Fore.GREEN + "\nThe password is strong enough!\n"
    
    
def main():    
    print(Fore.BLUE + "\nWelcome to Password Checker!\n")
    password = getpass.getpass(Fore.CYAN + "Enter your password : ")

    score = Password_Check(password)

    print(evaluate_score(score))
    
main()