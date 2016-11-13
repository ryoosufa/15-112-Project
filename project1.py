from os.path import *
import os
from Tkinter import *
from PIL import ImageTk, Image

class recipe:
    def __init__(self):
        global label
        self.window=Tk()
        self.btn=Button(self.window,text="save to your computer",command=self.saveRecipe)
        self.btn.grid(row=0,column=0)
        self.label=Label(self.window,text="Name")
        self.label.grid(row=1,column=0)
        self.label1=Label(self.window,text="Ingredients")
        self.label2=Label(self.window,text="Preparation Time")
        self.label3=Label(self.window,text="serves:")
        self.label4=Label(self.window,text="Instructions")
        self.cookit=Button(self.window,text="cook",command=self.cook)
        self.absent=Button(self.window,text="need to buy")
        self.label1.grid(row=2,column=0)
        self.label2.grid(row=3,column=0)
        self.label3.grid(row=4,column=0)
        self.label4.grid(row=5,column=0)
        self.cookit.grid(row=6,column=0)
        self.absent.grid(row=7,column=0)
        self.box=Text(self.window,height="1")
        self.box.grid(row=1,column=1)
        self.ingBox=Text(self.window,height="5")
        self.ingBox.grid(row=2,column=1)
        self.timeBox=Text(self.window,height="1")
        self.timeBox.grid(row=3,column=1)
        self.serves=Text(self.window,height="1")
        self.serves.grid(row=4,column=1)
        self.ins=Text(self.window,height="10")
        self.ins.grid(row=5,column=1)
        self.add=Button(self.window,text="add to cookbook",command=self.addRecipe)
        self.add.grid(row=8,column=0)
        



    
        
        
        
        self.window.mainloop()




    '''def saveTocb(self):'''
        



    def addRecipe(self):
        cwd = os.getcwd()
        print cwd
        
        name_recipe=self.box.get('0.0',END)
        
        if isfile(name_recipe.strip())==False:
            if isfile("names.txt"):
                f = open("names.txt")
                text = f.read()
                f.close()
            
        # open the file again for writing
                f = open("names.txt", 'w')
                f.write("//"+name_recipe)
        # write the original contents
                f.write(text)
                f.close()
            else:
                f = open("names.txt", 'w')
                f.write("//"+name_recipe)
                f.close()



        name_recipe=self.box.get('0.0',END)
        name_recipe=name_recipe.strip()
        
        #DownloadFile=open("recipe\\"+name_recipe+"protocol",'w')
        if exists(cwd+"\\recipes"):
            print cwd+"\\recipes"+name_recipe+"protocol"
            recipepath=join(cwd+"\\recipes",name_recipe+"protocol")
            #makedirs(cwd+"\\recipes")
            #print cwd+"\\recipes"+"\potat"
            print "entered if condition"
            DownloadFile=open(recipepath,'w')
    
    
        #DownloadFile=open(name_recipe+"protocol",'w')
        
        
            instructions=self.ins.get('0.0',END)
            people=self.serves.get('0.0',END)
            time=self.timeBox.get('0.0',END)
            ingredients=self.ingBox.get('0.0',END)
        
        # write to file
            strings=["@\n"+name_recipe+"\n#",
                     "\n@\n"+ingredients+"\n#",
                     "\n@\n"+instructions+"\n#",
                     "\n@\n"+people+"\n#",
                     "\n@\n"+time+"\n#"]
            for i in range(len(strings)):
                DownloadFile.write(strings[i])

        else:
            makedirs(cwd+"\\recipes")
            DownloadFile=open(recipepath,'w')
    
    
        #DownloadFile=open(name_recipe+"protocol",'w')
        
        
            instructions=self.ins.get('0.0',END)
            people=self.serves.get('0.0',END)
            time=self.timeBox.get('0.0',END)
            ingredients=self.ingBox.get('0.0',END)
        
        # write to file
            strings=["@\n"+name_recipe+"\n#",
                     "\n@\n"+ingredients+"\n#",
                     "\n@\n"+instructions+"\n#",
                     "\n@\n"+people+"\n#",
                     "\n@\n"+time+"\n#"]
            for i in range(len(strings)):
                DownloadFile.write(strings[i])




   
        


    def saveRecipe(self):
       

        name_recipe=self.box.get('0.0',END)
        name_recipe=name_recipe.strip()
        DownloadFile=open(name_recipe,'w')
        
        
        instructions=self.ins.get('0.0',END)
        people=self.serves.get('0.0',END)
        time=self.timeBox.get('0.0',END)
        ingredients=self.ingBox.get('0.0',END)
        strings=[name_recipe+"\n","Ingredients : "+"\n"+ingredients,"instructions : "+"\n"+instructions,"serves : "+"\n"+people,"prep time : "+"\n"+time]
        for i in range(len(strings)):
            DownloadFile.write(strings[i])




    def cook(self):
        wnd=Tk()
        ingredientList=self.ingBox.get('0.0',END)
        print ingredientList
        t=ingredientList.split("\n")
        '''for j in range(len(t)):
            t.strip()'''
        print t
        for i in range(len(t)):
            #print len(ingredientList), "this was the length"
            var=IntVar()
            if len(t[i])!=0:
                check=Checkbutton(wnd,text=t[i],variable=var).grid(row=i, sticky=W)

    def grocery():

        
        self.boxofitems=Text(self.window,height="20")
        
        
        

        




