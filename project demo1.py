from os.path import *
import os
from Tkinter import *
from PIL import ImageTk, Image


import socket

#this function was a helper function created as directed by the pseudocode

def leftrotate(x,c):

    return (x<<c)&0xFFFFFFFF|(x>> (32-c)&0x7FFFFFFF>>(32-c))


#this function connects to the server
#socket.socket means to create a socket, and that newly created socket is saved in a variable called s
#s.connect takes in one variable which is a tuple containing the port number and the IP address to which it will connect
#s is returned as it is used as the connection which is an input parameter for many of the functions defined below

def StartConnection(IPaddress,portNumber):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IPaddress, portNumber))
    return s



#this function lets a user login successfully as it is used for authentication
#it will return false if  the password entered is wrong 

def login(s,username,password):
    #s.send means sending to the server which is connnected by the socket s
    #we are sending a string so the str function is being used
    s.send("LOGIN" + " " +str(username)+"\n")
    #data contains the string that the server sends
    data=s.recv(512)

    #length_username is a variable that stores the length of the username which is an integer
    length_username=len(username)
    #Start_index is where the challenge sent by the server begins
    Start_index=7+length_username
    #Challenge_string is the slice of data(what is received from the server) that contains the challenge
    Challenge_string=data[Start_index:]
    #n and m are variables which were specified in the handout as the length of the password and the username
    n=len(password)
    m=length_username
    
    ##message is a concatenation of the password and the challenge, its a string

    message=password+(Challenge_string.strip("\r\n"))
    #messageLength contains the length of the message and it is converted to a string as it has to be part of
    #the string which will be sent to the server finally
    messageLength=str(len(message))

    #adding 1 to the end of the concatenation is a rule from the MD5 instrucions
    message=message+"1"
    #finalLength is the length of this concatenation after 1 has been added
    finalLength=len(message)
    #the total length minus the last three digits is (516-3) which is 509 so we need to extend the concatenation till 509 characters by adding zeros
    #then add the length of the "message" so the message becomes 512 characters long

    #a while loop makes sure that zeros are only added till the length becomes 509
    #message and the final length is updated each time the loop iterates
    #to message a zero is added each time and to the length 1 is added since zero is 1 character long

    while finalLength!=509:
        
        message=message+"0"
        finalLength=finalLength+1

        
    #the length of the messageLength which is to  be added at the end of  the concatenation
    #must be 3 digits long so zeros are added to it to make it long enough
    if len(messageLength)==3:
        messageLength=""+str(messageLength)
    if len(messageLength)==1:
        messageLength="00"+str(messageLength)
    elif len(messageLength)==2:
        messageLength="0"+str(messageLength)
        
    #this is converted to a string and appended to the cocantenation called message        
    message=message+str(messageLength)

    #M and listofchunks are 2 empty lists initially
    M=[]
    listofchunks=[]
    #index0,index1,etc are the chunks each of 32 characters from the concatenation
    index0=message[0:32]
    index1=message[32:64]
    index2=message[64:96]
    index3=message[96:128]
    index4=message[128:160]
    index5=message[160:192]
    index6=message[192:224]
    index7=message[224:256]
    index8=message[256:288]
    index9=message[288:320]
    index10=message[320:352]
    index11=message[352:384]
    index12=message[384:416]
    index13=message[416:448]
    index14=message[448:480]
    index15=message[480:512]

    #these chunks are  appended to the list called listofchunks which was empty earlier
    listofchunks.append(index0)
    listofchunks.append(index1)
    listofchunks.append(index2)
    listofchunks.append(index3)
    listofchunks.append(index4)
    listofchunks.append(index5)
    listofchunks.append(index6)
    listofchunks.append(index7)
    listofchunks.append(index8)
    listofchunks.append(index9)
    listofchunks.append(index10)
    listofchunks.append(index11)
    listofchunks.append(index12)
    listofchunks.append(index13)
    listofchunks.append(index14)
    listofchunks.append(index15)
    
