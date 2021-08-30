# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")


#if practice 2
counties=["arapahoe", "denver", "jefferson"]
if counties[1]!='jefferson':
        print(counties[0])

#Taxing Apples
price=float(input("How much is the apple?"))
if price>=5:
    apple_taxed=0
    apple_taxed=price*1.08875
    print(f"Your apple is ${apple_taxed:.2f}. Thank you for shopping with us today.")
else:
    print(f"Your apple is ${price:.2f}. Thank you for shopping with us today.")

#AC or Windows?
temp=int(input("What is the temp outisde?"))
if temp>80:
    print('Turn on the AC')
else:
    print('Open the windows')


#Scoring System (long way)
score=int(input("What is the student's score?"))
if score>=90:
    print("Student's grade is A.")
else:
    if score>=80:
        print("Student's grade is B.")
    else:
        if score>=70:
            print("Student's grade is C.")
        else:
            if score>=60:
                print("Student's grade is D.")
            else:
                print("Student's grade is F.")


#Scoring System (short way)
score=int(input("What is the student's score?"))
if score>=90:
    print("Student's grade is A.")
elif score>=80:
    print("Student's grade is B.")
elif score>=70:
    print("Student's grade is C.")
elif score>=60:
     print("Student's grade is D.")
else:
    print("Student's grade is F.")


#Membership operators
counties=['arapahoe','denver','jefferson']
if 'arapahoe' in counties:
    print('true')
else:
    print('false')

counties=['arapahoe','denver','jefferson']
if 'el paso' not in counties:
    print('true')
else:
    print('false')

#el paso practice
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")


#Loop thru dict
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for voters in counties_dict.keys():
    print(voters)