from os.path import *
import os
from Tkinter import *
from PIL import ImageTk, Image

# class defined in order to make a new recipe each time the user wants
# to add a recipe
class recipe:
    def __init__(self):
        # below is the gui for this recipe which has
        # the same attributes,because it belongs
        # to the same class
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
        # the gui above contains buttons,labels,textboxes,etc



   
        


    # some functions are defined for this specific class
    # in order to perform tasks related to each recipe
    # addRecipe is a function which saves a specific
    # protocol i've designed for each recipe to
    # a specific folder called "recipes" in the directory
    # where this application is run
    # it saves each time the user clicks the button "add to cookbook"
    # the reason for this protocol is to store the recipes
    # the user adds in a form which is readable using file IO's
    # this prevents the user from loosing all the recipes added once
    # the application is closed
    # and each time the app is run the recipes are read and shown
    def addRecipe(self):
        cwd = os.getcwd()
        name_recipe=self.box.get('0.0',END)

        # the names of all the recipes are also saved using this function
        # with a protocol, in this case it is "\\" before each new name
        # begins, so that we have all the names in a file called "names.txt"
        # so if the recipe is not already there, the below if condition
        # is entered,and the name is added
        if isfile(name_recipe.strip())==False:
            if isfile("names.txt"):
                f = open("names.txt")
                text = f.read()
                f.close()
            
        # open the file again for writing
        # for not loosing the names of different recipes
        # already present they are saved in "text"-a variable
                f = open("names.txt", 'w')
                f.write("//"+name_recipe)
        # write the original contents
                f.write(text)
                f.close()
            else:
        # if the file names.txt does not exist
        # for example when running the app for
        # the first time then this file is
        # created automatically
                f = open("names.txt", 'w')
                f.write("//"+name_recipe)
                f.close()


        # getting the name of the recipe entered by the user
        name_recipe=self.box.get('0.0',END)
        name_recipe=name_recipe.strip()
        
        # cwd has the path of the current directory
        # now looks inside folder  "recipes" in this path
        if exists(cwd+"\\recipes"):
           
            recipepath=join(cwd+"\\recipes",name_recipe+"protocol")
            # for each new recipe the protocol is stored with
            # the name "your recipeprotocol",
            # for example if the name is "Pasta" it will
            # be called :Pastaprotocol"
           
            
            # this new file is opened to write   
            DownloadFile=open(recipepath,'w')
    
    
        
        
            # the following are parts of the recipe and
            # all are  obtained by .get() function
            # as these are added by the user
            instructions=self.ins.get('0.0',END)
            people=self.serves.get('0.0',END)
            time=self.timeBox.get('0.0',END)
            ingredients=self.ingBox.get('0.0',END)
        
        # write to file with the following protocol
        # each of name, ingredients, etc are started with
        # an "@" and a newline character end with a
        # newline character then a "#"
            strings=["@\n"+name_recipe+"\n#",
                     "\n@\n"+ingredients+"\n#",
                     "\n@\n"+instructions+"\n#",
                     "\n@\n"+people+"\n#",
                     "\n@\n"+time+"\n#"]
        # the above list has the protocol
        # to be written to the file created
            for i in range(len(strings)):
                DownloadFile.write(strings[i])

        else:
            # in case you run the app for the first time
            # it makes a folder "recipes" in the current
            # directory and the rest of the procedure is
            # the same as explained above
            makedirs(cwd+"\\recipes")
            DownloadFile=open(recipepath,'w')
    
    
        
        
        
            instructions=self.ins.get('0.0',END)
            people=self.serves.get('0.0',END)
            time=self.timeBox.get('0.0',END)
            ingredients=self.ingBox.get('0.0',END)
        
        # writes to file
            strings=["@\n"+name_recipe+"\n#",
                     "\n@\n"+ingredients+"\n#",
                     "\n@\n"+instructions+"\n#",
                     "\n@\n"+people+"\n#",
                     "\n@\n"+time+"\n#"]
            for i in range(len(strings)):
                DownloadFile.write(strings[i])




   
        

    # this function is for the user to be able
    # to access recipes that they saved to their computer
    # even when the app is not running
    # this function is called when the user
    # clicks the "save to computer" button
    # this button is also part of the basic
    # gui of any instance of the class recipe
    # that is any new recipe created when
    # a button in the maincode which reads "Add new recipe"
    # is pressed
    # so instead of the protocol this
    # saves the same recipe in a form that
    # is easy to read and user-friendly
    def saveRecipe(self):
       
        # this function can be called from the same window where the function
        #  called by "add to computer" button is called
        # however this doesn't really make a difference
        # because saving recipes you really want to is optional and a
        # user may only save a few of them  instead of all
        # below the .get() function is being used because all
        # the data that is to be written to the file is entered by the user
        name_recipe=self.box.get('0.0',END)
        name_recipe=name_recipe.strip()
        DownloadFile=open(name_recipe,'w')
        
        
        instructions=self.ins.get('0.0',END)
        people=self.serves.get('0.0',END)
        time=self.timeBox.get('0.0',END)
        ingredients=self.ingBox.get('0.0',END)

        # this list in which the data is stored follows a specific
        # format to make the recipe saved user-friendly and organized
        # so the user can anytime read the document
        strings=[name_recipe+"\n","Ingredients : "+"\n"+ingredients,"instructions : "+"\n"+instructions,"serves : "+"\n"+people,"prep time : "+"\n"+time]
        for i in range(len(strings)):
            DownloadFile.write(strings[i])



    # this function is called if the user, while adding a recipe wants to
    # start cooking and for someone who has no one to help
    # it may be difficult to remember which ingredient was added
    # and the person might forget to add something
    # so this displays the ingredients in a way
    # you can tick as you add
    def cook(self):
        wnd=Tk()
        # it opens a window separately with all the ingredients it gets from
        # the .get() function
        # and displays them as buttons which look
        # like labels with tickboxes beside them
        ingredientList=self.ingBox.get('0.0',END)
        
        t=ingredientList.split("\n")
        # t stores the names of each ingredients as a list of strings
        
        # for loop adds each ingredient from t
        # as a button to the window and displays it
        #with a tickbox
        for i in range(len(t)):
            
            var=IntVar()
            if len(t[i])!=0:
                check=Checkbutton(wnd,text=t[i],variable=var).grid(row=i, sticky=W)

    
        
        
        
        

        






