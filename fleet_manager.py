def main():
    init_database()
    display_menu()
    if choice == 1:

    elif choice == 2:

    elif choice == 3:
        
    elif choice == 4:
        
    elif choice == 5:
        
    elif choice == 6:
        
    elif choice == 7:
        
    elif choice == 8:
        
    return

def init_database():
    n = ["Spock", "Sisko", "Quark", "Kirk", "Maxwell"]
    r = ["Commander", "Captain", "Civillian", "Rear Admiral", "Vice Admiral" ]
    d = ["Science" "Command", "None", "Command", "Command"]
    i = ["001", "002", "003", "004", "005"]
    return n, r, d, i

def display_menu():
    user_name = input("Please input full name ")
    while True:
        print("""-----Menu----- 
1. Add member 
2. Remove member
3. Update Rank
4. Display Roster
5. Search Crew
6. Filter by division
7. Calculate Payroll
8. Count Officers
User - """ + user_name)
        choice = int(input(""))
        if choice > 0 and choice < 9:
            break
        print( "choose a valid option")
    return choice

def add_member(names, ranks, divs, ids):

    return
def remove_member(names, ranks, divs, ids):
    return
def update_rank(names, ranks, ids):
    return
def display_roster(names, ranks, divs, ids):
    return
def search_crew(names, ranks, divs, ids):
    return
def filter_by_division(names, divs):
    return
def calculate_payroll(ranks):
    return
def count_officers(ranks):
    return
main()