#r iterates through each element of the listofchunks, which is a string, and j goes over
#each character of the string which is always 32 characters long and each character
#is a number whose ascii values' sum we need so we find it in chunks of 32 as each element is 32 characters long
#the variable input_ord saves what is to be given to the ord function
#so input_variable contains 1 character of the 32 character long element, as we are adding the ascii values one after the other
#ord of this input will  return one ascii value
#sumOfascii contains the sum 32 characters as it is part of both loops
#but when adding this sum to the list M, it is important that M is only in the for loop which iterates through each element,hence M
#will have 16 elements, each representing the sum of 32 characters from the previous list which was called listofchunks


    sumOfascii=0
    for r in range(len(listofchunks)):
        sumOfascii=0
        for j in range(32):
            input_ord=listofchunks[r][j]
            asciiValue=ord(input_ord)
            sumOfascii=sumOfascii+asciiValue


        M.append(sumOfascii)

###############   PSEUDOCODE BEGINS ################:
    
    S=[7,12,17,22,7,12,17,22,7,12,17,22,7,12,17,22,5,9,14,20,5,9,14,20,5,9,14,20
       ,5,9,14,20,4,11,16,23,4,11,16,23,4,11,16,23,4,11,16,23,6,10,15,21,6,10,15,21,6,10,15,21,6,10,15,21]





    K=[0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee,
    0xf57c0faf, 0x4787c62a, 0xa8304613, 0xfd469501,
    0x698098d8, 0x8b44f7af, 0xffff5bb1, 0x895cd7be, 
    0x6b901122, 0xfd987193, 0xa679438e, 0x49b40821,
    0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa, 
    0xd62f105d, 0x02441453, 0xd8a1e681, 0xe7d3fbc8, 
    0x21e1cde6, 0xc33707d6, 0xf4d50d87, 0x455a14ed, 
    0xa9e3e905, 0xfcefa3f8, 0x676f02d9, 0x8d2a4c8a, 
    0xfffa3942, 0x8771f681, 0x6d9d6122, 0xfde5380c, 
    0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70, 
    0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x04881d05, 
    0xd9d4d039, 0xe6db99e5, 0x1fa27cf8, 0xc4ac5665, 
    0xf4292244, 0x432aff97, 0xab9423a7, 0xfc93a039, 
    0x655b59c3, 0x8f0ccc92, 0xffeff47d, 0x85845dd1, 
    0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1, 
    0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391] 
    
    
    a0=0x67452301
    b0=0xefcdab89
    c0=0x98badcfe
    d0=0x10325476


    A=a0
    B=b0
    C=c0
    D=d0



    for i in range(0,64):
        if i<=15 and i>=0:
            F=(B & C) | ((~ B) & D)
            F=F&0xFFFFFFFF
            g=i
        elif i<=31 and i>=16:
            F=(D & B) | ((~ D) & C)
            F=F&0xFFFFFFFF
            g=(((i*5)+1)%16)
        elif i>=32 and i<=47:
            
            F=B ^ C ^ D
            F=F&0xFFFFFFFF
            g=(((3*i)+5)%16)
        elif i>=48 and i<=63:
            
            F=C^(B | (~ D))
            F=F&0xFFFFFFFF
            g=((7*i)%16)
        
        dTemp=D
        D=C
        C=B
        B=B+leftrotate((A+F+K[i]+M[g]),S[i])
        B=B&0xFFFFFFFF
        A=dTemp
    
    a0=(a0+A)& 0xFFFFFFFF
    b0=(b0+B)& 0xFFFFFFFF
    c0=(c0+C)& 0xFFFFFFFF
    d0=(d0+D)& 0xFFFFFFFF
    result= str(a0)+str(b0)+str(c0)+str(d0)

    #result is a variable that contains the message digest which was being calculated above
    
    
    send_command="LOGIN"+" "+str(username)+" "+str(result)+"\n"
    
    
    s.send(send_command)

    msg_recvd=s.recv(512)
    #msg_recvd is a variable which has the string which the server sends once it receives the messagedigest in the above format
    #format means it should always have the newline character and username in the exact order
    
    msg_recvd=msg_recvd.strip()
    #to easily interpret what the server sends back it is better to strip it of spaces, new line characterss,etc
    #so we know exactly what the command sent by the server is and we can return True and False when the login is successful or not.
    #to return True if statement was used.

    
    
    
    if msg_recvd=="Login Successful":
        return True
    else:
        return False



