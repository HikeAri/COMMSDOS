
import datetime
def changelog():
	print('pynotes for COMMSDOS Version: 1.5.1a')
	print('=--==============================--=\n')
	print("-Added import of module 'datetime'")
	print("-Added command '--refresh'")
	print("-Added command '--version'")
	print("-Added command '--remove'")
	print("-Added file 'pynotes_ota_upd.txt' for ota checks on latest versions of pynotes.")
	print('-Changed --exit command sequence (Now appends the date and time before leaving).')
	print('-Fixed newline syntaxes.')
	print('-Modified command displays.\n')

def removeline(a):
	with open('dos_storage_dir\\notes.txt', 'r') as f:
		lines = f.readlines()
		f.close()
	with open('dos_storage_dir\\notes.txt', 'w') as f:
		for line in lines:
			if line.strip('\n') != a:
				f.write(line)
				f.close
	print(f">Removed line containing {a}.")

def helpcmd():
	print('List of commands available:\n')
	print('--version			[Displays current version and checks for the latest version of pynotes ]')
	print('--changelog			[Displays the latest changes made into the software]')
	print('--read				[Prints out the contents from notes.txt file]')
	print('--refresh			[Clears the terminal]')
	print('--remove <input>		[Removes a line from your note that contains the word/sentence from <input>]')
	print('--exit				[Exits software]\n')

def verpynote():
	with open('dos_storage_dir\\pynotes_ota_upd.txt', 'r') as ota:
		otaread = ota.read()
		ota.close()
	otainfo = otaread.split()
	if otainfo[0] == '1.5.1a':
		version = 'OTA check complete: No available latest version of pynotes.'
	else:
		version = f'Latest version of pynotes available! Available update: v{otainfo[0]} [{otainfo[1]}]'
	print("Copyright (C) pynotes inc. 200X")
	print("Created by Benedict J. Kelvin and Yugora Hersson")
	print("Current pynotes version: v1.5.1a")
	print(version)

def refreshterm():
	clear_terminal()
	print('\n>Welcome to pynotes for COMMSDOS desktops!')
	print('All your notes will be appended automatically. Type "--help" for list of commands.\n')
            
def readall():
    with open('dos_storage_dir\\notes.txt', 'r') as n:
        readcontent = n.read()
        n.close()
    return readcontent
            

print('\n>Welcome to pynotes for COMMSDOS desktops!')
print('All your notes will be appended automatically. Type "--help" for list of commands.\n')
while True:
	inp = str(input('> '))
	inplist = inp.split()
	if len(inp) == 0:
		with open('dos_storage_dir\\notes.txt', 'a') as n:
			n.write('\n')
			n.close()
	elif inp == '--exit':
		with open('dos_storage_dir\\notes.txt', 'a') as n:
			n.write(f'[^Note(s) as of {datetime.datetime.today().strftime("%d-%m-%Y, %I:%M %p")}] \n')
			n.close()
		print('>Exiting pynotes...')
		break
	elif inp == '--changelog':
		changelog()
	elif inp == '--version':
		verpynote()
	elif inp == '--refresh':
		refreshterm()
	elif inp == '--read':
		print(readall())
	elif inplist[0] == '--remove':
		try:
			inplist[1]
			inplist.pop(0)
			removeline(" ".join(inplist))
		except IndexError:
			print('>Argument error. Proper syntax: --remove <input>')
	elif inp == '--help':
		helpcmd()
	else:
		with open('dos_storage_dir\\notes.txt', 'a') as n:
			n.write(inp + '\n')
			n.close()
