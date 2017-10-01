from DES import *

def main():
	fuct = input("0 to encryption, 1 for decryption : ")
	if fuct = 0:
		Enc()
	else:
		Dec()
		
def Dec():
	rfile = input("please input file for decryption ")
	lines = open(rfile,"r")
	bigLine =''
	for line in lines:
		line = line.strip('\n')
		bigLine+= line
	lines.close()

	keyFile = input("please input key file: ")
	keyLines = open(keyFile,'r')
	Key =''
	for line in keyLines:
		line = line.strip('\n')
		Key+= line
	keyLines.close()

	wfile = input("please input file to write ")
	lines = open(wfile,'w')

	for i in range(0,len(bigLine),64):
		curBlock = bigLine[i:i+64]
		Decrypted = DES_D(curBlock,Key)
		lines.write(Decrypted)
	lines.close()

def Enc():
	rfile = input("please input file for encryption ")
	lines = open(rfile,"r")
	bigLine =''
	for line in lines:
		line = line.strip('\n')
		bigLine+= line
	lines.close()

	keyFile = input("please input key file: ")
	keyLines = open(keyFile,'r')
	Key =''
	for line in keyLines:
		line = line.strip('\n')
		Key+= line
	keyLines.close()

	wfile = input("please input file to write ")
	lines = open(wfile,'w')

	for i in range(0,len(bigLine),64):
		curBlock = bigLine[i:i+64]
		Encrypted = DES_E(curBlock,Key)
		lines.write(Encrypted)
	lines.close()

main()