# this is very similar to the function described inside the recicpe
# class above, but it is defined outside as
# it  is called by other buttons which are in different windows
# these windows have almost the same layout as any recipe from the class
# recipe,but these are opened when clicked from inside a listbox
def cook():
        wind=Tk()
        ingsList=ingBox.get(0,END)
        
        ingsList=list(ingsList)
        
        
        for i in range(len(ingsList)):
            
            var=IntVar()
            if len(ingsList[i])!=0:
                check=Checkbutton(wind,text=ingsList[i],variable=var).grid(row=i, sticky=W)







# this function works the same way that the function
# recipebox works except that this shows a list
# of all the recipes and not only
# the ones entered particularly by this user
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

# this function is called when the button
# from the favourites window is pressed to
# delete from favourites
# this function is used to remove a particular recipe
# from favorites but not from the cookbook itself
def del_fav():
    # favBox is the listbox which displays
    # the names of recipes added by the user
    # to favourites and .delete(ACTIVE) only removes this
    # name from this listbox
    # ACTIVE means the only one  that has been selected by the user
    global favBox
    favbox.delete(ACTIVE)
    


# this function opens the window
# which has a listbox with the names of recipes
# that were added to favourites
# it is called when the button from the main menu called
# "Favourites" is pressed
def FavsWnd():
    # it opens the window with the following gui
    # witht buttons to open the recipe when the name of that
    # recipe is selected and "open" button is clicked
    # and another button for removing a recipe from Favourites
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


# this is similar to the above described function
# called FavsWnd, and opens a window with a listbox containing all the items
# which were added from the ingredients when the "need to buy" button was clicked
# this button appears on the window which opens when a recipe is opened(not when the user
# adds/creates a new recipe)
def openGrocery():
    global listItems
    global Box1
    show=Tk()
    show.title("My Grocery List")
    global ingBox
    label1=Label(show,text="Grocery List")
    label1.pack()
    Box1=Listbox(show,width="25",height="25")
    # if the "groocery list" button has not yet been pressed but the app is running
    # then the listbox for grocery items will be none existent
    # so the following if will be true andd whatever is added to the grocery items by
    # the user will be appended to a list which was empty initially
    # and from this list to the listbox in the grocery list window
    if listItems!=None and (len(listItems))!=0:
        for i in range (len(listItems)):
            Box1.insert(END,listItems[i])


    Box1.pack()
    show.mainloop()


