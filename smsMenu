import requests

def Send_SMS():
	resp = requests.post('https://textbelt.com/text', {
  'phone': (target_number),
  'message': (target_msg),
  'key': '3ab03b66488923feeada54e25e5118781c190991RIHEVBwMxq0XoZuG8EsnZNJyl',
})
	print(resp.json())
	return




# Start of the Run!

print('\n\n\n\n')
print('**********************************************')
print('**********************************************')
print('**********************************************')
print('**********                          **********')
print('**********  SMS CASTER VERSION 0.1  **********')
print('**********                          **********')
print('**********************************************')
print('**************************  By Ctabora10  ****')
print('**********************************************')


print('\n\n\n\n')

print('Welcome to the SMS Caster! Lets get started,')


# Collect the Number to Send to

target_number = int(input('Who is the target number to send to?'))
target_msg = input("What would you like to text to TARGET:")


print('Okay, I think I have everything I need if youre ready..')
print('The number you chose was ->')
print('\n')
target_select = input("Are you sure you want to send? (y/n)")




#Selection Screen

if target_select == str("y"):
	print('Okay you asked for it.. lol')
	#print(target_number)
	Send_SMS()
else: print("You selected no.. I see.. ")
