##coded by Syntaxxx
##telegram @syntaxxxtechexpert

import requests, datetime, sys

if sys.version_info[0] !=3:
	print('''--------------------------------------
	REQUIRED PYTHON 3.x
	use: python3/python 'auto-comment.py'
--------------------------------------
			''')

##Headers
header = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
    }

##This is the site's Form Data
add_comment = {
    'notenumber' : '2yrwpi'
    }

##Welcome message
print("coded by", end=" >> ")
print("1Syntaxxx1")
print("Telegram", end=" @")
print("syntaxxxtehexpert")
print("""

          ░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░
          ░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗
          ░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║
          ░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║
          ░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝
          ░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░

                   ░█████╗░░█████╗░███╗░░░███╗███╗░░░███╗███████╗███╗░░██╗████████╗  ██████╗░░█████╗░████████╗
                   ██╔══██╗██╔══██╗████╗░████║████╗░████║██╔════╝████╗░██║╚══██╔══╝  ██╔══██╗██╔══██╗╚══██╔══╝
                   ██║░░╚═╝██║░░██║██╔████╔██║██╔████╔██║█████╗░░██╔██╗██║░░░██║░░░  ██████╦╝██║░░██║░░░██║░░░
                   ██║░░██╗██║░░██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝░░██║╚████║░░░██║░░░  ██╔══██╗██║░░██║░░░██║░░░
                   ╚█████╔╝╚█████╔╝██║░╚═╝░██║██║░╚═╝░██║███████╗██║░╚███║░░░██║░░░  ██████╦╝╚█████╔╝░░░██║░░░
                   ░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░  ╚═════╝░░╚════╝░░░░╚═╝░░░, This is a beta version.
""")

##When this function is called the comment will be added to site
def addcomment():
    with requests.Session() as s:
        url = 'https://anotepad.com/note/addcomment'
        add_comment['name'] = input('What name should be on comment? ')
        add_comment['content'] = input('What is the comment? ')
        try:
            request = s.get(url, headers=header)
            request = s.post(url, data=add_comment, headers=header)
            print(request.content)
        except:
            raise ConnectionError("🅸🅽🆃🅴🆁🅽🅴🆃 🅴🆁🆁🅾🆁.")
        global Timeofcomment
        Timeofcomment = datetime.datetime.now().strftime("%c")
        print("This Message was sent at ", Timeofcomment)
        print("Loading", end="")
        for i in range(11):
            print(".", end="")

##This will loop until you are complete with program
while True:
    quit_command = input('\nDo you want to quit [y/n]?')
    print('\nYour comment can be viewed at this website', end=" >> ")
    print('https://anotepad.com/notes/2yrwpi\n')
    try:
        if quit_command == 'y':
            exit()
        elif quit_command == 'n':
            addcomment()
            print("\nAll info is logged in a log.txt in the local directory.")
            log = open('log.txt', 'a+')
            print("=================================================================\n", "Message sent", Timeofcomment, "\n", "message: ", add_comment['content'], "\n", "sent by: ", add_comment['name'], "\n", "=================================================================\n", file=log)
            log.close()
        else:
            print("Unexpeted input: %s" % quit_command)
    except:
        raise Exception("Error!")
        raise SystemExit("Bye!")
        raise ConnectionError("🅸🅽🆃🅴🆁🅽🅴🆃 🅴🆁🆁🅾🆁.")
