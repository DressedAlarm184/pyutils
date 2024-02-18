class UTILITIES:
	@staticmethod
	def countchars(txt,char):
		count = 0
		for letter in txt:
			if letter == char:
				count += 1
		return count
	
	@staticmethod
	def reverse(txt):
		return txt[::-1]
	
	@staticmethod
	def encrypt(text, shift = 7):
		encrypted_text = ''
		for char in text:
			if char.isalpha():
				if char.isupper():
					encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
				else:
					encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
			else:
				encrypted_text += char
		return encrypted_text

	@staticmethod
	def decrypt(text, shift = 7):
		decrypted_text = ''
		for char in text:
			if char.isalpha():
				if char.isupper():
					decrypted_text += chr((ord(char) - 65 - shift) % 26 + 65)
				else:
					decrypted_text += chr((ord(char) - 97 - shift) % 26 + 97)
			else:
				decrypted_text += char
		return decrypted_text

	@classmethod
	def methods(cls):
		class_attributes = dir(cls)
		all_methods = [attr for attr in class_attributes if callable(getattr(cls, attr))]
		methods = []
		for method in all_methods:
			if method.find("__") != -1:
				continue
			methods.append(method)
		return methods