import random
import time
import DES as D16
import DES_8round as D8

def toBi(a):
	return str(a) if a<=1 else toBi(a>>1) + str(a&1)
def main():
	print('----------------------')
	print("TESING DEFAULT DES")
	print("testing 1 block of 64-bit plaintText")
	plaintBlock = toBi(random.randint(0,2**63))
	Key = toBi(random.randint(0,2**63))
	while len(plaintBlock) <64:
		plaintBlock = '0'+plaintBlock
	while len(Key) < 64:
		Key = '0' + Key
	s =  time.time()
	cipherBox = D16.DES_E(plaintBlock,Key)
	print("Ecryption time took %s mili-seconds" % ((time.time() - s) * 10**3) )
	s = time.time()
	plaintBlock = D16.DES_D(cipherBox,Key)
	print("Decryption time took %s mili-seconds"%((time.time() - s) * 10**3))
	print("================================================================")
	print('testing for 1000 block of 64-bit plainText')
	blockList =[]
	cipherList=[]
	for i in range(1000):
		plaintBlock = toBi(random.randint(0,2**63))
		while len(plaintBlock) <64:
			plaintBlock = '0'+plaintBlock
		blockList.append(plaintBlock)
	s =time.time()
	while len(blockList) > 0:
		cipherList.append(D16.DES_E(blockList.pop(),Key))
	print("Ecryption time took %s mili-seconds" % ((time.time() - s) * 10**3) )
	s =time.time()
	while len(cipherList) >0:
		blockList.append(D16.DES_D(cipherList.pop(),Key))
	print("Decryption time took %s mili-seconds" % ((time.time() - s) * 10**3) )
	print("================================================================")
	print('testing for 10000 block of 64-bit plainText')
	blockList =[]
	cipherList=[]
	for i in range(10000):
		plaintBlock = toBi(random.randint(0,2**63))
		while len(plaintBlock) <64:
			plaintBlock = '0'+plaintBlock
		blockList.append(plaintBlock)
	s =time.time()
	while len(blockList) > 0:
		cipherList.append(D16.DES_E(blockList.pop(),Key))
	print("Ecryption time took %s mili-seconds" % ((time.time() - s) * 10**3) )
	s =time.time()
	while len(cipherList) >0:
		blockList.append(D16.DES_D(cipherList.pop(),Key))
	print("Decryption time took %s mili-seconds" % ((time.time() - s) * 10**3) )
	print('---------------------------')
	print('TESTING 8-round DES')
	print("testing 1 block of 64-bit plaintText")
	plaintBlock = toBi(random.randint(0,2**63))
	Key = toBi(random.randint(0,2**63))
	while len(plaintBlock) <64:
		plaintBlock = '0'+plaintBlock
	while len(Key) < 64:
		Key = '0' + Key
	s =  time.time()
	cipherBox = D8.DES_E(plaintBlock,Key)
	print("Ecryption time took %s mili-seconds" % ((time.time() - s) * 10**3) )
	s = time.time()
	plaintBlock = D8.DES_D(cipherBox,Key)
	print("Decryption time took %s mili-seconds"%((time.time() - s) * 10**3))
	print("================================================================")
	print('testing for 1000 block of 64-bit plainText')
	blockList =[]
	cipherList=[]
	for i in range(1000):
		plaintBlock = toBi(random.randint(0,2**63))
		while len(plaintBlock) <64:
			plaintBlock = '0'+plaintBlock
		blockList.append(plaintBlock)
	s =time.time()
	while len(blockList) > 0:
		cipherList.append(D8.DES_E(blockList.pop(),Key))
	print("Ecryption time took %s mili-seconds" % ((time.time() - s) * 10**3) )
	s =time.time()
	while len(cipherList) >0:
		blockList.append(D8.DES_D(cipherList.pop(),Key))
	print("Decryption time took %s mili-seconds" % ((time.time() - s) * 10**3) )
	print("================================================================")
	print('testing for 10000 block of 64-bit plainText')
	blockList =[]
	cipherList=[]
	for i in range(10000):
		plaintBlock = toBi(random.randint(0,2**63))
		while len(plaintBlock) <64:
			plaintBlock = '0'+plaintBlock
		blockList.append(plaintBlock)
	s =time.time()
	while len(blockList) > 0:
		cipherList.append(D8.DES_E(blockList.pop(),Key))
	print("Ecryption time took %s mili-seconds" % ((time.time() - s) * 10**3) )
	s =time.time()
	while len(cipherList) >0:
		blockList.append(D8.DES_D(cipherList.pop(),Key))
	print("Decryption time took %s mili-seconds" % ((time.time() - s) * 10**3) )




main()