#this returns a list of active users

def getUsers(s):
    #s.send sends the protocol "@users" to the server
    s.send("@users")
    #recvd stores whatever is returned by the server
    recvd=s.recv(512)
    #we already know the form in which the string is sent back hence we know that the start of the string will always contain the size which will be 5
    #digits long and an "@" character at the beginning so from 1 till 6 means we only get the slice of the string which represents the size
    #this  size is stored in a variable called recvd_size
    recvd_size=int(recvd[1:6])
    #all the "@" characters are replaced by a comma in this string
    recvd=recvd.strip("@")
    recvd=recvd.replace("@",",")
    #it is converted to a list using a split function which has each string (separated by a comma) as an element inside this string
    Users_list=recvd.split(",")
    
    
    Users=[]
    #Users is initially empty but then using a for loop which iterates from the  3rd to the last element of the list "Users_list"
    #every element of that list is appended to the list called Users which is returned
    #the reason why the range for the for loop is from 3 is because we know that the 3rd index onwards are all the usernames of the active
    #users which is sent by the server , this sequence of size,usernames, etc was given in the table of protocols in the handout
    for l in range(3,(len(Users_list))):
        Users.append(Users_list[l])

    #this list called Users is to be returned
    return Users



#this function sends a file to any other user who is in a user's friend list

def sendFile(s,filename):
#the variable f is used to open the file for reading it
    f=open(filename)
#the function readlines returns whatever is in the file and retrns that as a list of strings by reading the file line  after line
    listOfData=f.readlines()
#the variable listOfData stores this list of strings that readlines() returns

    #file string is an empty string and is used to initialize the variable in which the content of thee file will be stored as a list
    #so to convert this content to a string the for loop iterates over each element of  the list called listOfData and each
    #element here means each line of the file which was read earlier
    #it then adds these lines, afer converting them using the str function, to the file_string
    #the loop iterates over the length of the list so that all the file content is stored ti file_string
    file_string=""
    for i in range(len(listOfData)):
        file_string=file_string+listOfData[i]
    
    #filecontent is just another variable which stores all this filecontent
    filecontent=str(file_string)
   
    #send_msg is part of the message to be sent to the server, however to put it in the form desribed as the protocol, an "@" character is
    #being addded to parts of the string
    #send_msg however does not contain the size of the string which will be sent, including the actual size of the string which represents how long
    #the actual string will be , and that size needs to be 5 digits long always, so that "@"
    #plus the length 5 is added to the size of the string being sent
    #the size and "@" character will always add up to 6 characters in length
    #but the length of send_msg may vary depending on the amount of the file content
    
    send_msg="@sendfiler@"+str(filename)+"@"+filecontent
    sizeOfstring=str(6+(len(send_msg)))
    #sizeOfstring is the size of the complete string which is beinng sent

    #the following if statements make sure this size is 5 digits long
    #if its less than 5 then zeros are added as per need after checking its length
    if len(sizeOfstring)==1:
        sizeOfstring="0000"+str(sizeOfstring)
    elif len(sizeOfstring)==2:
        sizeOfstring="000"+str(sizeOfstring)
    elif len(sizeOfstring)==3:
        sizeOfstring="00"+str(sizeOfstring)
    elif len(sizeOfstring)==4:
        sizeOfstring="0"+str(sizeOfstring)

    #according to the protocol described even this string should have an "@" character at the beginning
    sizeOfstring="@"+sizeOfstring

    #this size is appended to the string "send_msg" which contains the message to be sent to the server the way its described in the protocol
    #and a new variable now contains this updated version of the message to be sent
    #this variable is called "sendToserver"
    sendToserver=sizeOfstring+send_msg
    
    #s.send(sendToserver) sends this message to the server connected by the input connection "s"
    s.send(sendToserver)

    #recvd is the variable which stores whatever is received from the server and if it contains the string
    #"not found" in it then it returns False otherwise it returns True
    #this is because it only returns True if the file or message is received and when it is successfully received it doesn't
    #contain the "not found" string in the string which the recepient receives from the server


    recvd=s.recv(512)
    

    if "not found" in recvd:
        return False
    else:
        return True
    
    