#w1=recipe()

#function to close the application
#called by "Quit" button on the first window


def cook():
        wind=Tk()
        ingsList=ingBox.get(0,END)
        print ingsList
        ingsList=list(ingsList)
        #t=ingsList.split()
        '''for j in range(len(t)):
            t.strip()'''
        
        for i in range(len(ingsList)):
            #print len(ingredientList), "this was the length"
            var=IntVar()
            if len(ingsList[i])!=0:
                check=Checkbutton(wind,text=ingsList[i],variable=var).grid(row=i, sticky=W)








def All_recipes():
    all_recipes=Tk()
    all_recipes.title("The Cookbook Club")
    labell_1=Label(all_recipes,text="All Recipes")
    labell_1.pack()
    recBox=Listbox(all_recipes,width="25",height="25")
    recBox.pack()
    butn=Button(all_recipes,text="open")
    butn.pack()
    butn2=Button(all_recipes,text="Add to Favourites List")
    butn2.pack()
    all_recipes.mainloop()

def del_fav():
    global favBox
    favbox.delete(ACTIVE)
    

def FavsWnd():
    favourites=Tk()
    favourites.title("Favvourite Recipes")
    label_1=Label(favourites,text="Favourites")
    label_1.pack()
    favBox=Listbox(favourites,width="25",height="25")
    favBox.pack()
    butn=Button(favourites,text="open")
    butn.pack()
    butnn=Button(favourites,text="delete from favourites", command=del_fav)
    butnn.pack()
    favourites.mainloop()

def openGrocery():
    global Box1
    show=Tk()
    show.title("My Grocery List")
    global ingBox
    label1=Label(show,text="Grocery List")
    label1.pack()
    Box1=Listbox(show,width="25",height="25")
    Box1.pack()
    show.mainloop()



def byebye():
    global root
    root.destroy()

def createRecipe():
    r=recipe()

def recipebox():
    global Box     
    openit=Tk()
    openit.title("My recipes")
    label1=Label(openit,text="Recipes")
    label1.pack()
    Box=Listbox(openit,width="30",height="25")
    Box.pack()
    
    '''Box2=Listbox(openit,width="30",height="25")
    Box2.grid(row=1,column=1)'''
    openBtn=Button(openit,text="Open",command=open_recipe)
    openBtn.pack()
    favsBtn=Button(openit,text="Add to Favourites")
    favsBtn.pack()
    delbtn=Button(openit,text="Delete recipe from the cookbook")
    delbtn.pack()
    
    
           
    if isfile("names.txt"):
        f = open("names.txt")
        text = f.read()
        f.close()
        text=text.replace("//","")
        #print text
        text=text.split("\n")
        for i in range(len(text)):
            Box.insert(END,text[i])

    openit.mainloop()
    
def go_shopping():
    global ingBox
    global Box1
    item=ingBox.get(ACTIVE)
    print item
    Box.insert(END,item)
    
    

def open_recipe():
    

    global Box
    global ingBox
    name=Box.get(ACTIVE)
    protocol_file=join(cwd+"\\recipes",name+"protocol")
    '''File=open(protocol_file)
    text=File.read()
    File.close()'''
    openwindow=Tk()
    btn=Button(openwindow,text="save to your computer")
    btn.grid(row=0,column=0)
    label=Label(openwindow,text="Name")
    label.grid(row=1,column=0)
    label1=Label(openwindow,text="Ingredients")
    label2=Label(openwindow,text="Preparation Time")
    label3=Label(openwindow,text="serves:")
    label4=Label(openwindow,text="Instructions")
    cookit=Button(openwindow,text="cook",command=cook)
    absent=Button(openwindow,text="need to buy", command=go_shopping)
    label1.grid(row=2,column=0)
    label2.grid(row=3,column=0)
    label3.grid(row=4,column=0)
    label4.grid(row=5,column=0)
    cookit.grid(row=6,column=0)
    absent.grid(row=7,column=0)
    box=Text(openwindow,height="1")
    
    ingBox=Listbox(openwindow,width="107",height="15")
    
    timeBox=Text(openwindow,height="1")
    
    serves=Text(openwindow,height="1")
    
    ins=Text(openwindow,height="10")
    
    
    listt=[]
    cn=""
    f=open(protocol_file).readlines()
    nodestart=False
    for i in range(len(f)):
        if "#" in f[i]:
            nodestart=False
            listt.append(cn)
            cn=""
        if nodestart:
            cn=cn+f[i]
        if "@" in f[i]:
            nodestart=True
    Name=listt[0]
    list_ingred=listt[1].split("\n")
    prepTime=listt[4]
    People=listt[3]
    Instructions=listt[2]
    for k in range(len(Name)):
    
        box.insert(END,Name[k])

    box.grid(row=1,column=1)

    for q in range(len(list_ingred)):
    
        ingBox.insert(END,list_ingred[q])

    ingBox.grid(row=2,column=1)

    for w in range(len(prepTime)):
    
        timeBox.insert(END,prepTime[w])
    timeBox.grid(row=3,column=1)

    for x in range(len(People)):
    
        serves.insert(END,People[x])

    serves.grid(row=4,column=1)

    for y in range(len(Instructions)):
    
        ins.insert(END,Instructions[y])

    ins.grid(row=5,column=1)


    
    openwindow.mainloop()
    #print text
    #print name+"protocol"



