# LIBRARY FUNCTIONS 

# MD5 

from f_ import *

class MD5(object):
	def __init__(self):
		self.buffers = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476]

		self.sin_constants = [asint32(int(abs(math.sin(i+1)) * 2**32)) for i in range(64)]

		self.shift_table = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
							5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20,
							4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
							6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21]

	def _set_message(self, message):
		byte_message = bytearray(message)
		md5_input_length_data = asint64(len(byte_message) << 3)
		byte_message.append(0x80)

		while len(byte_message) % 64 != 56:
			byte_message.append(0x00)

		byte_message += int_to_bytes_length(md5_input_length_data, 8, False)

		return byte_message

	def _hash_message_chunk(self, chunk):
		temp_buffers = self.buffers[:]

		for round_itteration in range(16):
			temp_value = (temp_buffers[1] & temp_buffers[2]) | (~temp_buffers[1] & temp_buffers[3])
			chunk_index = round_itteration * 4
			temp_value = asint32(temp_value + temp_buffers[0] + self.sin_constants[round_itteration] + bytes_to_int(chunk[chunk_index:chunk_index+4], False))
			temp_value = asint32(temp_buffers[1] + shift_rotate_left(temp_value, self.shift_table[round_itteration]))
			temp_buffers = [temp_buffers[3], temp_value, temp_buffers[1], temp_buffers[2]]

		for round_itteration in range(16, 32):
			temp_value = (temp_buffers[1] & temp_buffers[3]) | (temp_buffers[2] & ~temp_buffers[3])
			chunk_index = (((5 * round_itteration) + 1) % 16) * 4
			temp_value = asint32(temp_value + temp_buffers[0] + self.sin_constants[round_itteration] + bytes_to_int(chunk[chunk_index:chunk_index+4], False))
			temp_value = asint32(temp_buffers[1] + shift_rotate_left(temp_value, self.shift_table[round_itteration]))
			temp_buffers = [temp_buffers[3], temp_value, temp_buffers[1], temp_buffers[2]]

		for round_itteration in range(32, 48):
			temp_value = fixedlen_xor(fixedlen_xor(temp_buffers[1], temp_buffers[2]), temp_buffers[3])
			chunk_index = (((3 * round_itteration) + 5) % 16) * 4
			temp_value = asint32(temp_value + temp_buffers[0] + self.sin_constants[round_itteration] + bytes_to_int(chunk[chunk_index:chunk_index+4], False))
			temp_value = asint32(temp_buffers[1] + shift_rotate_left(temp_value, self.shift_table[round_itteration]))
			temp_buffers = [temp_buffers[3], temp_value, temp_buffers[1], temp_buffers[2]]

		for round_itteration in range(48, 64):
			temp_value = fixedlen_xor(temp_buffers[2], (temp_buffers[1] | ~temp_buffers[3]))
			chunk_index = ((7 * round_itteration) % 16) * 4
			temp_value = asint32(temp_value + temp_buffers[0] + self.sin_constants[round_itteration] + bytes_to_int(chunk[chunk_index:chunk_index+4], False))
			temp_value = asint32(temp_buffers[1] + shift_rotate_left(temp_value, self.shift_table[round_itteration]))
			temp_buffers = [temp_buffers[3], temp_value, temp_buffers[1], temp_buffers[2]]

		self.buffers = [asint32(self.buffers[0] + temp_buffers[0]), 
						asint32(self.buffers[1] + temp_buffers[1]),
						asint32(self.buffers[2] + temp_buffers[2]),
						asint32(self.buffers[3] + temp_buffers[3])]


	def hash(self, message):
		byte_message = self._set_message(message)

		for chunk in to_blocks(byte_message, 64):
			self._hash_message_chunk(chunk)

		output = b""
		for x in self.buffers:
			output += (x).to_bytes(4, byteorder='little')

		return output
		
	def hash_digest(self, message):
		return self.hash(message).hex()

# MD4 

