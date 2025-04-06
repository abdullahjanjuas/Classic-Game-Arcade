def start_game():
    print("<<<<<<<<<<<<<<<< WELCOME TO LOVE CALCULATOR>>>>>>>>>>>>>>>>>>")
    name_1 = input("\nEnter your name:")
    name_2 = input("Enter your crush's name:")
    l_name_1 = name_1.lower()
    l_name_2 = name_2.lower()

    #Adding both names to find total no of letters from true love
    name_1_2 = l_name_1 + l_name_2

    #Counting true in both names and adding 
    t_count=name_1_2.count("t")
    r_count=name_1_2.count("r")
    u_count=name_1_2.count("u")
    e_count=name_1_2.count("e")
    true_count = t_count + r_count + u_count + e_count

    #Counting love in both names and adding
    l_count=name_1_2.count("l")
    o_count=name_1_2.count("o")
    v_count=name_1_2.count("v")
    e_count=name_1_2.count("e")
    love_count = l_count + o_count + v_count + e_count

    #Adding true love letters count from both names
    love_score = str(true_count) + str(love_count)

    #Converting to int to check conditions 
    int_love_score = int(love_score)

    #Dispaying love score
    print(f"Your love score is: {love_score}%")

    #Based on love score,providing comments

    if int_love_score < 10 or int_love_score > 90:
        print("\nYou both go ike coke and mentos!")

    elif int_love_score >= 40 and int_love_score <= 50:
        print("You are alright together.")
        