def countfiles(serverString):
    count=0
    for i in range (len(serverString)):
        if "file" in serverString:
            count=count+1
    return count



#this function returns a tuple which has two lists, each list itself contains tuples
#one list has the tuples containing the username and the message(a string) sent by that user
#the other one contains tuples which have the username and the name of the file sent by  that user
#also on receving a file it downloads that and saves its content to a file

def getMail(s):
    content=[]
    # s.send sends "@rxmsg" as described in the  protocol
    s.send("@rrxmsg")
    # the variable recvd stores what the server sends back, this is striped to remove spaces and next line characters, etc 
    recvd=s.recv(512)
    print recvd, "i received this"
    liststrs=[]
    str_sent=recvd
    if "@file@" in str_sent:
        done=False
        
        while not done:
            if "@file@" not in str_sent:
                    done=True
            index=str_sent.index("@file@")
            # slicing is the index where file content for the first file starts 
            slicing=index+6
            strSlice=str_sent[slicing:]
            # figure out if this is the last file
            numFiles=strSlice.count("@file@")
            print "count:", numFiles

            if numFiles==0:
                f_content=strSlice
                liststrs.append(f_content)
                
                done=True

            else:
                index=strSlice.index("@file@")
                f_content=strSlice[:index]
                print f_content
                liststrs.append(f_content)
                ind=index+6
                str_sent=str_sent[ind:]

        # to get actual file content
                
                    

        print liststrs
        l_actualcont=[]
        
        
        for i in range (len(liststrs)):
            found=(liststrs[i]).index("@")
            each_file=liststrs[i]
            usernm=each_file[:found]
            newSlice=each_file[found+1:]
            newIndex=newSlice.index("@")
            filName=newSlice[:newIndex]
            newIndex=newIndex+1
            actualcontent=newSlice[newIndex:]
            tuup=(usernm,filName,actualcontent)
            l_actualcont.append(tuup)

        print "list of tuples",l_actualcont
            
        
    









    
    recvd=recvd.strip()
    
    recvd=recvd.replace("@",",")
    #all the "@" characters are replaced by a comma in this string

    #it is converted to a list using a split function which has each string (separated by a comma) as an element inside this string
    #this list is called recvd_content
    recvd_content=recvd.split(",")

    #Contentlist,Msgs,and Files are initially empty lists 
    Contentlist=[]
    Msgs=[]
    Files=[]
    #then usernames and messages are appended to "Msgs" as tuples
    #and usernames and filenames are appended to "Files" as tuples also


    #Contentlist is empty initially , then using a for loop which goes through each element of the list "recvd_content"
    #appends each element to Contentlist, because recvd_content contained each string from the file received as an element of the list
    #according to the protocol the file which is received has the username of the user sending it followed by the name of the file,followed by
    #whatever is contained in the file as strings, this was stored in the recvd_content after spliting it into a list
    #the range of the for loop is from 2, because the first two elements need not to be added, they only represent  the  size
    #of whatever is sent by the server and the number of items(number of messages and files) received by the user who is logged in
    for t in range(2,(len(recvd_content))):
        Contentlist.append(recvd_content[t])

    print "Contentlist =" , Contentlist
    #according to the protocol the username of the person sending a file/message is always
    #followed by the message otherwise the file name then its content
    #but the word "msg" and "file" indicate whether the next string will be corresponding to  a file or a msg
    #since the size and number of items received was not added
    #the "Contentlist" will look somewhat like this :
    # ["msg","ryoosufani","hey","file","hanna22","sample.txt","rija i made this file so you could test"]
    #if for example a user named "ryoosufani" sent a message which read "hey" and another user named "hanna22" sent a file
    #called "sample.txt" which contained the text "rija i made this file so you could test" then the list above would be the "Contentlist"
    #and the first index will always be the string "msg" or "file"

    for i in range(len(Contentlist)):
        #the for loop goes through the entire list from beginning to end
        #if it comes across the string "msg" which indicates a new message has been received
        #it appends to "Msgs" the message and the username of the person who sent it  and the message itself
        #so if the list at index i is "msg" at (i+1) it will be the name of the  user and at (i+2) will be the message itself
        
        if Contentlist[i]=="msg":
            
            
            Msgs.append((Contentlist[i+1],Contentlist[i+2]))

        #if it comes across the string "file" which indicates a new file has been received
        #it appends to "Files" the username of the person who sent it  and the filename 
        #so if the list at index i is "file" at (i+1) it will be the name of the  user and at (i+2) will be the filename
        '''print "this is it",Contentlist'''
        if Contentlist[i]=="file":
            
            
            Files.append((Contentlist[i+1],Contentlist[i+2]))
            #index=Contentlist.index('#')
            #print "this is the last ind of #", index
            #print "contentlist from hashtag onwards", Contentlist[index+1:]
            print Files,"list of file and user"
            cwd=os.getcwd()
            #to download  the file, we need to make a new file in the same folder/directory which has the same name as the
            #name of the file received
            #so "File_name" is the string which is the name of the file received
            File_name=str(Contentlist[i+2])
            File_name=File_name.strip()
            Filename=File_name.replace("protocol","")

            k=4
            print "k", k, Contentlist[5], "this was list[5]"
            print Contentlist[k]
            print k<(len(Contentlist))
            while k<(len(Contentlist)) and Contentlist[k]!="file":
                "entered while loop"
                content.append(Contentlist[k])
                k=k+1

            print "content", content

            if isfile(File_name.strip())==False:
                if isfile("Allnames.txt"):
                    f = open("Allnames.txt")
                    text = f.read()
                    f.close()
            
        # open the file again for writing
        # for not loosing the names of different recipes
        # already present they are saved in "text"-a variable
                f = open("Allnames.txt", 'w')
                F=File_name.replace("protocol","")
                print "written to names",F
                f.write("//"+F)
        # write the original contents
                f.write(text)
                f.close()
            else:
        # if the file names.txt does not exist
        # for example when running the app for
        # the first time then this file is
        # created automatically
                F=File_name.replace("protocol","")
                
                
                f = open("Allnames.txt", 'w')
                f.write("//"+F)
                f.close()

            
            Path=join(cwd+"\\recipes",File_name)
            print "this is the path", Path
            print "saves with this name in recipes folder", File_name

            #to create a file with this filename, or overwrite one that exists with the same name in this directory
            #we need to open that file for writing
            DownloadFile=open(Path,'w')
            #in Contentlist each time a file was received that is, each time a string called "file" was at an index, then
            #relative to the same index, 3 indexes ahead will be the string which represents the text in the file,
            #hence "Contentlist[i+3]" is the file content and is to be saved/written to the file opened for writing
            for j in range (len(l_actualcont)):
                firstup=l_actualcont[j]
                if File_name in firstup:
                    cont=firstup[2]
                    print "gonna write ti file",cont 
                




                    DownloadFile.write(cont)


            #this last if statement makes sure that the file called "ryoosufahw7" which i am writing this code on, is not overwritten
            #if someone tries to be evil enough to send me another file with the same name and destroy my homework
            if "ryoosufahw7" in Contentlist[i+2]:
                #instead of overwriting my file, the "DownloadFile" variable opens a file named "you can't destroy my homework.txt"
                DownloadFile=open("you can't destroy my homework",'w')
                #and writes to it whatever is received, and saves my original file, by changing the name the file is downloaded successfully
                #but my original file remains unchanged
                DownloadFile.write(Contentlist[i+3])




    #outside the for loop is the return (Msgs,Files) , which returns a tuple of two lists
    #one list has been used for messages and contains tuples
    #the other one too contains tuples but is  used for files
    return (Msgs,Files)
    
            


    

    
    






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
        name_recipe=name_recipe.replace(" ","")
        
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
    favBox.delete(ACTIVE)
    


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
    global listFavz
    global Box
    global favBox
    favourites.title("Favvourite Recipes")
    label_1=Label(favourites,text="Favourites")
    label_1.pack()
    favBox=Listbox(favourites,width="25",height="25")
    favBox.pack()
    butn=Button(favourites,text="open")
    butn.pack()
    butnn=Button(favourites,text="delete from favourites", command=del_fav)
    butnn.pack()
    if listFavz!=None and (len(listFavz))!=0:
        print "list of favs", listFavz
        for i in range (len(listFavz)):
            print "inserting items"
            favBox.insert(END,listFavz[i])


    favBox.pack()
    favourites.bind('<Destroy>',winClosed)
    
    favourites.mainloop()