class MD4(object):
	def __init__(self):
		self.buffers = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476]

		self.shift_table = [3,  7, 11, 19, 3,  7, 11, 19, 3,  7, 11, 19, 3,  7, 11, 19,
							3,  5,  9, 13, 3,  5,  9, 13, 3,  5,  9, 13, 3,  5,  9, 13,
							3,  9, 11, 15, 3,  9, 11, 15, 3,  9, 11, 15, 3,  9, 11, 15]

		self.round_addition = [0x0, 0x5A827999, 0x6ED9EBA1]
		self.round_indexes  = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0,4,8,12,1,5,9,13,2,6,10,14,3,7,11,15,0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]

	def _set_message(self, message):
		byte_message = bytearray(message)
		md5_input_length_data = asint64(len(byte_message) << 3)
		byte_message.append(0x80)

		while len(byte_message) % 64 != 56:
			byte_message.append(0x00)

		byte_message += int_to_bytes_length(md5_input_length_data, 8, False)

		return byte_message

	def _hash_message_chunk(self, chunk):
		temp_buffers = self.buffers[:]
		for round_itteration, index in enumerate(self.round_indexes):
			if round_itteration < 16:
				temp_value = ((temp_buffers[1] & temp_buffers[2]) | (~temp_buffers[1] & temp_buffers[3])) + self.round_addition[0]
			elif round_itteration < 32:
				temp_value = ((temp_buffers[1] & temp_buffers[2]) | (temp_buffers[1] & temp_buffers[3]) | (temp_buffers[2] & temp_buffers[3])) + self.round_addition[1]
			else:
				temp_value = (fixedlen_xor(fixedlen_xor(temp_buffers[1], temp_buffers[2]), temp_buffers[3])) + self.round_addition[2]
				round_add = self.round_addition[2]

			chunk_index = index * 4
			temp_value = asint32(temp_value + temp_buffers[0] + bytes_to_int(chunk[chunk_index:chunk_index+4], False))
			temp_value = asint32(shift_rotate_left(temp_value, self.shift_table[round_itteration]))
			temp_buffers = [temp_buffers[3], temp_value, temp_buffers[1], temp_buffers[2]]

		self.buffers = [asint32(self.buffers[0] + temp_buffers[0]), 
						asint32(self.buffers[1] + temp_buffers[1]),
						asint32(self.buffers[2] + temp_buffers[2]),
						asint32(self.buffers[3] + temp_buffers[3])]

	def hash(self, message):
		byte_message = self._set_message(message)

		for chunk in to_blocks(byte_message, 64):
			self._hash_message_chunk(chunk)

		output = b""
		for x in self.buffers:
			output += (x).to_bytes(4, byteorder='little')
		
		return output
		
	def hash_digest(self, message):
		return self.hash(message).hex()

# SHA1

class SHA1(object):
	def __init__(self):
		self.buffers = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0]
		self.round_constants = [0x5A827999, 0x6ED9EBA1, 0x8F1BBCDC, 0xCA62C1D6]
		
	def _set_message(self, message):
		byte_message = bytearray(message)
		input_length_data = asint64(len(byte_message) << 3)
		byte_message.append(0x80)

		while len(byte_message) % 64 != 56:
			byte_message.append(0x00)

		byte_message += int_to_bytes_length(input_length_data, 8)

		return byte_message

	def _hash_message_chunk(self, chunk):
		temp_buffers = self.buffers[:]
		temp_chunks = bytes_to_intarray(chunk, 4, byte_order="big")

		for index in range(16, 80):
			temp_chunks.append(shift_rotate_left(temp_chunks[index-3] ^ temp_chunks[index-8] ^ temp_chunks[index-14] ^ temp_chunks[index-16], 1))

		for round_itteration in range(20):
			temp_value = fixedlen_xor((temp_buffers[1] & temp_buffers[2]), (~temp_buffers[1] & temp_buffers[3]))
			temp_value = asint32(shift_rotate_left(temp_buffers[0], 5) + temp_value + temp_buffers[4] + self.round_constants[0] + temp_chunks[round_itteration])
			temp_buffers = [temp_value, temp_buffers[0], shift_rotate_left(temp_buffers[1], 30), temp_buffers[2], temp_buffers[3]]

		for round_itteration in range(20, 40):
			temp_value = fixedlen_xor(temp_buffers[1], fixedlen_xor(temp_buffers[2], temp_buffers[3]))
			temp_value = asint32(shift_rotate_left(temp_buffers[0], 5) + temp_value + temp_buffers[4] + self.round_constants[1] + temp_chunks[round_itteration])
			temp_buffers = [temp_value, temp_buffers[0], shift_rotate_left(temp_buffers[1], 30), temp_buffers[2], temp_buffers[3]]

		for round_itteration in range(40, 60):
			temp_value = fixedlen_xor(fixedlen_xor((temp_buffers[1] & temp_buffers[2]), (temp_buffers[1] & temp_buffers[3])), (temp_buffers[2] & temp_buffers[3]))
			temp_value = asint32(shift_rotate_left(temp_buffers[0], 5) + temp_value + temp_buffers[4] + self.round_constants[2] + temp_chunks[round_itteration])
			temp_buffers = [temp_value, temp_buffers[0], shift_rotate_left(temp_buffers[1], 30), temp_buffers[2], temp_buffers[3]]

		for round_itteration in range(60, 80):
			temp_value = fixedlen_xor(temp_buffers[1], fixedlen_xor(temp_buffers[2], temp_buffers[3]))
			temp_value = asint32(shift_rotate_left(temp_buffers[0], 5) + temp_value + temp_buffers[4] + self.round_constants[3] + temp_chunks[round_itteration])
			temp_buffers = [temp_value, temp_buffers[0], shift_rotate_left(temp_buffers[1], 30), temp_buffers[2], temp_buffers[3]]

		self.buffers = [asint32(self.buffers[0] + temp_buffers[0]), 
						        asint32(self.buffers[1] + temp_buffers[1]),
						        asint32(self.buffers[2] + temp_buffers[2]),
						        asint32(self.buffers[3] + temp_buffers[3]),
						        asint32(self.buffers[4] + temp_buffers[4])]

	def hash(self, message):
		byte_message = self._set_message(message)

		for chunk in to_blocks(byte_message, 64):
			self._hash_message_chunk(chunk)

		output = b""
		for x in self.buffers:
			output += (x).to_bytes(4, byteorder='big')
		
		return output
		
	def hash_digest(self, message):
		return self.hash(message).hex()

