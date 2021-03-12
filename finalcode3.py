
import time
import pdb
from tkinter import *  
from PIL import ImageTk,Image

items={}
primograms=100

def home(items,primograms):
    # pdb.set_trace()
    home_file=open("Home_description.txt", "r")#Might add kitchen later
    print(home_file.read())
    time.sleep(2) 
    root = Tk()  
    canvas = Canvas(root, width = 1000, height = 968)  
    canvas.pack()  
    img = ImageTk.PhotoImage(Image.open("home.jpg"))  
    canvas.create_image(20, 20, anchor=NW, image=img) 
    root.mainloop()
    home_file.close()
    time.sleep(3)
    village_file=open("Village_description.txt", "r")
    print(village_file.read())
    time.sleep(4)
    village_file.close()
    time.sleep(4)
    village(items,primograms)

def home_branch(items,primograms):

    choice=input("Would you like to go to the village once again to buy bread or the forest to move ahead in your journey?")
    quit(choice)
    if(choice=="village" or choice=="Village" or choice=="V" or choice=="v"):
        if primograms<20:
            print("You don't have enough primograms. Let's go to the forest")
            forest(items,primograms)
        else: 
            village(items,primograms)
    elif(choice=="forest" or choice=="Forest" or choice=="F" or choice=="f"):
        
        if('Bread' in items.keys()):
            time.sleep(2)
            forest(items,primograms)    
        else:
            print("Why don't we buy some bread for Grandma?")
            village(items,primograms)
    else:
        print("Please check for any spelling errors in input! ")
        home_branch(items,primograms)

  
def village(items,primograms):
    time.sleep(2)
    root = Tk()  
    canvas = Canvas(root, width = 900, height = 680)  
    canvas.pack()  
    img = ImageTk.PhotoImage(Image.open("village.jpg"))  
    canvas.create_image(20, 20, anchor=NW, image=img) 
    root.mainloop()

    
    
    def choice(items,primograms):
        root = Tk()  
        canvas = Canvas(root, width = 480, height = 360)  
        canvas.pack()  
        img = ImageTk.PhotoImage(Image.open("bread.jpg"))  
        canvas.create_image(20, 20, anchor=NW, image=img) 
        root.mainloop()
        food=input("Would you like to buy some bread?(Y/n)\n")
        quit(food)
        time.sleep(.5)
        
        if(food=='y' or food=='Yes' or food=='Y'):
            confirmation=input(f"You currently have {primograms} primograms. One loaf of bread will cost you 20 primograms are you sure?(y/n)")
            quit(confirmation)
            if(confirmation=='y' or confirmation=='Yes' or confirmation=='Y'):
                quantity=int(input("Please enter the quantity of bread you would like to buy: "))
                quit(quantity)
                if(quantity*20>primograms):
                    print("Not enough primograms..Let's just return home for now..")
                    home(items,primograms)
                else:
                    primograms-=(quantity*20)
                    if 'Bread' not in items.keys():
                        items['Bread']=quantity
                    else:
                        items['Bread']=items['Bread']+quantity
                    print("The number of primograms availble now are: ", primograms)
                    print("The items in your inventory are: ", items)
                    time.sleep(1)
                    print("Since we have bought all the needed ingredients, let's go ahead in our journey!")
                    home_branch(items,primograms)


            elif(confirmation=='n' or confirmation=='No' or confirmation=='N'):
                path=input("Would you like to stay in the village or go back to our house? ")
                quit(path)
                if(path=='village' or path=='Village' or path=='v' or path=='V'):
                    village(items,primograms)
                elif(path=='house' or path=='home' or path=='H' or path=='h'):
                    home(items,primograms)
                else:
                    print("Since you are not sure, let's go back home for the time being...")
                    home(items,primograms)
            else:
                print("Please enter a valid input..")
                choice(items,primograms)
        elif(food=='n' or food=='No' or food=='N'):
            print("Guess there's nothing to do here....Let's go back home...")
            time.sleep(1)
            home(items,primograms)
        
        else:
            print("Please enter a valid input..")
            choice(items,primograms)
        return primograms
    choice(items,primograms)

    return primograms

