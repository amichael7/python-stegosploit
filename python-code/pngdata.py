'''
program: pngdata.py

Description: A port of the PNGDATA.pm module
'''

import binascii
from modules.crc32 import CRC32

class PNG:
	'''
	Function to read PNG file in chunks and create
	a PNG array

	Input: entire png file
	Output: array of png chunks
	'''
	def read(data):
		pngChunks = []

		header = PNG.getHeader(data)
		pngChunks.append(header)
		data = data[8:]  # remove header bytes from data

		while len(data) > 0:
			length 		= int.from_bytes(data[0:4], byteorder='big')		# 4 bytes
			chunkType 	= data[4:8]
			chunkData	= data[8:length+8]
			crc 		= data[length+8:length+12]

			chunk = [length, chunkType, chunkData, crc]
			pngChunks.append(chunk)

			chunkSize = 12+length
			data = data[chunkSize:]		# remove the chunk from data

		return pngChunks

	'''
	Get the PNG header
	'''
	def getHeader(data):
		return data[:8]		# PNGs contain an 8-byte header

	def printHeader(header):
		# Check if the header matches the magic numbers
		status = 'OK!'
		if header != b'\x89PNG\r\n\x1a\n':
			status = 'Error'

		print('PNG Header: %s - %s' % (header, status))

	##########################
	##		BROKEN			##
	##########################
	'''
	Function to print a png chunk

	Input: PNG chunk
		format: [length, chunkType, chunkData, crc]
	Output: Nothing
	'''
	def printChunk(chunk):
		length 		= chunk[0]		# stored as int
		chunkType 	= chunk[1]
		chunkData 	= chunk[2]
		crc 		= int.from_bytes(chunk[3], byteorder='little')		# stored as int

		crc32 = CRC32()
		crc32.add(chunkData)
		computedCrc = crc32.result()

		print(crc)
		print(computedCrc)

		status = 'OK'
		if computedCrc != crc:
			status = 'Error'

		print('%s %d bytes CRC: 0x%08x (computed 0x%08x) - %s)' (chunkType, length, crc, status))

def main():
	with open('anon.png', 'rb') as file:
		data=file.read()

		header = PNG.getHeader(data)
		PNG.printHeader(header)

		chunks = PNG.read(data)
		print(chunks[1])
		PNG.printChunk(chunks[1])


if __name__ == '__main__':
	main()