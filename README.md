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

