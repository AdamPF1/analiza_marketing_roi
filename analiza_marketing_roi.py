import pandas as pd
import matplotlib.pyplot as plt

data = {
    'tipObjave': [
        'Tehnicki detalji(EV)',
        'Behind the Scenes',
        'Rezultati trke',
        'Intervju sa inženjerima',    #ovo su samo predlozi popoularnih objava koje mozemo videti na TikToku i Instagramu
        'Sponzorski promo'
    ],
    'reach': [15000, 22000, 30000, 12000, 8000],  #mock data, izmisljeno skroz
    'sponsozorEngagementRate': [4.5, 6.2, 3.1, 5.5, 2.0],  # ovo je obican meatematicka formula
    'vremeKreiranjaSati': [5, 2, 3, 4, 1]                  # (broj filtriranih b2b interakcija/ukupan doseg)*100
}

df = pd.DataFrame(data)
#kreiranje ROI indeksa
df['roiIndeks'] = (
    df['reach'] * (df['sponsozorEngagementRate'] / 100)
) / df['vremeKreiranjaSati']

plt.figure(figsize=(10, 6))
#dinamicko bojenje, lakse prepoznavanje
bars = plt.bar(
    df['tipObjave'],
    df['roiIndeks'],
    color=['#e60000' if x == max(df['roiIndeks']) else '#404040' for x in df['roiIndeks']]
)

plt.title('Analiza Marketinskog ROI: Fokus na B2B Angazovanje Sponzora', fontsize=14, fontweight='bold')
plt.ylabel('ROI Indeks (Angazovanje/Ulozeno Vreme)', fontsize=12)
plt.xticks(rotation=45, ha='right')

for bar in bars:
    yval = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        yval + 10,
        round(yval, 1),
        ha='center',
        va='bottom',
        fontweight='bold'
    )

plt.tight_layout()
plt.show()
