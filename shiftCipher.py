import os

def encrypt(plaintext,key):
	cipherText = ''
	try:
		keyFilled = str(key * (int(len(plaintext) / len(key)) + 1))[:len(plaintext)]
		for i in range(1,len(plaintext)+1):
			if i % 2 == 0:

				cipherText += str((int(plaintext[i-1]) + int(keyFilled[i-1]) + int(keyFilled[i-1])) % 10)
			else:
				cipherText += str((int(plaintext[i-1]) + int(keyFilled[i-1])) % 10)
	except:
		print('Only Numerical Digit are allowded')

	return cipherText




def decrypt(cipherText,key):
	plainText= ''
	keyFilled = str(key * (int(len(plaintext) / len(key)) + 1))[:len(plaintext)]
	for i in range(1,len(cipherText)+1):
		if i % 2 == 0:

			plainText += str((int(cipherText[i-1]) - int(keyFilled[i-1]) - int(keyFilled[i-1])) % 10)
		else:

			plainText += str((int(cipherText[i-1]) - int(keyFilled[i-1])) % 10)
	return plainText	
	
def main():
	print('''
 ____  _     _  __ _      ____ _       _               
/ ___|| |__ (_)/ _| |_   / ___(_)_ __ | |__   ___ _ __ 
\___ \| '_ \| | |_| __| | |   | | '_ \| '_ \ / _ \ '__|
 ___) | | | | |  _| |_  | |___| | |_) | | | |  __/ |   
|____/|_| |_|_|_|  \__|  \____|_| .__/|_| |_|\___|_|   
	                        |_|                    
1.Encrypt Text
2.Decrypt Text
3.Exit

	''')

while True:
	os.system('clear')
	main()
	options = input('Enter the option : ')
	if options == '1':
		plaintext = input('Enter the Digit to encrypt : ')
		key = input('Enter the Key : ')
		cipher=encrypt(plaintext,key)
		print(f'The Cipher Text :  {cipher} \n\n')
		input('Enter to continue..')
	elif options == '2':
		ciphertext = input('Enter the Cipher Text : ')
		key = input('Enter the Key : ')
		text=decrypt(ciphertext,key)
		print(f'The Plain Text :  {text} \n\n')
		input('Enter to continue..')
	elif options == '3':
		print('Bye')
		exit()
