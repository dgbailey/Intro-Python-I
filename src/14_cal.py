"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

def cal_func():
  #get command line args
  my_args = sys.argv[1:]
  

  my_calendar = calendar.Calendar()

  #evaluate conditions based on num args
  if len(my_args) == 0:
    
    return my_calendar.monthdayscalendar(datetime.today().year,datetime.today().month)

  elif len(my_args) == 1:
    
    
    return my_calendar.monthdayscalendar(datetime.today().year,int(my_args[0]))
    

  elif len(my_args) == 2:
   
    return  my_calendar.monthdayscalendar(int(my_args[1]),int(my_args[0]))

  else: 
    print("Incorrect argument format received, expected 14_cal.py month [year]")
  


print(cal_func())


