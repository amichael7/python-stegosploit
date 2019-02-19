#!/usr/bin/env python3

'''
Creates and HTML+JPG polyglot for Internet Explorer
'''

import argparse
import re

RANDOM_DATA_SIZE = 1900

STEGO = """
                                  .       .
                                 / `.   .' \\
                         .---.  <    > <    >  .---.
                         |    \\  \\ - ~ ~ - /  /    |
                          ~-..-~             ~-..-~
                      \\~~~\\.'   stegosploit      `./~~~/
                       \\__/                imajs   \\__/
                         /  .    -.                 \\
                  \\~~~\\/   {       \\       .-~ ~-.    -._ _._
                   \\__/    :        }     {       \\     ~{  p'-._
    .     .   |~~. .'       \\       }      \\       )      \\  ~--'}
    \\\\   //   `-..'       _ -\\      |      _\\      )__.-~~'='''''
 `-._\\\\_//__..-'      .-~    |\\.    }~~--~~  \\=   / \\
  ``~---.._ _ _ . - ~        ) /=  /         /+  /   }
                            /_/   /         {   } |  |
                              `~---o.       `~___o.---'
"""

def main():
	print(STEGO)	# print the stego

	description = 'Creates and HTML+JPG polyglot for Internet Explorer.'
	parser = argparse.ArgumentParser(description = description)
	parser.add_argument('htmlfile', 
			type=argparse.FileType('r'),
			nargs='?',					# REMOVE ME
			help='HTML file name')

	parser.add_argument('jpgfile', 
			type=argparse.FileType('rb'),
			nargs='?',					# REMOVE ME
			help='JPG file name')

	parser.add_argument('output', 
			type=argparse.FileType('wb'),
			nargs='?',					# REMOVE ME
			help='Output file name')
	args = parser.parse_args()

	htmlData = 'hello'		# FIXME
	if args.htmlfile:
		htmlData = args.htmlfile.read()
		htmlData = htmlData.rstrip()	# remove trailing whitespace

	jpgData = open('anon.jpg','rb').read()	# FIXME
	if args.jpgfile:
		jpgData = args.jpgfile.read()

	jpgStart = jpgData[:4]		# read the first 4 bytes (Magic # = 0xFFD8FFE0)
	jfifapp0 = jpgData[6:20]	# from JFIF to offset 20
	restOfJpg = jpgData[20:]	# read the rest of the file

	jpgData = None	# remove jpgData from cache for performance

	# print('',jpgStart,'\n',jfifapp0,'\n',restOfJpg)

	html = '<html><!--'
	content = ' -->'

	# remove <html>,<head> and <meta http-equiv ...> tags
	# from the html
	htmlTags = re.compile('<html>')
	headTags = re.compile('<head>')
	metaTags = re.compile('<meta http-equiv[^>]*>')

	htmlData = re.sub(htmlTags,'',htmlData)
	htmlData = re.sub(headTags,'',htmlData)
	htmlData = re.sub(metaTags,'',htmlData)

	content += htmlData + '<!--'

	##################################
	##		BOOKMARK LINE 94		##
	##################################

if __name__ == '__main__':
	main()