# function to close the application
# called by "Quit" button on the first window
def byebye():
    global root
    root.destroy()

# called when a new recipe is to be added
# create recipe creates the instance of recipe class
# which means it creates the basic layout common
# to each recipe
# can be called as many times as the button
# from the main menu page is clicked and
# for as many recipes as the user wants to add
def createRecipe():
    r=recipe()


# this function is called when the "My Recipes" button is pressed
# from the main menu
# it has a listbox which has all the recipes which have
# been added by this user running the app up until now
def recipebox():
    global Box     
    openit=Tk()
    openit.title("My recipes")
    label1=Label(openit,text="Recipes")
    label1.pack()
    Box=Listbox(openit,width="30",height="25")
    Box.pack()
    
    
    openBtn=Button(openit,text="Open",command=open_recipe)
    openBtn.pack()
    favsBtn=Button(openit,text="Add to Favourites")
    favsBtn.pack()
    delbtn=Button(openit,text="Delete recipe from the cookbook")
    delbtn.pack()
    
    # the names of these recipes were stored in the file called "names.txt"
    # so if the name is there it always starts with a "//" as an indication
    # that this is the name of a different recipe
    # to add these names to the listbox the "//" is to be removed
    # using the .replace() function
    
           
    if isfile("names.txt"):
        f = open("names.txt")
        text = f.read()
        f.close()
        text=text.replace("//","")
        
        text=text.split("\n")
        # the names were the stored in a variable called "text" as it contains
        # everything read from names.txt
        # the .read() returns a string of all the data in names.txt and after
        # removing the "//" this string is converted to a list with each name as
        # an element because the \n was not removed when the // were removed
        # and these indicate that a different recipe's name is being read
        # the for loop goes over the list of names and adds them to the
        # my recipes listbox
        for i in range(len(text)):
            Box.insert(END,text[i])

    openit.mainloop()



# when the user wants to search for a recipe by any ingredient name
# this function is called once the user clicks the "find" button after enttering
# the name of the ingredient to look for the recipe 
def openingIt():

    # it opens a window with a listbox to display all the search
    # results and to get these results
    # each file in the recipes folder i.e. each recipe is checked for
    # this keyword using the following procedure
    global tb
    global listb
    openn=Tk()
    openn.title("Search Results")
    results=Label(openn,text="Found what you were looking for?")
    results.pack()    
    listb=Listbox(openn,width="45")
    # . get() just gets the keyword the user enters
    entered=tb.get(1.0,END)
    entered=entered.strip()
    
    entered=entered.lower()
    
    # this for loop is used to load all the files in the recipes folder
    # loading means each file is opened and read from
    # whatever the file contains is stored in a variable called "txt"
    # this is the string in which , using the in function in the if condition,
    # we can look for
    # the keyword which is the substring
    
    for filename in os.listdir(os.getcwd()+"\\recipes"):
        cwd=os.getcwd()
        nameofFile=join(cwd+"\\recipes",filename)
        f=open(nameofFile, 'r') 
        txt=f.read()
        txt=txt.lower()
        if entered in txt:
            # if it is found then the name of that recipe can be taken
            # from the name of the file which is the "filename"
            # this filename is the "recipenameprotocol"
            # the name of the recipe is stored in a variable called "name_enter"
            # and inserted into the listbox containing the search results
            name_enter=filename.replace("protocol","")
            
            listb.insert(END,name_enter)
        # after each file is loaded and the keyword is searched  for in it
        # it must be closed before another file is loaded because
        # each file in the variable "f" is loaded using the for loop
        f.close()

    # if len(list(listb.get(0,END)))==0 checks for the following:
    # incase no match is found for this particular keyword
    # it just adds the following line to the litbox
    if len(list(listb.get(0,END)))==0:
        listb.insert(END,"Sorry no matches,try searching with different keyword")
        
        
    listb.pack()
    b1=Button(openn,text="open")
    b1.pack()





    

        
    
    








# this function is called when the button below the label
# "search by" is clicked
# this button reads "Ingredient"
# this function opens a small window
def search_ing():
    # the window opened contains a textbox called tb
    # this is made global because the text entered by the
    # user into this textbox is used in another function
    # called when the "find" button from this window is clicked
    # after the user enters the keyword to be searched
    # this window has the following gui with a button and a
    # small textbox and a label
    global tb
    openthis=Tk()
    openthis.title("Search By Ingredient")
    tb=Text(openthis,width="35",height="1")
    
    
    '''for filename in os.listdir(os.getcwd()+"\\recipes"):
        print filename'''
    tb.grid(row=0,column=1)
    labl=Label(openthis,text="Enter the name")
    labl.grid(row=0,column=0)
    find_btn=Button(openthis,text="Find",command=openingIt)
    find_btn.grid(row=0,column=2)
    openthis.mainloop()


    

    



