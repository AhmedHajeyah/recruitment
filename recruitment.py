def get_skills():
    # Add at least 3 random skills for the user to select from
    return ["Python", "Java", "C++"]



def show_skills(skills):
    # Pretty print skills to the user
    # Write your code here
    print("Available skills:")
    for i, element in enumerate(get_skills()):
        print("{}) {}".format(i + 1, element))

"""
print()
print("Skills:")
for index, skill in enumerate(skills, start=1):
print(f" {index}. {skill}")
print()
"""
    


def get_user_skills(skills):
    # Show the available skills and have user pick from them
    # Write your code here
    skills_list=[]
    skills=show_skills(skills)
    i = input("Choose a skill from above by entering its number: ")
    i2 = input("Choose another skill from above by entering its number: ")
    try:
        if 0 < int(i) <= len(skills):
            return int(i) - 1
    except:
        pass
    skills_list.append(get_skills()[int(i) - 1])
    try:
        if 0 < int(i2) <= len(skills):
            return int(i2) - 1
    except:
        pass
    skills_list.append(get_skills()[int(i2) - 1])
#    print(skills_list)
    return skills_list

#get_user_skills(get_skills())


def get_user_cv(skills):
    # Get the users CV from their inputs
    # Write your code here
#    cv = ({"name":"","age":"","yearexp":"","skills":""})
    return ({"name":input("What's your name? "),"age":int(input("How old are you? ")),"yearexp":int(input("How many years of experience do you have? ")),"skills":get_user_skills(skills)})
#    get_user_skills(skills)
#    print(cv)
#    return cv
#get_user_cv(get_skills())


def check_acceptance(cv, desired_skill):
    # Check if the cv is acceptable or not and return a boolean based on that
    # Write your code here
    return (cv["age"]) >= 18 and (cv["age"]) <= 40 and cv["yearexp"] > 3 and desired_skill in cv["skills"]
#        return True
#        print("Congratulations, you have been accepted!")
#    else:
#        return False
#    print("Sorry, you have not been accepted.")



def main():
    # Write your main logic here by combining the functions above into the
    # desired outcome
#    skills=get_skills()
    print("Welcome to the special recruitment program, please answer the following questions:")
    cv = get_user_cv(get_skills())
    if check_acceptance(cv, 'Python'):
#    if decision:
        print("Congratulations, you have been accepted! "+cv["name"])
    else:
        print("Sorry, you have not been accepted.")

if __name__ == "__main__":
    main()