
def main():
    n, r, d, i = init_database()
    while True:

        choice = display_menu()
        if choice == 1:
            n,r,d,i = add_member(n,r,d,i)
        elif choice == 2:
            n,r,d,i = remove_member(n,r,d,i)
        elif choice == 3:
            n, r, i = update_rank(n,r,i)
        elif choice == 4:
            display_roster(n,r,d,i)
        elif choice == 5:
            search_crew(n,r,d,i)
        elif choice == 6:
            filter_by_division(n,d)
        elif choice == 7:
            calculate_payroll(r)
        elif choice == 8:
            count_officers(r)
        repeat = input("Back to menu? (y/n) ")
        if repeat == "n":
            print ("System shutting down")
            break
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
        user_choice = int(input(""))
        if user_choice > 0 and user_choice < 9:
            break
        print("choose a valid option ")
    return user_choice

def add_member(names, ranks, divs, ids):
    id_check = False
    rank_check = False
    new_name = input("What is new member's name ")
    new_div = input("please input the new member's division ")
    while True:
        new_id = input("please input the new member's ID ")
        for q in range(len(ids)):
            if new_id == ids[q]:
                print("Please pick a unique ID ")
                id_check = True
        if id_check == False:
            break
    while True:
        new_rank = input("Please input the New member's rank (Case sensitive)")
        if new_rank == "Cadet" or new_rank == "Ensign" or new_rank == "Lieutenant" or new_rank == "Commander" or new_rank == "Captain" or new_rank == "Rear Admiral" or new_rank == "Vice Admiral" or new_rank == "Admiral" or new_rank == "Fleet Admiral":
            rank_check = True
        else: 
            print("invalid rank")
        if rank_check == True:
            break
        names.append(new_name)
        ranks.append(new_rank)
        divs.append(new_div)
        ids.append(new_id)
    return new_name, new_rank, new_div, new_id


def remove_member(names, ranks, division, ids):
    id_remover = input("Please input the Id of the member you wish to remove ")
    x = ids.index(id_remover) 
    names.pop(x)
    ranks.pop(x)
    division.pop(x)
    ids.pop(x)
    return names, ranks, division, ids

def update_rank(names, ranks, ids):
    rank_valid = False
    id = input("Please input a members ID to update their rank ")
    y = ids.index(id)
    while True:
        new_rank = input("Please input the member's updated rank")
        if new_rank == "Cadet" or new_rank == "Ensign" or new_rank == "Lieutenant" or new_rank == "Commander" or new_rank == "Captain" or new_rank == "Rear Admiral" or new_rank == "Vice Admiral" or new_rank == "Admiral" or new_rank == "Fleet Admiral":
            rank_valid == True
        if rank_valid == True:
            break
        else:
            print ("invalid rank, please re-input")
    ranks[y] = new_rank
    return names, ranks, ids

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