# SHA256

class SHA256(object):
	def __init__(self, version=256, message_delimiter=None, output_size=None):
		self.round_constants = [0x0000000000000001, 0x0000000000008082, 0x800000000000808A, 0x8000000080008000,
								0x000000000000808B, 0x0000000080000001, 0x8000000080008081, 0x8000000000008009,
								0x000000000000008A, 0x0000000000000088, 0x0000000080008009, 0x000000008000000A,
								0x000000008000808B, 0x800000000000008B, 0x8000000000008089, 0x8000000000008003,
								0x8000000000008002, 0x8000000000000080, 0x000000000000800A, 0x800000008000000A,
								0x8000000080008081, 0x8000000000008080, 0x0000000080000001, 0x8000000080008008, ]

		self.rotation_constants = [0, 1, 62, 28, 27, 36, 44, 6, 55, 20, 3, 10, 43, 25, 39, 41, 45, 15, 21, 8, 18, 2, 61, 56, 14]
		self.column_size = 5
		self.word_size = 64
		self.rounds = 12 + (2 * int(math.log(self.word_size, 2)))
		self.version = version
		self.output_size = (version * 2) // self.word_size
		self.block_size = (self.column_size * self.column_size) - self.output_size

		self.buffers = [0x00 for x in range(self.column_size * self.column_size)]

		if message_delimiter == None:
			self.message_delimiter = 0x06
		else:
			self.message_delimiter = message_delimiter
			self.version = version * 2
			
	def _set_message(self, message):
		byte_message = bytearray(message)
		input_length_data = len(byte_message)
		byte_message.append(self.message_delimiter)

		while len(byte_message) % (self.block_size * self.word_size // 8) != 0:
			byte_message.append(0x00)

		byte_message[-1] = 0x80

		return byte_message

	def __theta(self, buffers):
		parity_column = []

		for index in range(self.column_size):
			parity_column.append(buffers[index] ^ buffers[index + self.column_size] ^
								 buffers[index + 2 * self.column_size] ^ buffers[index + 3 * self.column_size] ^
								 buffers[index + 4 * self.column_size])

		for index in range(len(buffers)):
			column_index = index % self.column_size

			prev_parity_rot = shift_rotate_left(parity_column[(column_index + 1) % self.column_size], 1,
												 self.word_size)

			buffers[index] ^= parity_column[(column_index - 1) % self.column_size] ^ prev_parity_rot

		return buffers

	def __rho_phi(self, buffers):
		backup_buffer = buffers[:]

		for index in range(self.column_size * self.column_size):
			x = index % self.column_size
			y = index // self.column_size
			new_phi_index = y + (((2 * x) + (3 * y)) % self.column_size) * self.column_size

			backup_buffer[new_phi_index] = shift_rotate_left(buffers[index], self.rotation_constants[index],
															  self.word_size)

		return backup_buffer

	def __chi(self, buffers):
		backup_buffer = buffers[:]

		for index in range(self.column_size * self.column_size):
			x = index % self.column_size
			new_index1 = (index - x) + ((x + 1) % self.column_size)
			new_index2 = (index - x) + ((x + 2) % self.column_size)

			backup_buffer[index] ^= bit_not(buffers[new_index1], self.word_size) & buffers[new_index2]

		return backup_buffer

	def _hash_message_chunk(self, chunk):
		temp_buffers = self.buffers[:]

		for index in range(len(chunk)):
			temp_buffers[index] ^= chunk[index]

		for round_itteration in range(self.rounds):
			temp_buffers = self.__theta(temp_buffers)
	
			temp_buffers[0] ^= asint(self.round_constants[round_itteration], self.word_size)

		self.buffers = temp_buffers

	def hash(self, message):
		byte_message = self._set_message(message)

		for chunk in to_blocks(byte_message, (self.block_size * self.word_size // 8), ):
			self._hash_message_chunk(bytes_to_intarray(chunk, (self.word_size // 8)))

		output = b""
		for x in self.buffers:
			output += (x).to_bytes((self.word_size // 8), byteorder='little')

		return output[:(self.version // 8)]

	def hash_digest(self, message):
		return self.hash(message).hex()


# HMAC

def hmac(key, message, hash_function):
	block_size = getattr(hash_function(), 'block_size')

	if len(key) > block_size:
		key = hash_function(key).digest()

	if len(key) < block_size:
		key = key + b"\x00" * (block_size - len(key))

	o_key = fixedlen_xor(key, b"\x5c" * block_size)
	i_key = fixedlen_xor(key, b"\x36" * block_size)

	tmp = hash_function(i_key + message)

	return hash_function(o_key + tmp.digest()).digest()