import urllib.request, urllib.parse, urllib.error
import json
import time
from tkinter import *
#Allocating cache memory
from functools import lru_cache
@lru_cache(maxsize=32)              #cache memory size=32

def disptxt():  #This function takes in a keyword from the search box and displays the results
    url='https://www.googleapis.com/books/v1/volumes?'
    tm1=time.time()      #start time
    vol=kw.get()
    
    url1=url+urllib.parse.urlencode({'q': vol})     #Creating URL
    uh=urllib.request.urlopen(url1)
    data=uh.read().decode()
    try:
        js=json.loads(data)             #Converting data into JSON
    except:
        js=None
        print('==== Failure To Retrieve ====')
    i=0             #no of results
    while True:
        try:
            id=Label(rf, text=js['items'][i]['id'], fg='blue')      #Fetching book ID
            id.grid(row=i+1, column=0)              #Displaying book ID
            title=Label(rf, text=js['items'][i]['volumeInfo']['title'], fg='blue')      #Fetching title of the book
            title.grid(row=i+1, column=1)       ##Displaying title of the book
            aut=str()
            j=0
            while True:
                try:
                    if j==0:
                        aut=aut+js['items'][i]['volumeInfo']['authors'][j]
                    else:
                        aut=aut+', '+js['items'][i]['volumeInfo']['authors'][j]
                    j=j+1
                except:
                    break
            author=Label(rf, text=aut, fg='blue')
            author.grid(row=i+1, column=2)      #Displaying names of authors of the book seperated by commas
            if i==0:
                i=i+1
                t1='Publisher : '+ js['items'][i]['volumeInfo']['publisher']+'         Published Date : '+ js['items'][i]['volumeInfo']['publishedDate']
                publisher=Label(rf, text=t1, fg='blue')
                publisher.grid(row=i+1, column=1)       #Displaying publisher and published date of the top result
            i=i+1
        except:
            break
    tm2=time.time()      #end time
    s1='Total time taken : '+str(tm2-tm1)+' seconds'          #Display the total time taken
    i=i+1
    tm=Label(rf, text=s1)
    tm.grid(row=i+1, columnspan=3)          
    return

#Creating a GUI
root = tk.Tk()
root.title("Search for books")
root.geometry("700x400")   
kw=tk.StringVar()
lf=Frame(root)          #Upper part of frame
lf.pack()
rf=Frame(root)          #Lower part of frame
rf.pack()

#Creating the search box and the button
l1= Label(lf, text='Enter a Keyword', fg='blue', font=("Helvetica", 20))
l1.grid(row=0)
l2= Entry(lf, textvariable=kw)
l2.grid(row=1)
l3= Button(lf, text='Search', command=disptxt, fg='white', bg='blue')
l3.grid(row=2, padx=10, pady=10)
l4= Label(lf, text='')
l4.grid(row=3)

#Creating the first row (Index)
t1= Label(rf, text='ID', fg='blue', bg='yellow', font=("Helvetica", 12))
t1.grid(row=0, column=0, sticky=W+E+N+S)
t2= Label(rf, text='Title', fg='blue', bg='yellow', font=("Helvetica", 12))
t2.grid(row=0, column=1, sticky=W+E+N+S)
t3= Label(rf, text='Author', fg='blue', bg='yellow', font=("Helvetica", 12))
t3.grid(row=0, column=2, sticky=W+E+N+S)
root.mainloop()