The program is written in python 3.6. The libraries imported are:
1. urllib
2. json
3. time
4. tkinter
5. functools ->lru_cache
The GUI is divided into two parts. The upper part contains a string (Enter a keyword), an input box, and a button(Search) stacked vertically. The lower part contains a grid with index ID, Title, and Author. 
The program takes in the input from the input box when the submit button is pressed. The input is concatenated with the URL string and the URL returns a text in JSON format. The text is converted into JSON using library functions and the ID, title and the name of author are extracted and displayed. For the first result, the publisher and the published date are also extracted and displayed. 
The start time and the end time are calculated. The time taken to display the results is calculated by taking the difference of them and is displayed at the bottom of the screen. 
For the program, a cache memory of 32 bytes is allocated in the starting.
Created by
Kanishk Katara
2017AAPS0416H
