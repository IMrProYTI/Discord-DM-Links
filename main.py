def getLink(userid):
	return f"https://discordapp.com/channels/@me/{userid}/"

def writeLink(link):
	print()
	print(f"The link: {link}")
	print()

def copyLink(text):
	answer = input("Do you want to copy the link? [y|N]: ")
	if answer == 'Y' or answer == 'y':
		from pyperclip import copy
		copy(text)
		print("Done!")


if __name__ == '__main__':
	link = getLink(input('Enter your or another userid/snowflake: '))
	writeLink(link)
	copyLink(link)
