#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

### auteur: Ward De Ridder
### bedoeling: regelmatige werkwoorden op -er (let op voor -ger, die zit hier niet in) vervoegen in het Frans

werkwoord = input("Werkwoord: ")
#werkwoord = developper
stam = werkwoord[:-2]

FILE = open(werkwoord+".txt","w",encoding='utf-8')


begin = "{{-start-}}\n"
eind = "\n{{-stop-}}\n"

basis = "\n{{=fra=}}\n{{-verb-|0}}\n"
fraverbform = "{{fra-verb-form|"+werkwoord+"|"
fradeelwoord = "{{fra-deelwoord|"+werkwoord+"|"

#-a
FILE.write(begin + "'''" + stam + "a" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=3|num=s|temp=ps}}")
FILE.write(eind)

#-ai
FILE.write(begin + "'''" + stam + "ai" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=1|num=s|temp=ps}}")
FILE.write(eind)

#-aient
FILE.write(begin + "'''" + stam + "aient" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=3|num=p|temp=imp}}")
FILE.write(eind)

#-ais
FILE.write(begin + "'''" + stam + "ais" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=12|num=s|temp=imp}}")
FILE.write(eind)

#-ait
FILE.write(begin + "'''" + stam + "ait" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=3|num=s|temp=imp}}")
FILE.write(eind)

#-ant
FILE.write(begin + "'''" + stam + "ant" + "'''")
FILE.write(basis)
FILE.write(fradeelwoord+"temp=t}}")
FILE.write(eind)

#-as
FILE.write(begin + "'''" + stam + "as" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=2|num=s|temp=ps}}")
FILE.write(eind)

#-asse
FILE.write(begin + "'''" + stam + "asse" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=1|num=s|temp=simp}}")
FILE.write(eind)

#-assent
FILE.write(begin + "'''" + stam + "assent" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=3|num=p|temp=simp}}")
FILE.write(eind)

#-asses
FILE.write(begin + "'''" + stam + "asses" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=2|num=s|temp=simp}}")
FILE.write(eind)

#-assiez
FILE.write(begin + "'''" + stam + "assiez" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=2|num=p|temp=simp}}")
FILE.write(eind)

#-assions
FILE.write(begin + "'''" + stam + "assions" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=1|num=p|temp=simp}}")
FILE.write(eind)

#-e
FILE.write(begin + "'''" + stam + "e" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=13|num=s|temp=ip}}"+fraverbform+"pers=13|num=s|temp=sp|nohead=1}}"+fraverbform+"pers=2|num=s|temp=impp|nohead=1}}")
FILE.write(eind)

#-ent
FILE.write(begin + "'''" + stam + "ent" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=3|num=p|temp=ip}}"+fraverbform+"pers=3|num=p|temp=sp|nohead=1}}")
FILE.write(eind)

#-era
FILE.write(begin + "'''" + stam + "era" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=3|num=s|temp=fs}}")
FILE.write(eind)

#-erai
FILE.write(begin + "'''" + stam + "erai" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=1|num=s|temp=fs}}")
FILE.write(eind)

#-eraient
FILE.write(begin + "'''" + stam + "eraient" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=3|num=p|temp=cp}}")
FILE.write(eind)

#-erais
FILE.write(begin + "'''" + stam + "erais" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=12|num=s|temp=cp}}")
FILE.write(eind)

#-erait
FILE.write(begin + "'''" + stam + "erait" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=3|num=s|temp=cp}}")
FILE.write(eind)

#-eras
FILE.write(begin + "'''" + stam + "eras" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=2|num=s|temp=fs}}")
FILE.write(eind)

#-erez
FILE.write(begin + "'''" + stam + "erez" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=2|num=p|temp=fs}}")
FILE.write(eind)

#-eriez
FILE.write(begin + "'''" + stam + "eriez" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=2|num=p|temp=cp}}")
FILE.write(eind)

#-erions
FILE.write(begin + "'''" + stam + "erions" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=1|num=p|temp=cp}}")
FILE.write(eind)

#-erons
FILE.write(begin + "'''" + stam + "erons" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=1|num=p|temp=fs}}")
FILE.write(eind)

#-eront
FILE.write(begin + "'''" + stam + "eront" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=3|num=p|temp=fs}}")
FILE.write(eind)

#-es
FILE.write(begin + "'''" + stam + "es" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=2|num=s|temp=ip}}"+fraverbform+"pers=2|num=s|temp=sp|nohead=1}}")
FILE.write(eind)

#-ez
FILE.write(begin + "'''" + stam + "ez" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=2|num=p|temp=ip}}"+fraverbform+"pers=2|num=p|temp=impp|nohead=1}}")
FILE.write(eind)

#-iez
FILE.write(begin + "'''" + stam + "iez" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=2|num=p|temp=imp}}"+fraverbform+"pers=2|num=p|temp=sp|nohead=1}}")
FILE.write(eind)

#-ions
FILE.write(begin + "'''" + stam + "ions" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=1|num=p|temp=imp}}"+fraverbform+"pers=1|num=p|temp=sp|nohead=1}}")
FILE.write(eind)

#-ons
FILE.write(begin + "'''" + stam + "ons" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=1|num=p|temp=ip}}"+fraverbform+"pers=1|num=p|temp=impp|nohead=1}}")
FILE.write(eind)

#-âmes
FILE.write(begin + "'''" + stam + "âmes" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=1|num=p|temp=ps}}")
FILE.write(eind)

#-ât
FILE.write(begin + "'''" + stam + "ât" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=3|num=s|temp=simp}}")
FILE.write(eind)

#-âtes
FILE.write(begin + "'''" + stam + "âtes" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=2|num=p|temp=ps}}")
FILE.write(eind)

#-èrent
FILE.write(begin + "'''" + stam + "èrent" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=3|num=p|temp=ps}}")
FILE.write(eind)

#-é
FILE.write(begin + "'''" + stam + "é" + "'''")
FILE.write(basis)
FILE.write(fradeelwoord+"temp=v}}")
FILE.write(eind)

#-ée
FILE.write(begin + "'''" + stam + "ée" + "'''")
FILE.write(basis)
FILE.write(fradeelwoord+"gesl=f|num=s|temp=v}}")
FILE.write(eind)

#-ées
FILE.write(begin + "'''" + stam + "ées" + "'''")
FILE.write(basis)
FILE.write(fradeelwoord+"gesl=f|num=p|temp=v}}")
FILE.write(eind)

#-és
FILE.write(begin + "'''" + stam + "és" + "'''")
FILE.write(basis)
FILE.write(fradeelwoord+"gesl=m|num=p|temp=v}}")
FILE.write(eind)


