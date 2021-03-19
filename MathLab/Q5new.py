# A total of $10000 is distributed among 150 persons as gift. A gift is either of $50 or $100. Find the number of gifts of each type.
import random
total_set = [10000, 20000, 30000, 40000, 50000,80000,100000]
total = random.choice(total_set)

people_set = [150,200,250,300,400]
people = random.choice(people_set)

dist_set = [50, 100,150,200,500]
#
#x = int((total - v2*people)/(v1 - v2)) due to this expression 
# sometimes (v1-v2) was becoming negative 
# or 
# sometimes (total-v2*people) was becoming negative
# So I introduced while loop which will make sure (v1-v2) and (total-v2*people) stays positive all the time.
#
v1,v2=0,0
while(v1<=v2 or total<=v2*people or v1*people < total):
    v1,v2=random.choices(dist_set,k=2)
#print(v1,v2)

item_set = ['gift', 'prize', 'coupon']
item = random.choice(item_set)

#print(total, item, people, v1, v2)


print("A total of Rs", total, "is distributed among", people, "persons as", item+"s", ". A", item, "is either of Rs", v1, "or Rs", v2, ". Find the number of", item+"s", "of each type." )

def soln(total, item, people, v1, v2):
    print("\033[1m" + "Solution:" + "\033[0m")
    print('''Total number of''', item+"s", "=", people, '''
    Let the number of Rs''', v1, item,'''is x.
    Then the number of''', item+'s', '''is (''',people, '''- x )
    Amount spent on x''', item+'s', "of", v1, "=", str(v1)+'''x
    Amount spent on (''',people, '''- x )''', item+'s', '''of''', v2, "=", str(v2)+"(",people, '''- x )''')
    print("Total amount spent for", item+'s', "=", total, '''
    According to the question,''')
    print(str(v1)+"x +", str(v2)+"(",people, '''- x ) =''', total)
    print("=>", str(v1)+"x +", v2*people, "-", str(v2)+"x =", total)
    print(str(v1-v2)+'x =', total, '-', v2*people)
    print(str(v1-v2)+'x =', total - v2*people, '''
    x =''', total - v2*people,"/", str(v1-v2), '''
    x =''', int((total - v2*people)/(v1 - v2)))
    print(people,'- x = ', people, '-',x,'=', people-x)

x = int((total - v2*people)/(v1 - v2))

a = [x, people-x]
b = [x-10,people-x+14]
c = [x-10,people-x+10]
d = [x-5,people-x+5]

options = [a, b, c, d]
random.shuffle(options)
corr = options.index(a) + 1

print(' option 1 : '+str(options[0])+'\n option 2 : '+str(options[1])+'\n option 3 : '+str(options[2])+'\n option 4 : '+str(options[3])+'\n')
choice = int(input("Enter the option number "))

if choice == corr:
    print('Your answer is correct!')
   #soln(total, item, people, v1, v2)
elif choice in [1,2,3,4]:
    print('Your answer is incorrect!')
    print('The correct answer is option', corr)
    print('-------- SOLUTION----------')
    soln(total, item, people, v1, v2)
else:
    print("Invalid input")