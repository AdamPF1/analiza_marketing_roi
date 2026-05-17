# Analiza marketinškog ROI indeksa

Ovaj projekat prikazuje jednostavnu analizu marketinškog ROI indeksa pomoću Python biblioteka **pandas** i **matplotlib**.

Program koristi primer podataka za različite tipove objava i računa ROI indeks na osnovu:

- dosega objave,
- engagement rate-a sponzora,
- vremena potrebnog za kreiranje sadržaja.

Rezultat se prikazuje kao stubičasti grafikon, gde je najbolji ROI indeks posebno označen crvenom bojom.

## Tehnologije

Projekat koristi:

- Python
- pandas
- matplotlib

## Instalacija

Pre pokretanja projekta potrebno je instalirati zavisnosti.

Ako koristiš virtuelno okruženje, prvo ga aktiviraj.

Zatim instaliraj potrebne biblioteke: bash pip install pandas matplotlib        

``` 
## Pokretanje projekta

Pokreni Python fajl komandom:
```

bash python trening.py``` 

Nakon pokretanja prikazaće se grafikon sa analizom ROI indeksa.

## Opis podataka

Podaci u projektu su primeri i služe za demonstraciju analize.

Korišćene kolone su:

- `tipObjave` — tip objave
- `reach` — broj ljudi do kojih je objava stigla
- `sponsozorEngagementRate` — procenat angažovanja sponzora
- `vremeKreiranjaSati` — vreme potrebno za kreiranje objave
- `roiIndeks` — izračunati ROI indeks

Formula za ROI indeks:
```

text ROI indeks = reach * (sponsozorEngagementRate / 100) / vremeKreiranjaSati``` 

## Primer rezultata

Program generiše stubičasti grafikon koji poredi ROI indeks za različite tipove objava.

Objava sa najvećim ROI indeksom prikazana je crvenom bojom, dok su ostale prikazane tamno sivom bojom.

## Struktura projekta
```

text . ├── trening.py ├── README.md └── .gitignore``` 

## Autor

Projekat je napravljen kao primer analize podataka i vizualizacije u Pythonu.
```

