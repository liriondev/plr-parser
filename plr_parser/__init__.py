from plr_parser.src.parser import Parser
from plr_parser.src.aes128cbc import Cryptor

def get_data(file:str) -> object:
	return Parser(file).get()

def get_bytes_map(file:str) -> object:
	return Parser(file).get_bytes_map()

def save(file_name:str, raw_bytes:bytes) -> str:
	Cryptor.encrypt(file_name, raw_bytes)
