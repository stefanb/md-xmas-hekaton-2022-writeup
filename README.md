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

