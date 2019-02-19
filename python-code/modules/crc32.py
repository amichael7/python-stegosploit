#!/usr/bin/env python3

# use CRC32;
# 
# my $data = 'Hello World';
# 
# CRC32::clear();
# CRC32::add(\$data);
# 
# my $check_value = CRC32::result();
# 
# printf("Check value (in hex): %x\n", $check_value);
#
# Reference
# http://www.dispersiondesign.com/articles/graphics/png_crc32_calculations


'''
Instead of rolling our own CRC32 generator, we
will be using the zlib version

Usage:

crc32 = CRC32()
crc32.add(data)

checkValue = crc32.result()
'''

# import zlib
import binascii

class CRC32:
	def __init__(self):
		self.crc = None

	def add(self, data):
		# Normalize data to bytes
		data = str(data).encode()

		# evaluate the CRC32 checksum
		if self.crc != None:
			self.crc = binascii.crc32(data, self.crc)
		else:
			self.crc = binascii.crc32(data)

		return True

	def result(self):
		return self.crc

def main():
	crc32 = CRC32()

	crc32.add('hello world')
	crc = crc32.result()
	print(crc)
	# print('crc32 = {:#010x}'.format(crc))

if __name__ == '__main__':
	main()