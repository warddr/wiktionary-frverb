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
FILE.write(begin + "'''" + stam + "gea" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=3|num=s|temp=ps}}")
FILE.write(eind)

#-ai
FILE.write(begin + "'''" + stam + "geai" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=1|num=s|temp=ps}}")
FILE.write(eind)

#-aient
FILE.write(begin + "'''" + stam + "geaient" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=3|num=p|temp=imp}}")
FILE.write(eind)

#-ais
FILE.write(begin + "'''" + stam + "geais" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=12|num=s|temp=imp}}")
FILE.write(eind)

#-ait
FILE.write(begin + "'''" + stam + "geait" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=3|num=s|temp=imp}}")
FILE.write(eind)

#-ant
FILE.write(begin + "'''" + stam + "geant" + "'''")
FILE.write(basis)
FILE.write(fradeelwoord+"temp=t}}")
FILE.write(eind)

#-as
FILE.write(begin + "'''" + stam + "geas" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=2|num=s|temp=ps}}")
FILE.write(eind)

#-asse
FILE.write(begin + "'''" + stam + "geasse" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=1|num=s|temp=simp}}")
FILE.write(eind)

#-assent
FILE.write(begin + "'''" + stam + "geassent" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=3|num=p|temp=simp}}")
FILE.write(eind)

#-asses
FILE.write(begin + "'''" + stam + "geasses" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=2|num=s|temp=simp}}")
FILE.write(eind)

#-assiez
FILE.write(begin + "'''" + stam + "geassiez" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=2|num=p|temp=simp}}")
FILE.write(eind)

#-assions
FILE.write(begin + "'''" + stam + "geassions" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=1|num=p|temp=simp}}")
FILE.write(eind)

#-e
FILE.write(begin + "'''" + stam + "ge" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=13|num=s|temp=ip}}"+fraverbform+"pers=13|num=s|temp=sp|nohead=1}}"+fraverbform+"pers=2|num=s|temp=impp|nohead=1}}")
FILE.write(eind)

#-ent
FILE.write(begin + "'''" + stam + "gent" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=3|num=p|temp=ip}}"+fraverbform+"pers=3|num=p|temp=sp|nohead=1}}")
FILE.write(eind)

#-era
FILE.write(begin + "'''" + stam + "gera" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=3|num=s|temp=fs}}")
FILE.write(eind)

#-erai
FILE.write(begin + "'''" + stam + "gerai" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=1|num=s|temp=fs}}")
FILE.write(eind)

#-eraient
FILE.write(begin + "'''" + stam + "geraient" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=3|num=p|temp=cp}}")
FILE.write(eind)

#-erais
FILE.write(begin + "'''" + stam + "gerais" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=12|num=s|temp=cp}}")
FILE.write(eind)

#-erait
FILE.write(begin + "'''" + stam + "gerait" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=3|num=s|temp=cp}}")
FILE.write(eind)

#-eras
FILE.write(begin + "'''" + stam + "geras" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=2|num=s|temp=fs}}")
FILE.write(eind)

#-erez
FILE.write(begin + "'''" + stam + "gerez" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=2|num=p|temp=fs}}")
FILE.write(eind)

#-eriez
FILE.write(begin + "'''" + stam + "geriez" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=2|num=p|temp=cp}}")
FILE.write(eind)

#-erions
FILE.write(begin + "'''" + stam + "gerions" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=1|num=p|temp=cp}}")
FILE.write(eind)

#-erons
FILE.write(begin + "'''" + stam + "gerons" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=1|num=p|temp=fs}}")
FILE.write(eind)

#-eront
FILE.write(begin + "'''" + stam + "geront" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=3|num=p|temp=fs}}")
FILE.write(eind)

#-es
FILE.write(begin + "'''" + stam + "ges" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=2|num=s|temp=ip}}"+fraverbform+"pers=2|num=s|temp=sp|nohead=1}}")
FILE.write(eind)

#-ez
FILE.write(begin + "'''" + stam + "gez" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=2|num=p|temp=ip}}"+fraverbform+"pers=2|num=p|temp=impp|nohead=1}}")
FILE.write(eind)

#-iez
FILE.write(begin + "'''" + stam + "giez" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=2|num=p|temp=imp}}"+fraverbform+"pers=2|num=p|temp=sp|nohead=1}}")
FILE.write(eind)

#-ions
FILE.write(begin + "'''" + stam + "gions" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=1|num=p|temp=imp}}"+fraverbform+"pers=1|num=p|temp=sp|nohead=1}}")
FILE.write(eind)

#-ons
FILE.write(begin + "'''" + stam + "geons" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=1|num=p|temp=ip}}"+fraverbform+"pers=1|num=p|temp=impp|nohead=1}}")
FILE.write(eind)

#-âmes
FILE.write(begin + "'''" + stam + "geâmes" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=1|num=p|temp=ps}}")
FILE.write(eind)

#-ât
FILE.write(begin + "'''" + stam + "geât" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=3|num=s|temp=simp}}")
FILE.write(eind)

#-âtes
FILE.write(begin + "'''" + stam + "geâtes" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=2|num=p|temp=ps}}")
FILE.write(eind)

#-èrent
FILE.write(begin + "'''" + stam + "gèrent" + "'''")
FILE.write(basis)
FILE.write(fraverbform+"pers=3|num=p|temp=ps}}")
FILE.write(eind)

#-é
FILE.write(begin + "'''" + stam + "gé" + "'''")
FILE.write(basis)
FILE.write(fradeelwoord+"temp=v}}")
FILE.write(eind)

#-ée
FILE.write(begin + "'''" + stam + "gée" + "'''")
FILE.write(basis)
FILE.write(fradeelwoord+"gesl=f|num=s|temp=v}}")
FILE.write(eind)

#-ées
FILE.write(begin + "'''" + stam + "gées" + "'''")
FILE.write(basis)
FILE.write(fradeelwoord+"gesl=f|num=p|temp=v}}")
FILE.write(eind)

#-és
FILE.write(begin + "'''" + stam + "gés" + "'''")
FILE.write(basis)
FILE.write(fradeelwoord+"gesl=m|num=p|temp=v}}")
FILE.write(eind)


