import os, subprocess

key:str = '6800330079005F006700550079005A00'

class Cryptor:
	
	def decrypt(raw:bytes) -> bytes:
		
		with open('tmp', 'wb') as f:
			f.write(raw)
			f.close()
		
		process = subprocess.Popen(f'openssl enc -d -nosalt -aes-128-cbc -in tmp -out tmp-out -K {key} -iv {key} -nopad'.split(' '), stdout=subprocess.PIPE)
		output, error = process.communicate()
		
		with open('tmp-out', 'rb') as f2:
			data:bytes = f2.read()
			f2.close()
			
		os.remove('tmp')
		os.remove('tmp-out')
		
		return data
	
	def encrypt(file_name:str, raw_bytes:bytes) -> str:
		
		with open('tmp-out', 'wb') as f:
			f.write(raw_bytes)
			f.close()
		
		process = subprocess.Popen(f'openssl enc -e -nosalt -aes-128-cbc -in tmp-out -out {file_name} -K {key} -iv {key} -nopad'.split(' '), stdout=subprocess.PIPE)
		output, error = process.communicate()
			
		os.remove('tmp-out')