import itertools,pyautogui,time
bn = open("boyname.txt", "r")
gn = open("girlname.txt", "r")
sn = open('sirname.txt', "r")
rn = open('random.txt','w')
for n in sn :
    for b in bn :
        c=b.strip() +" "+n.strip()
        print(c)
      
      