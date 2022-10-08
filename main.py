import encryption as enc
import os

class main:
	def __init__(self):
		pass

	def terminal(self):
		avcommands = ["help","encrypt","decrypt","hide","reveal","quickhide","quickreveal"]
		while True:
			c = str(input("$> "))
			if "\"" in c:
				c = c.split("\"")
				args = [c[1]]
				for i in c[2].split(" "):
					args.append(i)
				c = c[0].split(" ")
				c.pop(c.index(""))
				c = c[0]
				args.pop(args.index(""))
			else:
				args = c.split(" ")[1:]
				c = c.split(" ")[0]
			
			print(c,args)

			if not (c.lower() in avcommands):
				continue

			if c.lower() == avcommands[0]:
				print('\n'.join(avcommands))
			
			if c.lower() == avcommands[1]:
				print("encrypt")
				if len(args) >= 1:
					print("enough args")
					if self.isfile(args[0]):
						print("file")
						data = self.readfile(args[0])
						if len(args) > 1:
							key = args[1]
						else:
							key = ''
						enc.custom_enc_file(filedata=data, key=key)
					else:
						print("string")
						if len(args) >= 1:
							data = args[0]
							if len(args) > 1:
								key = args[1]
							else:
								key = ''
							print("output")
							print(enc.custom_enc(phrase=data, key=key).decode())
				else:
					print("not enough arguments")

			if c.lower() == avcommands[2]:
				if len(args) >= 1:
					print("enough args")
					if self.isfile(args[0]):
						data = self.readfile(args[0])
						if len(args) > 1:
							key = args[1]
						else:
							key = ''
						enc.custom_dec_file(filedata=data, key=key)
					else:
						if len(args) >= 1:
							data = args[0]
							if len(args) > 1:
								key = args[1]
							else:
								key = ''
							print(enc.custom_dec(phrase=data, key=key))
				else:
					print("not enough arguments")
			if c.lower() == avcommands[3]:
				print("command unavailable at this time")

			if c.lower() == avcommands[4]:
				print("command unavailable at this time")

			if c.lower() == avcommands[5]:
				print("command unavailable at this time")

			if c.lower() == avcommands[6]:
				print("command unavailable at this time")

	def GUI(self):
		while True:
			c = easygui.buttonbox("Select an option")

	def writefile(self, filename, data):
		if not isinstance(data, bytes):
			if not isinstance(data, list):
				raise TypeError("Data is not byteslike object, cannot write to file")
			if isinstance(data, list):
				if not isinstance(data[0], bytes):
					raise TypeError("Data is not byteslike object, cannot write to file")
				else:
					islist=True
		else:
			if islist:
				with open(filename, 'wb') as f:
					f.write(b''.join(data))
			if not islist:
				with open(filename, 'wb') as f:
					f.write(data)
			return "400 OK | Operation Completed"

	def readfile(self, filename):
		with open(filename, 'rb') as f:
			data = f.readlines()
		return b''.join(data)

	def hide_data(self, image_name, data):
		return out_image

	def reveal_data(self, image_name):
		return data

	def isfile(self, quest):
		if os.path.isfile(quest):
			return True
		return False

if __name__ == '__main__':
	mn = main()
	mn.terminal()