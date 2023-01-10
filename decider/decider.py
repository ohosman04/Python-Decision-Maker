import random
import operator
def create_list_of_options(number_of_options):
    options = []
    for i in range(number_of_options):
        option = input(f"Option {i+1}: ")
        options.append(option)
    return options
    

def random_vote(number_of_votes,list_of_options):
    tally = {}
    while number_of_votes != 0:
        random_vote = random.choice(list_of_options)
        if random_vote not in tally:
            tally[random_vote] = 1
        else:
            tally[random_vote] +=1
        number_of_votes-=1
    sorted_tally = dict(sorted(tally.items(), key=operator.itemgetter(1), reverse= True))
    return sorted_tally
def main():
    run = True
    print("Welcome to The Decider. We are here to solve your indecisiveness.")
    wow = 1
    while run:
        user_options = int(input("How indecisive are you? (How many options do you wanna choose from?): "))
        user_options = create_list_of_options(user_options)
        voters = int(input("How many voters do you want? "))
        print(random_vote(voters,user_options))
        while wow > 0:
            again = input("Would you like to go again? (y/n): ").lower()
            if again in ['y','n']:
                if again == 'y':
                    main()
                    run = False
                    wow = 0
                else:
                    print("Goodluck with whatever you chose :)")
                    run = False
                    wow = 0
            else:
                print("Invalid choice. Try again.")
if __name__ == "__main__":
    main()
                    


    

