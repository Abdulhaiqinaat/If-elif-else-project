'''Your parents pay you $3 for each trash bag full of leaves you rake. If you can fill more than 10
bags in a month, they give you a bonus of $20. Write a program that asks the user how many
bags of leaves they filled in the past month and prints out the total amount of money they made.
For example, if someone fills 8 bags in a month, they would get $24. But, if they fill 11 bags in a
month, they would get 11 x $3 + $20 = $53.
How many bags of leaves did you fill this month?
20
Great, you made $80.'''
user=int(input("How many bags of leaves you have filled in the past month= "))
pay=user*3
Bonus=user*3+20
if user>=10:
    print("Congratulation")
    print("You have filled more then 10 bags,you will get 20$ bonus=%d"%Bonus)
else:
    print("Sorry,you have filled less then 10 bags, you wont get 20$ bonus=%d"%pay)
