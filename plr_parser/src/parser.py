import struct
from plr_parser.src.aes128cbc import Cryptor

class Read:
	
	def int8(byte:bytes) -> int:
		return struct.unpack('<b', byte)[0]
	
	def uint8(byte:bytes) -> int:
		try: return struct.unpack('B', byte)[0]
		except: return int(byte)
		
	def int32(byte:bytes) -> int:
		return struct.unpack('i', byte)[0]
	
	def uint32(byte:bytes) -> int:
		return struct.unpack('<I', byte)[0]
	
	def bool(byte:bytes) -> bool:
		return bool(Read.uint8(byte))
	
	def bytes(byte:bytes, count:int=0) -> dict:
		return [byte[i] for i in range(count)]

	def string(byte:bytes, count:int=0) -> str:
		return ''.join([chr(i) for i in Read.bytes(byte, count)])
		

class Parser(object):
	
	def __init__(self, file:str) -> None:
		self.file:str = file
		self.bytes_crypt:bytes
		self.offset:int = 0
		
	
	def _bytes(self, num:int, offset_get:bool = True) -> bytes:
		if offset_get :
			self.offset+=num
			return self.offset-num, self.bytes_crypt[self.offset - num : self.offset]
		else:
			return self.bytes_crypt[self.offset: self.offset+num]
	
	def get(self) -> object:
		
		_raw:bytes = open(self.file, 'rb').read()
		self.bytes_crypt:bytes = Cryptor.decrypt(_raw)
		
		class data:
			
			version:int = Read.uint32(self._bytes(4)[1])
			company:str = Read.string(self._bytes(7)[1], 7)
			fileType:int = Read.uint8(self._bytes(1)[1])
			
			self.offset+=12
			
			name_lenght:int = Read.uint8(self._bytes(1)[1])
			name:str = Read.string(self._bytes(name_lenght)[1], name_lenght)
			difficulty:int = Read.int8(self._bytes(1)[1])
			playTime:int = int(struct.unpack('<Q', self._bytes(8)[1])[0])/10000000
			
			self.offset+=9
			
			statLife:int = Read.int32(self._bytes(4)[1])
			statLifeMax:int = Read.int32(self._bytes(4)[1])
			statMana:int = Read.int32(self._bytes(4)[1])
			statManaMax:int = Read.int32(self._bytes(4)[1])
			extraAccessory:int = Read.bool(self._bytes(1)[1])
			
			self.offset+=1
			
			taxMoney:int = Read.int32(self._bytes(4)[1])
			
			self.offset+=23
			
			armor:dict = [{'id': Read.int32(self._bytes(4)[1]), 'prefix': Read.uint8(self._bytes(1)[1])} for i in range(3)]
			acsesuars:dict = [{'id': Read.int32(self._bytes(4)[1]), 'prefix': Read.uint8(self._bytes(1)[1])} for i in range(6)]
			
			self.offset+=10
			
			dye:dict = [{'id': Read.int32(self._bytes(4)[1]), 'prefix': Read.uint8(self._bytes(1)[1])} for i in range(12)]
			
			self.offset+=35
			
			inventory=[]
			for i in range(58):
				id:int=Read.int32(self._bytes(4)[1])
				if id >= 5080 or id == 0:
					inventory.append({'id': 0})
					self.offset+=6
				else: inventory.append({'id': id, 'stack': Read.int32(self._bytes(4)[1]), 'prefix': Read.uint8(self._bytes(1)[1]), 'favorites': Read.bool(self._bytes(1)[1])})
				
		return data
	
	def get_bytes_map(self) -> object:
		
		_raw:bytes = open(self.file, 'rb').read()
		self.bytes_crypt:bytes = Cryptor.decrypt(_raw)
		
		class data:
			
			version:tuple = self._bytes(4)
			company:tuple = self._bytes(7)
			fileType:tuple = self._bytes(1)
			
			self.offset+=12
			
			name_lenght:tuple = self._bytes(1)
			name:tuple = self._bytes(Read.uint8(name_lenght[1]))
			difficulty:int = self._bytes(1)
			playTime:tuple = self._bytes(8)
			
			self.offset+=9
			
			statLife:tuple = self._bytes(4)
			statLifeMax:tuple = self._bytes(4)
			statMana:tuple = self._bytes(4)
			statManaMax:tuple = self._bytes(4)
			extraAccessory:tuple = self._bytes(1)
			
			self.offset+=1
			
			taxMoney:tuple = self._bytes(4)
			
			self.offset+=23
			
			armor:dict = [{'id': self._bytes(4), 'prefix': self._bytes(1)} for i in range(3)]
			acsesuars:dict = [{'id': self._bytes(4), 'prefix': self._bytes(1)} for i in range(6)]
			
			self.offset+=10
			
			dye:dict = [{'id': self._bytes(4), 'prefix': self._bytes(1)} for i in range(12)]
			
			self.offset+=35
			
			inventory:dict = []
			for i in range(58):
				inventory.append({'id': self._bytes(4), 'stack': self._bytes(4), 'prefix': self._bytes(1), 'favorites': self._bytes(1)})
				
		return data, self.bytes_crypt
		