listItems=[]




# this  function is responsible to add ingredients to the
# grocery list i.e. the listbox which contains all the ingredients
# which the user added to from different recipes
def go_shopping():
    global ingBox
    global Box1
    global listItems
    # in case the user adds something to the grocery list and this listbox
    # called Box1 has not been created then it equals None
    # because box1 is created by a function which is called when
    # the "grocery list" button from the main menu is pressed and
    # this is pressed only when the user wants to view the items
    # in the grocery list

    # if it is not pressed then whatever ingredient the user
    # adds to the grocery list will be stored in a list and
    # that list will be checked for elements(ingredients)
    # when box1 will be created ie whenever the user views the grocery list
    if Box1==None:
        
        item=ingBox.get(ACTIVE)
        
        listItems.append(item)
    else:
        # otherwise if the grocerylist has already been opened
        # the names will  be added directly to Box1
        # but one ingredient must not be repeated
        # so first the variable present is used to check
        # if the listbox is empty or not
        # and if its not empty does it already have an ingredient
        # which matches to the one that is going to be inserted
        # using the .insert() function
        
        present=Box1.get(0,END)
        
        present=list(present)
        
        item=ingBox.get(ACTIVE)
        
        if len(present)==0:
            Box1.insert(END,item)

        else:
            # if it does not contain the same ingredient already then the ingredient
            # is added to  Box1 using the .insert() function
            for i in range (len(present)):
                if item not in present:
        
                    Box1.insert(END,item)
    



# the following 2 functions "openList" and "open_rcp"
# work exactly the same way
# exept that they refer to two different windows and hence are called
# when buttons on separate windows are pressed
# they just read from the already present recipes and display them
# in the required format
def open_recipe():
    
    # below is described the gui for this format
    # in which a recipe is to be displayed
    # when its name is clicked from the listbox
    # in this case its called "Box"
    global Box
    global ingBox
    name=Box.get(ACTIVE)
    cwd=os.getcwd()
    # the recipe to be opened is in the listbox called Box
    # however this was saved with the name "recipenameprotocol" in the directory
    # so protocol_file is a variable that stores this name as it is in the directory
    protocol_file=join(cwd+"\\recipes",name+"protocol")
    
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
    

    # initializing the list called "listt"
    # as an empty list
    listt=[]

    # initializing another varibale "cn" to an empty string
    cn=""

    # the variable f stores all the lines as strings
    # as elements in a list
    # after the file is opened to read  in a variable "f"
    f=open(protocol_file).readlines()
    #nodestart is another variable that keeps track if
    # some part of the recipe has started
    # or is it just a # or @ or other parts of the protocol
    nodestart=False
    # according to the protocol the start of
    # something is @ and the end is a newline and a #

    # for loop goes over each line and checks
    for i in range(len(f)):
        # if the line has a # which is always in a separate
        # line because of the \n at the end of it
        # then this means the next line will have  what
        # we need, an ingredient,name,etc
        if "#" in f[i]:
            nodestart=False
            # cn is an empty string in the start however it is
            # added to the empty list
            # basically cn is the current node(or part of a string)
            listt.append(cn)
            # cn becomes empty again as it has added to the list
            # whatever useful strings it found
            cn=""
           
        if nodestart:
            cn=cn+f[i]

        # the start of anything useful from the file
        # will always have an @ symbol
        # so if this is found then nodestart becomes True
        # and when this becomes true the previous condition
        # adds that line from the list f to the current node or cn variable
        # as soon as this ends , it reaches a #
        # hence whatever the cn is till now
        # it adds to the list
        if "@" in f[i]:
            nodestart=True


    # because of the specific protocol that was followed when these recipes
    # were saved in files
    # we know by convention that the first thing in the file will
    # always be the name, and the second the ingredients
    # followed by the instructions
    # followed by the number of people it serves
    # and the last one will be the preparation time

    # since these are the sequence of the parts of the recipe stored in the list
    # called "listt" then this list is accessed when these are  to be displayed
    Name=listt[0]
    list_ingred=listt[1].split("\n")
    prepTime=listt[4]
    People=listt[3]
    Instructions=listt[2]

    # the list at different indices is a string so each for loop below
    # loops over each part of this string and inserts it to its textbox
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



