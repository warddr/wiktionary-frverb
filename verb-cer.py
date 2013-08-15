#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

### auteur: Ward De Ridder
### bedoeling: regelmatige werkwoorden op -cer vervoegen in het Frans

werkwoord = input("Werkwoord: ")
#werkwoord = developper
stam = werkwoord[:-3]

FILE = open(werkwoord+".txt","w",encoding='utf-8')


begin = "{{-start-}}\n"
eind = "\n{{-stop-}}\n"

basis = "\n{{=fra=}}\n{{-verb-|0}}\n"
fraverbform = "{{fra-verb-form|"+werkwoord+"|"
fradeelwoord = "{{fra-deelwoord|"+werkwoord+"|"

#-a
FILE.write(begin + "'''" + stam + "ça" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=3|num=s|temp=ps}}")
FILE.write(eind)

#-ai
FILE.write(begin + "'''" + stam + "çai" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=1|num=s|temp=ps}}")
FILE.write(eind)

#-aient
FILE.write(begin + "'''" + stam + "çaient" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=3|num=p|temp=imp}}")
FILE.write(eind)

#-ais
FILE.write(begin + "'''" + stam + "çais" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=12|num=s|temp=imp}}")
FILE.write(eind)

#-ait
FILE.write(begin + "'''" + stam + "çait" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=3|num=s|temp=imp}}")
FILE.write(eind)

#-ant
FILE.write(begin + "'''" + stam + "çant" + "'''")
FILE.write(basis)
FILE.write(fradeelwoord+"temp=t}}")
FILE.write(eind)

#-as
FILE.write(begin + "'''" + stam + "ças" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=2|num=s|temp=ps}}")
FILE.write(eind)

#-asse
FILE.write(begin + "'''" + stam + "çasse" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=1|num=s|temp=simp}}")
FILE.write(eind)

#-assent
FILE.write(begin + "'''" + stam + "çassent" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=3|num=p|temp=simp}}")
FILE.write(eind)

#-asses
FILE.write(begin + "'''" + stam + "çasses" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=2|num=s|temp=simp}}")
FILE.write(eind)

#-assiez
FILE.write(begin + "'''" + stam + "çassiez" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=2|num=p|temp=simp}}")
FILE.write(eind)

#-assions
FILE.write(begin + "'''" + stam + "çassions" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=1|num=p|temp=simp}}")
FILE.write(eind)

#-e
FILE.write(begin + "'''" + stam + "ce" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=13|num=s|temp=ip}}"+fraverbform+"pers=13|num=s|temp=sp|nohead=1}}"+fraverbform+"pers=2|num=s|temp=impp|nohead=1}}")
FILE.write(eind)

#-ent
FILE.write(begin + "'''" + stam + "cent" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=3|num=p|temp=ip}}"+fraverbform+"pers=3|num=p|temp=sp|nohead=1}}")
FILE.write(eind)

#-era
FILE.write(begin + "'''" + stam + "cera" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=3|num=s|temp=fs}}")
FILE.write(eind)

#-erai
FILE.write(begin + "'''" + stam + "cerai" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=1|num=s|temp=fs}}")
FILE.write(eind)

#-eraient
FILE.write(begin + "'''" + stam + "ceraient" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=3|num=p|temp=cp}}")
FILE.write(eind)

#-erais
FILE.write(begin + "'''" + stam + "cerais" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=12|num=s|temp=cp}}")
FILE.write(eind)

#-erait
FILE.write(begin + "'''" + stam + "cerait" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=3|num=s|temp=cp}}")
FILE.write(eind)

#-eras
FILE.write(begin + "'''" + stam + "ceras" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=2|num=s|temp=fs}}")
FILE.write(eind)

#-erez
FILE.write(begin + "'''" + stam + "cerez" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=2|num=p|temp=fs}}")
FILE.write(eind)

#-eriez
FILE.write(begin + "'''" + stam + "ceriez" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=2|num=p|temp=cp}}")
FILE.write(eind)

#-erions
FILE.write(begin + "'''" + stam + "cerions" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=1|num=p|temp=cp}}")
FILE.write(eind)

#-erons
FILE.write(begin + "'''" + stam + "cerons" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=1|num=p|temp=fs}}")
FILE.write(eind)

#-eront
FILE.write(begin + "'''" + stam + "ceront" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=3|num=p|temp=fs}}")
FILE.write(eind)

#-es
FILE.write(begin + "'''" + stam + "ces" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=2|num=s|temp=ip}}"+fraverbform+"pers=2|num=s|temp=sp|nohead=1}}")
FILE.write(eind)

#-ez
FILE.write(begin + "'''" + stam + "cez" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=2|num=p|temp=ip}}"+fraverbform+"pers=2|num=p|temp=impp|nohead=1}}")
FILE.write(eind)

#-iez
FILE.write(begin + "'''" + stam + "ciez" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=2|num=p|temp=imp}}"+fraverbform+"pers=2|num=p|temp=sp|nohead=1}}")
FILE.write(eind)

#-ions
FILE.write(begin + "'''" + stam + "cions" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=1|num=p|temp=imp}}"+fraverbform+"pers=1|num=p|temp=sp|nohead=1}}")
FILE.write(eind)

#-ons
FILE.write(begin + "'''" + stam + "çons" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=1|num=p|temp=ip}}"+fraverbform+"pers=1|num=p|temp=impp|nohead=1}}")
FILE.write(eind)

#-âmes
FILE.write(begin + "'''" + stam + "çâmes" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=1|num=p|temp=ps}}")
FILE.write(eind)

#-ât
FILE.write(begin + "'''" + stam + "çât" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=3|num=s|temp=simp}}")
FILE.write(eind)

#-âtes
FILE.write(begin + "'''" + stam + "çâtes" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=2|num=p|temp=ps}}")
FILE.write(eind)

#-èrent
FILE.write(begin + "'''" + stam + "cèrent" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=3|num=p|temp=ps}}")
FILE.write(eind)

#-é
FILE.write(begin + "'''" + stam + "cé" + "'''")
FILE.write(basis)
FILE.write(fradeelwoord+"temp=v}}")
FILE.write(eind)

#-ée
FILE.write(begin + "'''" + stam + "cée" + "'''")
FILE.write(basis)
FILE.write(fradeelwoord+"gesl=f|num=s|temp=v}}")
FILE.write(eind)

#-ées
FILE.write(begin + "'''" + stam + "cées" + "'''")
FILE.write(basis)
FILE.write(fradeelwoord+"gesl=f|num=p|temp=v}}")
FILE.write(eind)

#-és
FILE.write(begin + "'''" + stam + "cés" + "'''")
FILE.write(basis)
FILE.write(fradeelwoord+"gesl=m|num=p|temp=v}}")
FILE.write(eind)


