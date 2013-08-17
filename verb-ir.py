#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

### auteur: Ward De Ridder
### bedoeling: regelmatige werkwoorden op -ir vervoegen in het Frans

werkwoord = input("Werkwoord: ")

stam = werkwoord[:-2]

FILE = open(werkwoord+".txt","w",encoding='utf-8')


begin = "{{-start-}}\n"
eind = "\n{{-stop-}}\n"

basis = "\n{{=fra=}}\n{{-verb-|0}}\n"
fraverbform = "{{fra-verb-form|"+werkwoord+"|"
fradeelwoord = "{{fra-deelwoord|"+werkwoord+"|"

#-is
FILE.write(begin + "'''" + stam + "is" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=12|num=s|temp=ip}}"+fraverbform+"pers=12|num=s|temp=ps|nohead=1}}"+fraverbform+"pers=2|num=s|temp=impp|nohead=1}}"+fradeelwoord+"temp=v|num=p|gesl=m|nohead=1}}")
FILE.write(eind)

#-it
FILE.write(begin + "'''" + stam + "it" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=3|num=s|temp=ip}}"+fraverbform+"pers=3|num=s|temp=ps|nohead=1}}")
FILE.write(eind)

#-issons
FILE.write(begin + "'''" + stam + "issons" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=1|num=p|temp=ip}}"+fraverbform+"pers=1|num=p|temp=impp|nohead=1}}")
FILE.write(eind)

#-issez
FILE.write(begin + "'''" + stam + "issez" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=2|num=p|temp=ip}}"+fraverbform+"pers=2|num=p|temp=impp|nohead=1}}")
FILE.write(eind)

#-issent
FILE.write(begin + "'''" + stam + "issent" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=3|num=p|temp=ip}}"+fraverbform+"pers=3|num=p|temp=simp|nohead=1}}"+fraverbform+"pers=3|num=p|temp=sp|nohead=1}}")
FILE.write(eind)

#-issais
FILE.write(begin + "'''" + stam + "issais" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=12|num=s|temp=imp}}")
FILE.write(eind)

#-issait
FILE.write(begin + "'''" + stam + "issait" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=3|num=s|temp=imp}}")
FILE.write(eind)

#-issions
FILE.write(begin + "'''" + stam + "issions" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=1|num=p|temp=imp}}"+fraverbform+"pers=1|num=p|temp=sp|nohead=1}}"+fraverbform+"pers=1|num=p|temp=simp|nohead=1}}")
FILE.write(eind)

#-issiez
FILE.write(begin + "'''" + stam + "issiez" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=2|num=p|temp=imp}}"+fraverbform+"pers=2|num=p|temp=sp|nohead=1}}"+fraverbform+"pers=2|num=p|temp=simp|nohead=1}}")
FILE.write(eind)

#-issaient
FILE.write(begin + "'''" + stam + "issaient" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=3|num=p|temp=imp}}")
FILE.write(eind)

#-îmes
FILE.write(begin + "'''" + stam + "îmes" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=1|num=p|temp=ps}}")
FILE.write(eind)

#-îtes
FILE.write(begin + "'''" + stam + "îtes" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=2|num=p|temp=ps}}")
FILE.write(eind)

#-irent
FILE.write(begin + "'''" + stam + "irent" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=3|num=p|temp=ps}}")
FILE.write(eind)

#-irai
FILE.write(begin + "'''" + stam + "irai" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=1|num=s|temp=fs}}")
FILE.write(eind)

#-iras
FILE.write(begin + "'''" + stam + "iras" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=2|num=s|temp=fs}}")
FILE.write(eind)

#-ira
FILE.write(begin + "'''" + stam + "ira" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=3|num=s|temp=fs}}")
FILE.write(eind)

#-irons
FILE.write(begin + "'''" + stam + "irons" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=1|num=p|temp=fs}}")
FILE.write(eind)

#-irez
FILE.write(begin + "'''" + stam + "irez" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=2|num=p|temp=fs}}")
FILE.write(eind)

#-iront
FILE.write(begin + "'''" + stam + "iront" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=3|num=p|temp=fs}}")
FILE.write(eind)

#-isse
FILE.write(begin + "'''" + stam + "isse" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=13|num=s|temp=sp}}"+fraverbform+"pers=1|num=s|temp=simp|nohead=1}}")
FILE.write(eind)

#-isses
FILE.write(begin + "'''" + stam + "isses" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=2|num=s|temp=sp}}"+fraverbform+"pers=2|num=s|temp=simp|nohead=1}}")
FILE.write(eind)

#-ît
FILE.write(begin + "'''" + stam + "ît" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=3|num=s|temp=simp}}")
FILE.write(eind)

#-irais
FILE.write(begin + "'''" + stam + "irais" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=12|num=s|temp=cp}}")
FILE.write(eind)

#-irait
FILE.write(begin + "'''" + stam + "irait" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=3|num=s|temp=cp}}")
FILE.write(eind)

#-irions
FILE.write(begin + "'''" + stam + "irions" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=1|num=p|temp=cp}}")
FILE.write(eind)

#-iriez
FILE.write(begin + "'''" + stam + "iriez" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=2|num=p|temp=cp}}")
FILE.write(eind)

#-iraient
FILE.write(begin + "'''" + stam + "iraient" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=3|num=p|temp=cp}}")
FILE.write(eind)

#-issant
FILE.write(begin + "'''" + stam + "issant" + "'''")
FILE.write(basis)
FILE.write(fradeelwoord+"temp=t}}")
FILE.write(eind)

#-i
FILE.write(begin + "'''" + stam + "i" + "'''")
FILE.write(basis)
FILE.write(fradeelwoord+"temp=v}}")
FILE.write(eind)

#-ie
FILE.write(begin + "'''" + stam + "ie" + "'''")
FILE.write(basis)
FILE.write(fradeelwoord+"temp=v|num=s|gesl=f}}")
FILE.write(eind)

#-ies
FILE.write(begin + "'''" + stam + "ies" + "'''")
FILE.write(basis)
FILE.write(fradeelwoord+"temp=v|num=p|gesl=f}}")
FILE.write(eind)
