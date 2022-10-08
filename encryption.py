from itertools import cycle
import hashlib
import base64

def custom_enc(phrase, key='', isbytes=False):
	key = hashlib.sha256(key.encode()).hexdigest()
	kylst = list(key)
	if not isbytes:
		prlst = list(phrase.encode())
	if isbytes:
		prlst = list(phrase)
	count = 0
	for i in range(len(prlst)):
		if count > len(kylst)-1:
			count = 0
		if isinstance(prlst[i], str):
			prlst[i] = int(ord(prlst[i])+ord(kylst[count]))
		if isinstance(prlst[i], int):
			prlst[i] = int(prlst[i]+ord(kylst[count]))
		else:
			raise TypeError(f"phrase list was not int or str, {prlst[i]}: {type(prlst[i])}")
		while prlst[i] > 110000:
			prlst[i] -= 110000
		while prlst[i] < 0:
			prlst[i] += 110000
		count += 1

	outlist = []
	for i in prlst:
		outlist.append(chr(i).encode())
	return b''.join(outlist)

def custom_enc_file(filedata, key=''):
	if not isinstance(filedata, bytes):
		raise TypeError("filedata is not bytes, byteslike object required")
	else:
		return enc(filedata, key=key, isbytes=True)

def custom_dec(phrase, key='', isbytes=False):
	key = hashlib.sha256(key.encode()).hexdigest()
	kylst = list(key)
	if not isbytes:
		prlst = list(phrase.encode())
	if isbytes:
		prlst = list(phrase)
	count = 0
	for i in range(len(prlst)):
		if count > len(kylst)-1:
			count = 0
		if isinstance(prlst[i], str):
			prlst[i] = int(ord(prlst[i])-ord(kylst[count]))
		if isinstance(prlst[i], int):
			prlst[i] = int(prlst[i]-ord(kylst[count]))
		else:
			raise TypeError(f"phrase list was not int or str, {prlst[i]}: {type(prlst[i])}")
		while prlst[i] > 110000:
			prlst[i] -= 110000
		while prlst[i] < 0:
			prlst[i] += 110000
		count += 1

	outlist = []
	for i in prlst:
		outlist.append(chr(i))
	return ''.join(outlist)

def custom_dec_file(filedata, key=''):
	if not isinstance(filedata, bytes):
		raise TypeError("filedata is not bytes, byteslike object required")
	else:
		return dec(filedata, key=key, isbytes=True)

def xor_encrypt(data, key=''):
	if not isinstance(key, bytes):
		try:
			key = key.encode()
		except:
			# can't turn into bytes
			raise TypeError("not string, could not convert to bytes like object")
	key = hashlib.sha256(key).hexdigest()
	if isinstance(data, bytes):
		xored = ''.join(chr(x^ord(y)) for (x,y) in zip(data, cycle(key)))
	else:
		xored = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(data, cycle(key)))
	return base64.b64encode(xored.encode()).strip().decode()

def xor_enc_file(filedata, key=''):
	if not isinstance(filedata, bytes):
		raise TypeError("Not byteslike object unable to encrypt filedata")
	else:
		return xor_encrypt(data=filedata, key=key)

def xor_decrypt(data, key=''):
	if not isinstance(key, bytes):
		try:
			key = key.encode()
		except:
			# can't turn into bytes
			raise TypeError("not string, could not convert to bytes like object")
	key = hashlib.sha256(key).hexdigest()
	if isinstance(data, bytes):
		data = base64.b64decode(data)
		xored = ''.join(chr(x ^ ord(y)) for (x,y) in zip(data, cycle(key)))
	else:
		data = base64.b64decode(data.encode()).decode()
		xored = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(data, cycle(key)))
	return xored

def xor_dec_file(filedata, key=''):
	if not isinstance(filedata, bytes):
		raise TypeError("Not byteslike object unable to decrypt filedata")
	else:
		return xor_decrypt(data=filedata, key=key)

if __name__ == '__main__':
	while True:
		try:
			c = input("[e]ncrypt or [d]ecrypt:\n- ")
			m = 'xor'#input("[xor] or [custom]:\n- ")
			if c.lower() == 'e':
				if m.lower() == 'xor':
					print(xor_encrypt(data=str(input("phrase:\n- ")),key=str(input("Key:\n- "))))
				#if m.lower() == 'custom':
				#	print(custom_enc(key=input("Key:\n- "), phrase=input("phrase:\n- ")).decode())
				if m.lower() != 'xor' and m.lower() != 'custom':
					print("you did not select a viable option")
			if c.lower() == 'd':
				if m.lower() == 'xor':
					print(xor_decrypt(data=input("phrase:\n- "), key=str(input("Key:\n- "))))
				#if m.lower() == 'custom':
				#	print(custom_dec(key=input("Key:\n- "), phrase=input("phrase:\n- ")))
				if m.lower() != 'xor' and m.lower() != 'custom':
					print("you did not select a viable option")
		except EOFError:
			print("Exiting")
			break
		except KeyboardInterrupt:
			print("Exiting")
			break
		except Exception as e:
			print(e)
			break