def winClosed(event):
    global favBox
    favBox=None

def windowClosed(event):
    global Box1
    Box1=None

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
        print "list of items", listItems 
        for i in range (len(listItems)):
            print "inserting items"
            Box1.insert(END,listItems[i])


    Box1.pack()
    show.bind('<Destroy>',windowClosed)
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
    favsBtn=Button(openit,text="Add to Favourites",command=go_favz)
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
            if text[i] not in Box.get(0,END):
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

listFavz=[]
def go_favz():
    global favBox
    global Box
    global listFavz
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
    if favBox==None:
        openfile=open("")
        item=Box.get(ACTIVE)
        
        listFavz.append(item)
    else:
        # otherwise if the grocerylist has already been opened
        # the names will  be added directly to Box1
        # but one ingredient must not be repeated
        # so first the variable present is used to check
        # if the listbox is empty or not
        # and if its not empty does it already have an ingredient
        # which matches to the one that is going to be inserted
        # using the .insert() function
        print Box
        present=favBox.get(0,END)
        
        present=list(present)

        item=Box.get(ACTIVE)
        
        if len(present)==0:
            favBox.insert(END,item)

        else:
            # if it does not contain the same ingredient already then the ingredient
            # is added to  Box1 using the .insert() function
            for i in range (len(present)):
                if item not in present:
        
                    favBox.insert(END,item)
    
        
    

    



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
        openfile=open("")
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
        print Box1
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
    global menu
    global Txt
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







