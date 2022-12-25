# Naloge

## 1. IZGUBLJENA PISMA BOŽIČKU

1. https://hekaton.mojedelo.com/hekaton/bozicni-it-hekaton/naloga_1/
2. >Težave v Božičkovem informacijskem sistemu.
3. > Božiček je to leto svojim IT palčkom naročil naj izdelajo informacijski sistem v katerega se shranjujejo vsa pisma želja otrok. Da bo imel lažji pregled katera darila bodo morali njegovi palčki ustvariti za otroke.
   >
   > Po več urnem sestanku so IT palčki prišli do naslednje rešitve. Odločili so se, da bodo izdelali sistem, ki bo skeniral vsa poslana sporočila in jih shranil v podatkovno bazo.
   >
   > Podatkovna baza ima dva stolpca. Prvi je Id datoteke, ki je unikaten, drugi pa pot do datoteke. Id je tipa CHAR(32), generira pa se na podlagi izračunane MD5 hash vrednosti datoteke, ki je bila skenirana.
   >
   >Dan pred božičem, so IT palčki za vsak slučaj prešteli vsa pisma, ki so jih skenirali in pa prešteli vse stolpce v bazi. Opazili so, da je število sporočil v podatkovni bazi manjše kot pa število pisem, ki so jih prejeli. Težava je definitivno v informacijskem sistemu, ki so ga naredili, saj so bila skenirana vsa sporočila.
   >
   > Ali lahko ugotoviš kako se imenuje težava do katere je prišlo? (odgovori v angleškem jeziku)
4. https://en.wikipedia.org/wiki/Hash_collision
5. `hash collision`

## 2. SLIKA

1. https://hekaton.mojedelo.com/hekaton/bozicni-it-hekaton/naloga_2/
2. >Božiček je prejel sliko in ne ve kaj bi z njo.
3. > Božiček je dobil sporočilo, v katerem piše, da se njegovo pismo nahaja v sliki ssrd/its-xmas-time. Sam ne ve, kaj to je. Mu lahko pomagaš?
4. https://hub.docker.com/r/ssrd/its-xmas-time
5. `docker image save ssrd/its-xmas-time > its-xmas-time.tar`
6. `tar xvf its-xmas-time.tar`
7. `cat tar/3ac3e9ec79c0af263a197784768f9a0133ace6bf38a79b7431a457d972f2b7bd/var/local/main/.history`
8. [.history file](2/tar/3ac3e9ec79c0af263a197784768f9a0133ace6bf38a79b7431a457d972f2b7bd/var/local/main/.history)
9. flag:RaiseAGlassForEveryone
10. `RaiseAGlassForEveryone`

## 3. PISMO BOŽIČKU

1. https://hekaton.mojedelo.com/hekaton/bozicni-it-hekaton/naloga_3/
2. >Poredni škrati.
3. > Božiček je po starem kanalu dobil sporočilo, ki pa so ga zlobni škratje spremenili.
   >
   > Božiček si razbija glavo ker ne ve kam mora dostaviti darila. Otroci bodo žalostni, v kolikor ne dobijo daril. Ali mu lahko pomagaš, kam more dostaviti del daril?
   >
   > Sporočilo: `1110 1 101 000 1110 111 010 000 1110 10 110 1011 11 0101 10 11111 11111`
