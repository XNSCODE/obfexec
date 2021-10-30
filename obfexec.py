#!usr/bin/python

import sys,codecs, random, os

def main():
	os.system("clear")
	try:
		data = []
		file = input("\n [+] Nama File > ")
		out = input(" [+] Output File > ")
		s = open(file).read()
		for i in s:
			data.append(ord(i))
			d = open(out, 'w')
			d.write(f"exec(''.join(chr(_) for _ in {data}))")
			d.close()
		print ("\n [+] File Berhasil Di Encrypt")
		print(f" [+] Nama File > {out}")
		print("")
	except:
		pass

main()
