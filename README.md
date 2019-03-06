# python-stegosploit

## How Stegosploit Works

The exploit code is inserted within the pixels of the image so that the image contains the exploit code.  IMAJS then creates a polyglot image that will be read as an image and contains a decoder that will extract and run the javascript exploit.

The exploit that we will use is an Internet Explorer Use-after-free exploit ([CVE-2014-0282](https://nvd.nist.gov/vuln/detail/CVE-2014-0282)).

## What we have done so far

__Highlights:__

* The server can serve images to the VM over `10.0.2.2:5000`
* The jpg.py program can build a polyglot file (valid `.html` and `.jpg`)

## Checklist

- [X] Refactor `CRC32.pm`
- [X] Refactor `PNGDATA.pm`
- [ ] Refactor `html_in_jpg_ie.pl`
- [X] Refactor `pngenum.pl`

- [ ] Demo Server
	- [X] Move all static exploit files in demo pages to `/static`
	- [ ] Make sure all static files are passed parsed using `template_render`
	- [ ] Add an image picker for the image_layer_analysis.html \(Optional\)

## References

* https://conference.hitb.org/hitbsecconf2015ams/sessions/stegosploit-hacking-with-pictures/
* https://www.vulnerability-db.com/?q=articles/2015/06/17/exploit-delivery-steganography-using-stegosploit-tool-v02
* https://www.blackhat.com/docs/eu-15/materials/eu-15-Shah-Stegosploit-Exploit-Delivery-With-Steganography-And-Polyglots.pdf
* https://stackoverflow.com/questions/4110964/how-does-heap-spray-attack-work
* https://www.youtube.com/watch?time_continue=1&v=6lYUtIZHlJA
* https://www.owasp.org/images/0/01/OWASL_IL_2010_Jan_-_Moshe_Ben_Abu_-_Advanced_Heapspray.pdf
* https://en.wikipedia.org/wiki/Heap_spraying
* https://developer.microsoft.com/en-us/microsoft-edge/tools/vms/