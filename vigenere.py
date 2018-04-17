# import pyperclip
alphabet  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():

	print("##################################################################")
	print("#                                                                #")
	print("#         Author : Oumar Djimé Ratou                             #")
	print("#         Algorithme : Viginère                                  #")
	print("#                                                                #")
	print("##################################################################")

	while 1:
		
		print()
		print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		print("+ PROGRAMME QUI CHIFFRE ET DECHIFFRE LE MESSAGE AVEC LA CRYPTOSYSTEME DE VIGINERE +")
		print("+     (encrypt) CHIFFRER                                                          +")
		print("+     (decrypt) DECHIFFRER                                                        +")
		print("+     (Q)       QUITER                                                            +")
		print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		print()
		myMode = input("Entrez votre choix :")

		if myMode == 'encrypt':
			myMessage = input("Veillez entrer le message à chiffrer  :")
			myKey = input("Veillez entrer la phrase secrète :")
			translated = encryptMessage(myKey, myMessage)
		elif myMode == 'decrypt':
			myMessage = input("Veillez entrer le message à dechiffrer :")
			myKey = input("Veillez entrer la phrase secrète :")
			translated = decryptMessage(myKey, myMessage)
		# print('%sed message : '% (myMode.title()))
		elif myMode=='Q':
			print("Merci d'avoir esseyer notre Programme, bye bye !!!!!!!")
			break	
		print(translated)
		# pyperclip.copy(translated)
		print()
		# print('The message has been copied to the clipboard.')

def encryptMessage(key, message):
	return translateMessage(key, message, 'encrypt')

def decryptMessage(key, message):
	return translateMessage(key, message, 'decrypt')

def translateMessage(key, message, mode):
	translated = [] #stocke le message chiffrer/dechiffrer

	keyIndex = 0
	key = key.upper()

	for symbol in message:
		num = alphabet.find(symbol.upper())
		if num != -1:
			if mode == 'encrypt':
				num+= alphabet.find(key[keyIndex])
			elif mode == 'decrypt':
				num-= alphabet.find(key[keyIndex])

			num %= len(alphabet)

			if symbol.isupper():
				translated.append(alphabet[num])
			elif symbol.islower():
				translated.append(alphabet[num].lower())

			keyIndex += 1
			if keyIndex == len(key):
				keyIndex = 0
		else:
			translated.append(symbol)	
	return ''.join(translated)	
	

#--------------------Programme principal---------------------------------------

if __name__ == '__main__':
	main()				
						
					




