#################################################################################################################################################


'''def windowClosed(event):
    global Txt
    global menu
    Txt.delete(0,END)'''



#this function is  basically used as a timer
#to keep checking is anything new is happening while still logged in, its just like refreshing
#it is a timer because it calls itself after every 7 seconds
def check():
    #chatWindow is the window which displays the menu with listboxes of requests,friends, and users
    #from the previous functions in homework 7 getMail returns a tuple of lists and these lists contain tuples of username and  message
    global menu
    global socket
    global Txt
    tuples=getMail(socket)
    #the variable tuples is this tuple
    #msgz is list of tuples of users and messages
    
    filez=tuples[1]

            
    
   
    

#Messages is another list which is initially empty by default but is there to call the startchat function to open a window (the one named openwnd) when it
#is passed as an input however, this was an optional input
#if,as soon as the chatwindow opens, there were some messages received while you were not logged in then this checks
#using a for loop to go over each tuple whether that user is already present in the dictionary (i.e. is a window for it already open)
    #however in a case where you just logged in d was an empty dictionary so it must pass overlook the if and go on to the else statement
    #here it calls startchat with the Messages, a list which has all the messages for the first user encountered in the list of tuples called "msgz"

    #the second instance is when the window of a specific user is already open and the dictionary contains the key named the username of the
    #person whose window is already opened or with whom a conversation is already in progress
    Files=[]
    for i in range (len(filez)):

        #user is a variable which stores the name of the user from the tuple inside the list
        #so msgz[i] for example could look like ("maimoon","how are you?")
        #then it goes from the zeroth index to the length which means the last one thats why msgz[i] uses "i" as the index
        #however in each tuple a format is fixed that the first element in the tuple will be the username and the second one will have the message
        #so msgz[i][0] could be for example= "maimoon" according to the above tuple i gave as an example
        #this is stored in a variable called user
        #another variable called msg stores the msg which in this case will be "how are you" and hence is equal to msgz[i][1]
        #for each tuple in msgz it either goes into the if or else
        user = filez[i][0]
        filee = filez[i][1]
        
        
        
            
        displaymsg=user+":"+filee+"\n"
            
            
        Txt.insert(END,displaymsg)
            
            
        
            

        
    

    menu.after(7000,check)
    #menu.bind('<Destroy>',windowClosed)
            




