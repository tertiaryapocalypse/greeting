import json
import datetime
import os
import webbrowser

username = 'username.json'
todayis = datetime.datetime.now() 
tasklist = 'tasks.json'
weather_url = 'https://wttr.in/'

'''
TO-DO:
- https://pypi.org/project/keyboard/ <- key lock rather than input funct.
- revise the editing tool a bit so invalid keystrokes dont do anything, after keystroke 
implementation
- if you do end up putting it on github make a userguide
'''



#navigation command, shows user possible actions
def say_something(): 
	print("\nVIEW TO-DO LIST: V\nEDIT TO-DO LIST: E\nVIEW NASA IOTD: N\nVIEW WEATHER: W")
	action = input("\nWhat would you like to do?\n").lower()
	do_something(action)
	
def repeat_something():
	run_again = input("Would you like to do anything else? (Y/N)\n").lower()
	if (run_again == 'y'):
		os.system('cls')
		say_something()
	else:
		os.system('cls')
		print(f'Have a good day, {user}!')

#runs user action & prompts nav again if desired
def do_something(action):
	os.system('cls')
	#prints tasklist if available, otherwise runs set up
	if (action == "v"):
		try: 
			with open(tasklist) as f:
				tasks = json.load(f)
				for task in tasks:
					print(task)
		except FileNotFoundError:
			task_setup()
	#opens editor if available, otherwise runs set up
	elif (action == "e"):
		try: 
			with open(tasklist) as f:
				task_edit()
		except FileNotFoundError:
			task_setup()
	#opens nasa's astronomy image of the day in a new tab
	elif (action == "n"):
		webbrowser.open_new_tab('https://apod.nasa.gov/apod/astropix.html')
	#opens reno weather in a new tab
	elif (action == 'w'):
		webbrowser.open_new_tab(weather_url)
	elif (action == 'p'):
		with open('prayer.txt') as f:
			print(f.read())
	repeat_something()

#if user chooses to edit the to-do list		
def task_edit():
	act = ''
	while (act != 'q'): 
		with open(tasklist) as f:
			tasks_start = json.load(f)
			tasks = tasks_start[:]
			for task in tasks:
				print(task)
			print('ADD TASK: A\nREMOVE TASK: D\nQUIT EDITOR: Q')
			act = input().lower()
			if (act == 'a'):
				temp = input('What do you need to do?\n')
				tasks.append(temp)
				os.system('cls')
				with open(tasklist, 'w') as j:
					json.dump(tasks, j)
				continue
			elif (act == 'd'):
				temp = int(input('Which # task are you done with?\n'))
				temp = temp-1
				del tasks[temp]
				os.system('cls')
				with open(tasklist, 'w') as j:
					json.dump(tasks, j)
				continue
			
#sets up to-do list if there is none
def task_setup():
	set_up_start = input("There doesn't seem to be a to-do list on file. Would you like to set one up? (Y/N)\n").lower()
	if (set_up_start == 'n'):
		repeat_something()
	elif (set_up_start == 'y'):
		tlist = []
		ans = 'y'
		while (ans != 'n'):
			new_task = input("What do you need to do?\n")
			tlist.append(new_task)
			ans = input("Would you like to add something else? (Y/N)\n").lower()
		with open(tasklist, 'w') as f:
			json.dump(tlist, f)
		with open(tasklist) as f:
			os.system('cls')
			tasks = json.load(f)
			for task in tasks:
				print(task)

#on open, sets up nav
try:
	with open(username) as f:
		user = json.load(f)
except FileNotFoundError:
	user = input('What is your name? ')
	with open(username, 'w') as f:
		json.dump(user, f)
		os.system('cls')
		print(f'Nice to meet you, {user}.')
else:
	print(f'Welcome back, {user}!')

print(f'Today is {todayis.strftime("%A")}, {todayis.strftime("%b")} {todayis.strftime("%d")}, {todayis.year}.')
print(f'It is {todayis.strftime("%H")}:{todayis.strftime("%M")}.')
say_something()