def forest(items,primograms):
    forest_file=open("Forest_description.txt", "r")
    print(forest_file.read())
    time.sleep(1)
    root = Tk()  
    canvas = Canvas(root, width = 400, height = 251)  
    canvas.pack()  
    img = ImageTk.PhotoImage(Image.open("forest.jpg"))  
    canvas.create_image(20, 20, anchor=NW, image=img) 
    root.mainloop()
    time.sleep(2)
    forest_file.close()
    def goldilocks(items,primograms):
        gold=open("gold.txt","r")
        print(gold.read())
        time.sleep(3)
        root = Tk()  
        canvas = Canvas(root, width = 1080, height = 608)  
        canvas.pack()  
        img = ImageTk.PhotoImage(Image.open("goldilocks.jpg"))  
        canvas.create_image(20, 20, anchor=NW, image=img) 
        root.mainloop()
        gold.close()
        help=input("Would you like to help goldilocks? (y/n): ")
        quit(help)
        

        if(help=='y' or help=='Yes' or help=='Y' or help=="yes"):
            count=0
            for key,value in items.items():
                count=items.get("Bread")
            if(count>1):
                print("Looks like you have more than one slice of bread!")
                print("Let's offer some to console the baby bear!\n *offers bread to baby bear* ")
                time.sleep(1)
                print("For helping the bear family you recieve 40 primograms and a silver knife as a reward!")
                primograms+=40
                items['Silver Knife']=1
                print("You currently have {} primograms.".format(primograms))
                print(items)
                time.sleep(.5)
                print("Let's keep moving! No time to waste!")
                time.sleep(5)
                kalsProbs(items, primograms)
            else:
                print("You grab goldilocks hand and quickly run away from clsthe bears....")
                print("You get 20 primograms and a silver knife for helping goldilocks")
                primograms+=20
                items['Silver Knife']=1
                print("You currently have {} primograms.".format(primograms))
                print("The items in your inventory are," , items)
                kalsProbs(items, primograms)
        elif(help=='n' or help=='No' or help=='N' or help=="no"):
            print("Guess there's nothing to do here...Let's move on..")
            kalsProbs(items, primograms)
        else:
            print("invalid input")
            goldilocks(items,primograms)
        return primograms
    goldilocks(items,primograms)
    return primograms


def kalsProbs(items, primograms):
    
    kalsProbs_file=open("kalsProbs_description.txt", "r")
    print(kalsProbs_file.read())  
    time.sleep(5)  
    root = Tk()  
    canvas = Canvas(root, width = 600, height = 600)  
    canvas.pack()  
    img = ImageTk.PhotoImage(Image.open("kal.jpg"))  
    canvas.create_image(20, 20, anchor=NW, image=img) 
    root.mainloop()
    time.sleep(2)

    kalsProbs_file.close()
    choice=input("Would you like to help Kalyani? (y/n): ")
    quit(choice)
    if(choice=='y' or choice == 'Yes' or choice == 'Y' or choice == 'yes'):
        print("prnt('hello world')")
        print("n=iput('Enter your correct age')")
        err= input("What kind of error do you think it is? \n a. Indentation error b. Syntax Error c. Semantic Error d.Spelling mistake\n")
        if(err=='d' or err=='d.' or err=='D' or err=='D.' or err=='Spelling mistake' or err=='Spelling Mistake' or err=='Spelling' or err=='Mistake'):
            print("Ohh the code works now !! Thank you so much!!")
            time.sleep(2)
            root = Tk()  
            canvas = Canvas(root, width = 800, height = 800)  
            canvas.pack()  
            img = ImageTk.PhotoImage(Image.open("kal_happy.jpg"))  
            canvas.create_image(20, 20, anchor=NW, image=img) 
            root.mainloop()
            time.sleep(2)

            print("You earn 10 primograms for helping Kalyani.  ")
            primograms+=10
            print("You currently have {} primograms.".format(primograms))
            print("Looks like Kalyani gave you a shotgun as thanks! Items has been added to inventory. ")
            items['Shotgun']=1
            print(items)
            time.sleep(.5)
            print("Now let's hurry to grandma's place")
            time.sleep(2)
            grannyAbode(items, primograms)
            
        else:
            print("Look's like you've got the wrong answer..")
            time.sleep(.5)
            print("Oh, well..let's move on..Granny is still waiting for you.")
            time.sleep(.5)
            print("Legend says that Kalyani is still trying to solve the code to this day...")
            time.sleep(1)
            print("Now let's hurry to grandma's place")
            time.sleep(2)
            grannyAbode(items, primograms)
            
    else:
        print("You try to leave but Kalyani follows behind, still pestering you to help her with the code..")
        primograms-=10
        print("You decide to help her in the end...")
        time.sleep(1)
        print("Put some random code with a problem here")
        err= input("What kind of error do you think it is? \n a. Indentation error b. Syntax Error c. Semantic Error d.Spelling mistake\n")
        quit(err)
        if(err=='d' or err=='d.' or err=='D' or err=='D.' or err=='Spelling mistake' or err=='Spelling Mistake' or err=='Spelling' or err=='Mistake'):
            print("Ohh the code works now !! Thank you so much!!")
            time.sleep(2)
            root = Tk()  
            canvas = Canvas(root, width = 800, height = 800)  
            canvas.pack()  
            img = ImageTk.PhotoImage(Image.open("kal_happy.jpg"))  
            canvas.create_image(20, 20, anchor=NW, image=img) 
            root.mainloop()
            time.sleep(5)
            print("You earn 10 primograms for helping Kalyani.  ")
            primograms+=10
            print("You currently have {} primograms.".format(primograms))
            time.sleep(.5)
            print("Now let's hurry to grandma's place")
            time.sleep(2)
            grannyAbode(items, primograms)
            
        else:
            print("Look's like you've got the wrong answer..")
            time.sleep(.5)
            print("Oh, well..let's move on..Granny is still waiting for you.")
            time.sleep(.5)
            print("Legend says that Kalyani is still trying to solve the code to this day...")
            time.sleep(1)
            print("Now let's hurry to grandma's place")
            time.sleep(2)
            grannyAbode(items, primograms)