def openList():
    global showit
    openn=Tk()
    openn.title("Search Results")
    results=Label(openn,text="Found what you were looking for?")
    results.pack()
    lb=Listbox(openn)
    entered=showit.get(1.0,END)
    entered=entered.strip()
    print entered
    
    
    for filename in os.listdir(os.getcwd()+"\\recipes"):
        
        filename=filename.replace("protocol","")
        print filename
        print entered in filename
        if entered in filename:
            print "entered this if"
            lb.insert(END,filename)
    lb.pack()

    buttn=Button(openn,text="open")
    buttn.pack()
    favz=Button(openn,text="Add this to Favourites")
    favz.pack()
    delete=Button(openn,text="Delete From Cookbook")
    delete.pack()
    
    openn.mainloop()

def search_name():
    global showit
    openthis=Tk()
    openthis.title("Searching For Recipe")
    showit=Text(openthis,width="35",height="1")
    
    
    for filename in os.listdir(os.getcwd()+"\\recipes"):
        print filename
    showit.grid(row=0,column=1)
    labl=Label(openthis,text="Enter the name")
    labl.grid(row=0,column=0)
    find_btn=Button(openthis,text="Find",command=openList)
    find_btn.grid(row=0,column=2)
    openthis.mainloop()




def start():
    menu=Tk()
    button1=Button(menu,text="Add New Recipe",command=createRecipe)
    button1.grid(row=0,column=0)
    button2=Button(menu,text="Export Recipe")
    button2.grid(row=1,column=0)
    button3=Button(menu,text="My Recipes",command=recipebox)
    button3.grid(row=2,column=0)
    button4=Button(menu,text="Recently Viewed")
    button4.grid(row=3,column=0)
    button5=Button(menu,text="Favourites", command=FavsWnd)
    button5.grid(row=0,column=5)
    button6=Button(menu,text="Grocery List",command=openGrocery)
    button6.grid(row=0,column=2)
    button7=Button(menu,text="Hungry?")
    button7.grid(row=0,column=3)
    search=Label(menu,text="Search by:")
    search.grid(row=0,column=6)
    filter1=Button(menu,text="Recipe Name",command=search_name)
    filter1.grid(row=1,column=6)
    filter2=Button(menu,text="Ingredient")
    filter2.grid(row=2,column=6)
    filter3=Button(menu,text="User")
    filter3.grid(row=3,column=6)
    button8=Button(menu,text="Notifications")
    button8.grid(row=0,column=4)
    newsfeed=Label(menu,text="Newsfeed")
    newsfeed.grid(row=0,column=1)
    cookbook=Button(menu,text="Main Cookbook", command=All_recipes)
    cookbook.grid(row=1,column=4)
    Txt=Text(menu,height="20")
    Txt.grid(row=1,column=1)
    menu.mainloop()

showit=None
path = 'startup.jpg'
Box=None
ingBox=None
root = Tk()
root.title("My Digital CookBook")
help_btn=Button(root,text="About")
help_btn.pack()
btn=Button(root,text="Join the Cookbook Club",command=start)
btn.pack()
img = ImageTk.PhotoImage(Image.open(path))
panel =Label(root, image = img)
panel.pack(side="bottom", fill = "both", expand = "yes")
btn2=Button(root,text="Quit",command=byebye)
btn2.pack()
cwd = os.getcwd()
print cwd
'''if exists(cwd+"\\recipes"):
    #makedirs(cwd+"\\recipes")
    print cwd+"\\recipes"+"\potat"
    f=open(cwd+"\\recipes"+"\potat",'w')
    
    f.close()'''
    
root.mainloop()