def logging_in():
    #this function creates the main menu window called "chatWindow" after the loginWindow
    #the layout of this window contains 3 listboxes all stored in separate variables
    #listbox1 contains all the users, listbox2 contains all the friends and listbox3 displays all your pending requests
    #quite a few of the variables have been made global as they are being used inside other functions in different sequences in which they are called
    
    global chatwindow
    global loginWindow
    global socket
    global listbox1
    global listbox3
    global listbox2
    global loginlist


    #in the main code the "loginWindow" has already been created with entry boxes and labels
    #we need the password and name of the user which is entered by him/her for authentication purposes
    #to get  these from corresponding entry boxes we use the .get() function
    #both username and password are stored in a list called "loginlist"
    #at index 0 is the username entered and at index 1 is the password entered
    loginlist=[userEntered.get(),passwordEntered.get()]
    username=loginlist[0]
    password=loginlist[1]

    #the login function is called with this specific username and corresponding password
    #it returns True if the password and username entered were correct and false otherwise


    #if its correct then this loginWindow must close and the "chatwindow" must show up and the 
    if login(socket,username,password):
        # code to initialize all the global variables being used  above

        

        # the first window being opened by .Tk() has an image on it which
        # is saved in the same folder and called "startup.jpg"
        # the following is the layout for thr gui of the first window that opens up
        '''path = 'startup.jpg'
        img = ImageTk.PhotoImage(Image.open(path))
        panel =Label(root, image = img)
        panel.pack(side="bottom", fill = "both", expand = "yes")'''
        root = Tk()
        root.title("My Digital CookBook")
        help_btn=Button(root,text="About")
        help_btn.pack()
        btn=Button(root,text="Join the Cookbook Club",command=start)
        btn.pack()

        # ImageTk.PhotoImage is used to open and display this photo on the window

       
        btn2=Button(root,text="Quit",command=byebye)
        btn2.pack()

        root.after(7000,check)
        #root.after(10000,req)
    
        root.mainloop()

        
        loginWindow.destroy()







##################################################### gui for login #####################################################################################
socket = StartConnection("86.36.33.206", 15112)
#socket is the connection which is given to most of the functions as an input parameter, its connected at the given IP address and port number

#since openwnd is a window has to be used as a global variable inside several functions it can be assigned any valuue initially
#which will be changed according to the sequence of events in which the functions using it are called
openwnd=""



#this loginWindow is the first window that opens up when the maincode is run, its not  tied to conditions like if this happens open this window,etc
#at the end of the maincode at the bottom is its mainloop, an infinite loop  which keeps it open
loginWindow=Tk()

#userentered is a variable that contains the string the user enters, this could be different each time hence it has inside it a tkinter Stringvar() funcion
userEntered=StringVar()
passwordEntered=StringVar()

#userEntered and passwordEntered both are variables that allow the user to enter strings to the entry boxes namely EnterUser and EnterPassword

loginWindow.geometry("200x200")
loginWindow.title("Sign In!")

#user and password are two variables used to store the labels on the window called loginWindow, these labels are displayed with the text assigned to each

#also whereever a window,button or label,entrybox or textbx, or listbox are created they must be packed so they are visible on the respective windows
#or they may be made visible using the .grid() notation in which the row number and column numbers are added relative to all other widgets on that window

user=Label(loginWindow,text="Username")
user.pack()



#EnterUser and EnterPassword are entry boxes where the user can type their password and username as the window opens


EnterUser=Entry(loginWindow,textvariable=userEntered)
EnterUser.pack()

password=Label(loginWindow,text="Password")
password.pack()
EnterPassword=Entry(loginWindow,textvariable=passwordEntered,show="*")
EnterPassword.pack()



chatwindow=0
#since chatwindow is a gllobal variable it needed to be assigned any value by default  before its used inside a function

#okayButton is the button on the startup window called loginWindow which asks for the username and password
#its linked to the function "logging_in" 
okayButton=Button(loginWindow,text="OK",command=logging_in)
okayButton.pack()


loginWindow.mainloop()









############################################################################# MAIN CODE ################################################################### 
favBox=None
listb=None
tb=None
lb=None
showit=None
Box=None
Box1=None

ingBox=None