def grannyAbode(items, primograms):    
    grannyAbode_file=open("grannyAbode_file.txt", "r")
    print(grannyAbode_file.read())
    time.sleep(2)
    root = Tk()  
    canvas = Canvas(root, width = 800, height = 400)  
    canvas.pack()  
    img = ImageTk.PhotoImage(Image.open("granny_abode.jpg"))  
    canvas.create_image(20, 20, anchor=NW, image=img) 
    root.mainloop()
    if('Shotgun' not in items.keys()):
        
        if("Silver Knife" in items.keys()):
            print("You find Granny hidden in the corner of the house")
            time.sleep(.5)
            print("You suddenly remember the Silver KNife you had been given by Goldilocks.")
            time.sleep(.5)
            print("You realize that you can use it against the wolf to escape.")
            time.sleep(.5)
            print("That's when you realize that between you and your granny,")
            print("one of you have to sacrifice their life to get close enough to stab the wolf")
            print("Granny convinces you that at her stage of life, she is will to die if it means saving you.")
            time.sleep(2)
            print("You watch with a heavy heart as the wolf kills your granny, but not before she stabs it's heart.")
            time.sleep(.5)
            root = Tk()  
            canvas = Canvas(root, width = 320, height = 180)  
            canvas.pack()  
            img = ImageTk.PhotoImage(Image.open("granny_dead.jpg"))  
            canvas.create_image(20, 20, anchor=NW, image=img) 
            root.mainloop()
            time.sleep(.5)
            print("Still afraid, you run away from the house and from the forest, tears flowing as you remember your granny.")
            time.sleep(2)
            root = Tk()  
            canvas = Canvas(root, width = 612, height = 612)  
            canvas.pack()  
            img1 = ImageTk.PhotoImage(Image.open("girl_run.jpg"))  
            canvas.create_image(20, 20, anchor=NW, image=img1)
            root.mainloop()
            time.sleep(2)
            print("You lead the rest of your life always remember the hero you Granny had been and the big bad wolf which had killed her.")
            time.sleep(1)
            print("Normal End")
            time.sleep(.5)
            print("Game Over...You can do better next time")
            items['Primograms']=primograms
            print("The Items in your inventory are: \n")
            for keys,values in items.items():
                print(keys+ " ...... " , values)
            time.sleep(5)

        else:
            print("You turn around to run so that you can search for help.")
            time.sleep(.5)
            print("But the wolf was faster and quickly blocks your path.")
            time.sleep(.5)
            print("Soon both you and Granny are devoured by the wolf.")
            time.sleep(1)
            root = Tk()  
            canvas = Canvas(root, width = 320, height = 180)  
            canvas.pack()  
            img = ImageTk.PhotoImage(Image.open("granny_dead.jpg"))  
            canvas.create_image(20, 20, anchor=NW, image=img) 
            root.mainloop()
            time.sleep(.5)
            print("Both granny and you die")
            time.sleep(1)
            print("Bad End")
            time.sleep(.5)
            print("Game Over....Try again next time")
            items['Primograms']=primograms
            print("The Items in your inventory are: \n")
            for keys,values in items.items():
                print(keys+ " ...... " , values)
            time.sleep(5)
        
    elif('Shotgun' in items.keys()):
        if("Silver Knife" in items.keys()):
            print("You quickly grab Granny’s hand and start running with the wolf hot at your heels.")
            time.sleep(.5)
            print("You suddenly remember the shot gun Kalyani had given you for helping with her code.")
            time.sleep(.5)
            print("You stop running and hold your grandma close to you as you aim at the running wolf and fire.")
            time.sleep(.5)
            print("But your victory is short lived when you realize that the wolf is still alive but has been severly wounded.")
            time.sleep(.5)
            print("Then with the silver knife which Goldilocks had given to you, you walk close enough to the wolf to kill it.")
            time.sleep(.5)
            print("Since it was shot, it could barely put up any fight and you managed to kill it by stabbing its heart.")
            time.sleep(.5)
            print("You and Granny are very happy at having managed to kill the big bad wolf")
            root = Tk()
            canvas = Canvas(root, width = 800, height = 800)  
            canvas.pack()  
            img1 = ImageTk.PhotoImage(Image.open("wolfdead.png"))  
            canvas.create_image(20, 20, anchor=NW, image=img1) 
            root.mainloop()
            time.sleep(2)
            root = Tk()
            canvas = Canvas(root, width = 800, height = 800)  
            canvas.pack()  
            img1 = ImageTk.PhotoImage(Image.open("granny_alive.jpg"))  
            canvas.create_image(20, 20, anchor=NW, image=img1) 
            root.mainloop()
            time.sleep(2)
            root=Tk()
            canvas = Canvas(root, width = 756, height = 1080)  
            canvas.pack()   
            img = ImageTk.PhotoImage(Image.open("girl_happy.jpg"))  
            canvas.create_image(20, 20, anchor=NW, image=img) 
            root.mainloop()
            time.sleep(2)
            print("That evening Granny and you eat the bread you had bought in the village earlier that day.")
        
            time.sleep(2)
            print("It had been a long day of adventure but all is well that ends well.")
            time.sleep(1)
            print("Perfect End")
            time.sleep(.5)
            print("You have won the game!!")
            items['Primograms']=primograms
            print("The Items in your inventory are: \n")
            for keys,values in items.items():
                print(keys+ " ...... " , values)
            time.sleep(5)
        else:
            print("You quickly grab Granny’s hand and start running with the wolf hot at your heels.")
            time.sleep(.5)
            print("You suddenly remember the shot gun Kalyani had given you for helping with her code.")
            time.sleep(.5)
            print("You stop running and hold your grandma close to you as you aim at the running wolf and fire.")
            time.sleep(.5)
            print("But your victory is short lived when you realize that the wolf is still alive but has been severly wounded.")
            time.sleep(.5)
            print("You and Granny run long and far till the village until you are sure that the wounded wolf is no longer chasing you.")
            time.sleep(.5)
            print("You and Granny are very happy for having escaed the big bad wolf and decide to stay in your house with Granny forever.")
            time.sleep(.5)
            root=Tk()
            canvas = Canvas(root, width = 800, height = 802)  
            canvas.pack()  
            img1 = ImageTk.PhotoImage(Image.open("granny_alive.jpg"))  
            canvas.create_image(20, 20, anchor=NW, image=img1)
            root.mainloop()
            time.sleep(2)
            root=Tk()
            canvas = Canvas(root, width = 756, height = 1080)  
            canvas.pack()  
            img2= ImageTk.PhotoImage(Image.open("girl_happy.jpg"))  
            canvas.create_image(20, 20, anchor=NW, image=img2) 
            root.mainloop()
            print("But deep down, you both are always afraid that it might return one day to kill you both....")
    
            time.sleep(2)
            print("Good End")
            time.sleep(.5)
            print("Game Over...You can do even better.")
            time.sleep(.5)
            items['Primograms']=primograms
            print("The Items in your inventory are: \n")
            for keys,values in items.items():
                print(keys+ " ...... " , values)
            time.sleep(5)

def quit(answer):
    if(answer=="quit" or answer=="exit" or answer=="Quit" or answer=="Exit"):
        exit()
    else:
        pass
        
home(items,primograms)
'''
f = open("kalsProbs_description.txt", "a")
f.write("You again start heading towards Granny’s house, when you see an AMAZING, BEAUTIFUL and DOWNRIGHT MESMERISING black haired girl, ")
f.write("who was sitting in the forest with a computer and seemed to be emitting a very frustrated aura. " )
f.write("She spots you as you walking by and runs over to you and says- ")
f.write("“Hey, I’ve been struggling with this god-forsaken code for god knows how long.")
f.write("I beg you!!! Pls for the love of god HELP MEEEEE”.")
f.close()
'''