4. morse koda https://cryptii.com/
5. [CyberChef Recept](https://gchq.github.io/CyberChef/#recipe=Find_/_Replace(%7B'option':'Simple%20string','string':'0'%7D,'-',true,false,false,false)Find_/_Replace(%7B'option':'Simple%20string','string':'1'%7D,'.',true,false,false,false)From_Morse_Code('Space','Line%20feed')&input=MTExMCAxIDEwMSAwMDAgMTExMCAxMTEgMDEwIDAwMCAxMTEwIDEwIDExMCAxMDExIDExIDAxMDEgMTAgMTExMTEgMTExMTEK)
6. `verovskovaulica55`

## 4. BOŽIČKOVA PAMETNA HIŠA

1. https://hekaton.mojedelo.com/hekaton/bozicni-it-hekaton/naloga_4/
2. >Božičku se samodejno odpirajo vrata.
3. >Božičkova pametna hiša ima lokalno omrežje na katerega so preko switchev povezane vse naprave v hiši (IoT, računalniki, multimedija, nadzorne kamere,...). Ker se dogajajo čudne stvari, želi Božiček za vsako skupino od teh naprav ustvariti svoje omrežje. Božiček želi zagotoviti, da lahko naprave komunicirajo samo znotraj svoje skupine. Na primer IoT naprava lahko komunicira samo z napravami, ki spadajo v IoT omrežje.
   >
   >Vse naprave so že priklopljene na več switchev, ki so L2 managed (mrežno stikalo), vsi switchi so povezani na en router (usmerjevalnik).
   >
   >Ali veš kako se imenuje kratica nastavitev za ločevanje omrežij? (angleška kratica)
4. `VLAN`

## 5. ŠIFRIRANA VOŠČILNICA

1. https://hekaton.mojedelo.com/hekaton/bozicni-it-hekaton/naloga_5/
2. >Božiček je od Rijmena prejel čudno voščilnico s samo dvema podatkoma.
3. >Božiček je prejel voščilnico od svojega prijatelja Rijmena. Rijemen ve da poredni škratje berejo Božičkova sporočila. Božiček je tokrat dobil po dveh različnih kanalih dva podatka.
   >
   >Prvi: `IV9zVgsPSwuVbbYjgs5hGTrb7lG953aO`
   >
   >Drugi: `FMpxqPYXvtbPsdGfO2JWXv28mPiS7jRHzoSocTFfkLvZG76EaB6E761qD4OWwrvo`
4. 2x AES decryption, ECB mode, 256 bit key (prvi del `IV9zVgsPSwuVbbYjgs5hGTrb7lG953aO`)
5. [CyberChef recept](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',false,true)AES_Decrypt(%7B'option':'Latin1','string':'IV9zVgsPSwuVbbYjgs5hGTrb7lG953aO'%7D,%7B'option':'Latin1','string':''%7D,'ECB','Raw','Raw',%7B'option':'Hex','string':''%7D,%7B'option':'Hex','string':''%7D)From_Base64('A-Za-z0-9%2B/%3D',false,true)AES_Decrypt(%7B'option':'Latin1','string':'IV9zVgsPSwuVbbYjgs5hGTrb7lG953aO'%7D,%7B'option':'Latin1','string':''%7D,'ECB','Raw','Raw',%7B'option':'Hex','string':''%7D,%7B'option':'Hex','string':''%7D)&input=Rk1weHFQWVh2dGJQc2RHZk8ySldYdjI4bVBpUzdqUkh6b1NvY1RGZmtMdlpHNzZFYUI2RTc2MXFENE9Xd3J2bw)
6. `Lepe praznike :D`

## 6. ČUDNO PISMO

1. https://hekaton.mojedelo.com/hekaton/bozicni-it-hekaton/naloga_6/
2. >Le kako bo Božiček lahko dostavil?
3. >Božiček je dobil čudno pismo, kjer se pojavljajo določeni znaki. Ali mu lahko pomagaš razvozlati sporočilo?
4. https://hekaton.mojedelo.com/wp-content/uploads/2022/12/6.nal_.QXNHYmsPmJsQfW.txt
5. [6.nal_.QXNHYmsPmJsQfW.txt](6/6.nal_.QXNHYmsPmJsQfW.txt)
6. Frequenčna analiza znakov: https://www.dcode.fr/frequency-analysis
7. nekaj znakov se pojavi točno samo po enkrat (drugo 200-300 krat)
8. unique znaki v originalnem vrstnem redu tvorijo
9. `Fr3KveNc4_ZnAk0V`

## 7. NAPAKA PODATKOVNE BAZE

1. https://hekaton.mojedelo.com/hekaton/bozicni-it-hekaton/7-napaka-podatkovne-baze/
2. >Božičkova podatkovna baza.
3. >Škrat Krampus je Božičku spremenil povezavo na bazo. Božiček ne pride več do svojih sporočil. Kakšno geslo mora Božiček uporabiti, da lahko pride do sporočil?
4. https://hekaton.mojedelo.com/wp-content/uploads/2022/11/7.redis_connect.zip
5. [7.redis_connect.zip](7/7.redis_connect.zip)
6. Go binary
7. https://cujo.com/reverse-engineering-go-binaries-with-ghidra/
8. ghidra
9.  find "main.main"
10. github.com/go-redis/redis/v8.NewClient();
11. eden izmed parametrov je geslo
12. `P0rT_L1st3neR`

## 8. PODPORA

1. https://hekaton.mojedelo.com/hekaton/bozicni-it-hekaton/8-podpora/
2. >Božičkova podpora.
3. >Božiček ima novo tehnično pomoč. Palčki so dobili sporočilo od stare babice v katerem piše 4 666 7777 33 66 444 222 2.
4. SMS pisanje
5. https://www.dcode.fr/multitap-abc-cipher
6. `GOSENICA`

## 9. VARNO SHRANJEVANJE GESEL V PODATKOVNI BAZI

1. https://hekaton.mojedelo.com/hekaton/bozicni-it-hekaton/9-varno-shranjevanje-gesel-v-podatkovni-bazi/
2. >Postopek varnega shranjevanja gesel v podatkovni bazi.
3. >Božiček je naročil izdelavo novega bloga, na katerem se bodo uporabniki lahko registrirali. S svojim kreiranim računom bodo lahko na blogu odgovarjali, všečkali in komunicirali z ostalimi blogerji. Varovanje uporabniških gesel ima zelo visoko prioriteto, zato gesla preden jih shranimo v bazo šifriramo z uporabo zgoščevalne funkcije (enosmerna funkcija). To storimo, zato, da v primeru vdora v bazo nepreidipravom otežimo razkrivanje gesel uporabnikov. Postopek shranjevanja gesel ob registraciji deluje tako, da takoj, ko informacijski sistem dobi podatek o registraciji šifrira geslo z uporabo enosmerne zgoščevalne funkcije. Vendar pri tem postopku obstaja ena specifična ranljivost. Predpostavimo, da imamo dva sistema, ki uporabljata isto zgoščevalno funkcijo in uporabnik v obeh sistemih uporabi isto geslo. Pri vdoru v enega od sistemov nepridipravi dobijo hash podatek gesla. Ker je hash uporabljen z enosmerno funkcijo pomeni, da nepridipravom ne preostane drugega, da uporabijo nad geslom napad mavrišne tabele (rainbow attack) ali pa brute force napad. Predpostavimo, da je nepridipravom uspelo razbiti hash in pridobiti geslo. To geslo lahko nato preprosto uporabijo v drugem informacijskem sistemu (pri katerem ni prišlo do vdora) in se lahko brez težav prijavi v račun svoje tarče. Da to preprečimo običajno geslu vsak informacijski sistem doda naključen podatek geslu preden nad njim uporabi zgoščevalno funkcijo. Ta dodan podatek tudi shrani, vendar ločeno z geslom. Ali veš kako se imenuje "začimba", ki je unikatna za vsakega uporabnika, katero dodamo geslu preden ga poženemo skozi zgoščevalno funkcijo? (Odgovori v angleščini)
4. `salt`

## 10. ZVEZDNO SPOROČILO

1. https://hekaton.mojedelo.com/hekaton/bozicni-it-hekaton/10-zvezdno-sporocilo/
2. >Le kaj piše v zvezdah?
3. >Božiček veliko krat gleda v zvezde in premišljuje. Tokrat se mu je med zvezdami zazdelo da vidi sporočilo. Ali znaš prebrati usodo?
4. ![jhfduhdsioehd.png](10/jhfduhdsioehd.png)
5. https://www.dcode.fr/klingon-language
6. https://www.kli.org/about-klingon/writing-klingon/
7. `majqa'`
8. https://memory-beta.fandom.com/wiki/MajQa%27 `majQa' was a Klingonese phrase meaning "well done"`
9. `well done`

## 11. ZASTAVA

1. https://hekaton.mojedelo.com/hekaton/bozicni-it-hekaton/11-zastava/
2. >Božičkova zastava.
3. >Božiček je designerjem poslal nalogo,da mu naredijo novo zastavo. Zastava mu ni všeč ima pa globlje sporočilo.
4. Majhna slika: ![11.santa_flag.png](11/11.santa_flag.png) (4x1 pixel)
5. Povečana: <img src="11/11.santa_flag.png" style="image-rendering:pixelated;width:400px;"/>
6. 4 piksli, hex vrednosti RGB barv:
   1. #6f6e6c
   2. #796f6e
   3. #65776f
   4. #726c64
7. združeno v `6f6e6c796f6e65776f726c64`
8. hex decode [CyberChef recept](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')&input=NmY2ZTZjNzk2ZjZlNjU3NzZmNzI2YzY0)
9. `onlyoneworld`
10. Alternativa: https://convertio.co/png-rgb/

## 12. PRVI NASLOV

1. https://hekaton.mojedelo.com/hekaton/bozicni-it-hekaton/12/
2. >Na kakšnem naslovu se nahaja pošta?
3. >Pridni škratje so Božičku postavili spletni strežnik. Bushy je naredil IP naslovni blok `167.199.170.82/27`. Pepper sedaj ne najde kateri je lahko prvi IP, katerega lahko nastavi spletnemu strežniku. Ali mu lahko pomagaš?
4. IP calculator https://jodies.de/ipcalc?host=167.199.170.82&mask1=27&mask2= or `ipcalc 167.199.170.82/27`
5. ```
    Address:   167.199.170.82        10100111.11000111.10101010.010 10010
    Netmask:   255.255.255.224 = 27  11111111.11111111.11111111.111 00000
    Wildcard:  0.0.0.31              00000000.00000000.00000000.000 11111
    =>
    Network:   167.199.170.64/27     10100111.11000111.10101010.010 00000 (Class B)
    Broadcast: 167.199.170.95        10100111.11000111.10101010.010 11111
    HostMin:   167.199.170.65        10100111.11000111.10101010.010 00001
    HostMax:   167.199.170.94        10100111.11000111.10101010.010 11110
    Hosts/Net: 30```
6. HostMin
7. `167.199.170.65`

## 13. ILCODE

1. https://hekaton.mojedelo.com/hekaton/bozicni-it-hekaton/13-ilcode/
2. >Čudna funkcija.
3. >Božiček je na svojem računalniku našel to funkcijo. Zanima ga kaj vrača ta funkcija. Mu lahko pomagaš?
4. IL koda: [jklgiefnkoekerg.txt](13/jklgiefnkoekerg.txt)
5. IL -> C#: [sharplab](https://sharplab.io/#v2:DYLglsA0AmINQB8ACA2ABAQQLACgDeuAvrrkgOxoDCuataSAHLgTnfQJxoDOALgIY8wAYxps6AM2AB7ASgAsaALJoAFAEp6AZlG0WYugDppQvsC5owAOzA9VO/XQDaABgC6Fyz00AmNH0j2DmiOAIzuVl6+AEYBrEFO3u6SMjzyaACmsfFOmknSsgpCWdnBcnkpadDF2Y4ArO5RUlJQgQ6OKOUFrbRqJHH6llIADt1owNBCBmByBuaacqO8xgbOo+OT0wYoizzLIWsTBgBODGjeBrU7y94Hy6v9YkJSlgBux0wPbON7o0+v76NoGAXlcpJNtJ86N8wQYIUE/m9prcYftIbQhMAeAcNjN7vD0gBHUGTcyXNFjaDLUmjKJHcSmLjpWZjVFBQYjcnQyashxc2G/Z6IhbkgC2AFdgAL/idiczhWzhjSjszgDdOSEQKN2cjJnjeZSUaMAB5SI5St4y8lLGHmeUObWc7yazkGkloO36a1u7bk2kquG8zTOoJ88w+oJHdJYh7EHCx3BAA==)
6. Print solution in [solve.cs](13/solve.cs)
7. Run C#: https://dotnetfiddle.net/EhUjnP
8. `36`