# this function works the same way as the one above
# the only difference is that the name of the recipe to be opened
# is taken from a different listbox which belongs to a different window( the
# search results window)
# and is called lb
def open_rcp():
    cwd=os.getcwd()
    global lb
    
    global ingBox
    name=lb.get(ACTIVE)
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


# when the "find" button is clicked this is called
# takes what the user enters as the search keywords
def openList():
    global showit
    global lb
    # it opens a window with a listbox and the following layout and labels
    openn=Tk()
    openn.title("Search Results")
    results=Label(openn,text="Found what you were looking for?")
    results.pack()    
    lb=Listbox(openn,width="45")

    # entered sttored what the  user enters into the textbox called "showit"
    # from the previous function, which is why its global
    entered=showit.get(1.0,END)
    entered=entered.strip()

    
    # listdir is a function that gives a list
    # of all the files in a particular directory
    # here we need a list of files in the folder "recipes"
    for filename in os.listdir(os.getcwd()+"\\recipes"):

        # to get the name of the recipe the string "protocol" is
        # removed by the .replace() function
        # and the key word entered by the user in the searchbar
        # was stored in the variable "entered"
        # so if in checks  if the keyword is a substring of any file name
        # because file names were contained the name of the recipe
        # when they were saved in this folder
        
        filename=filename.replace("protocol","")
        
        
        if entered.lower() in filename.lower():
            # if the keyword is part of the file name then this particular recipe
            # has been found, and in the for loop each file in the directory is checked
            # to find a match and each time a match is found
            # the name of that recipe is appended to the lb made above
            # on the window which opens
            # when this function is called
            
            lb.insert(END,filename)

    # if len(list(lb.get(0,END)))==0 checks for the following:
    # incase no match is found for this particular keyword
    # it just adds the following line to the litbox


    
    if len(list(lb.get(0,END)))==0:
        lb.insert(END,"Sorry no matches,try searching with different keyword")
    lb.pack()

    buttn=Button(openn,text="open",command=open_rcp)
    buttn.pack()
    
    
    openn.mainloop()
# this function is used to search for a recipe by its name
# so it opens a small window  which is type of a search bar
# the button in it "find"
# calls another function called "openList"
def search_name():
    global showit
    # the showit variable is made global because the
    # openit function needs to get the text entered in that
    # by the user to look for the recipes with that text

    # below is the gui for this search bar window 
    openthis=Tk()
    openthis.title("Searching For Recipe")
    showit=Text(openthis,width="35",height="1")
    
    
    '''for filename in os.listdir(os.getcwd()+"\\recipes"):
        print filename'''
    showit.grid(row=0,column=1)
    labl=Label(openthis,text="Enter the name")
    labl.grid(row=0,column=0)
    find_btn=Button(openthis,text="Find",command=openList)
    find_btn.grid(row=0,column=2)
    openthis.mainloop()



# called when the "Join the Cookbook Club" button
# from the first window that opens when the maincode is run
# is pressed
# it contains all the buttons and almost every feature for this application
# so this start window will enable the user to add recipes, view them, seacrh
# and the following function has its layout, which contains many buttons with
# call back functions
# those functions are written above
def start():
    menu=Tk()
    button1=Button(menu,text="Add New Recipe",command=createRecipe)
    button1.grid(row=0,column=0)
    
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
    filter2=Button(menu,text="Ingredient",command=search_ing)
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


############################################################################# MAIN CODE ################################################################### 

# code to initialize all the global variables being used  above

listb=None
tb=None
lb=None
showit=None
Box=None
Box1=None
ingBox=None

# the first window being opened by .Tk() has an image on it which
# is saved in the same folder and called "startup.jpg"
# the following is the layout for thr gui of the first window that opens up
path = 'startup.jpg'
root = Tk()
root.title("My Digital CookBook")
help_btn=Button(root,text="About")
help_btn.pack()
btn=Button(root,text="Join the Cookbook Club",command=start)
btn.pack()

# ImageTk.PhotoImage is used to open and display this photo on the window

img = ImageTk.PhotoImage(Image.open(path))
panel =Label(root, image = img)
panel.pack(side="bottom", fill = "both", expand = "yes")
btn2=Button(root,text="Quit",command=byebye)
btn2.pack()


    
root.mainloop()
