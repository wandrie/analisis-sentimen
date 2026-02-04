# 1. Instalasi Library

#pip install google-play-scraper

from google_play_scraper import app, reviews_all, Sort

"""## 2. Scraping Dataset"""

scrapreview = reviews_all(
    'com.tokopedia.tkpd',
    lang='id',
    country='id',
    sort=Sort.MOST_RELEVANT,
    count=10000 # Jumlah maksimal data yang dibuat
)

import pandas as pd

app_reviews_df = pd.DataFrame(scrapreview)
app_reviews_df.shape
app_reviews_df.head()
app_reviews_df.to_csv('dataset.csv', index=False)

app_reviews_df.info()

# Membuat DataFrame dari hasil scrapreview
app_reviews_df = pd.DataFrame(scrapreview)

# Menghitung jumlah baris dan kolom dalam DataFrame
jumlah_ulasan, jumlah_kolom = app_reviews_df.shape

# Membuat DataFrame baru (clean_df) dengan menghapus baris yang memiliki nilai yang hilang (NaN) dari app_reviews_df
clean_df = app_reviews_df.dropna()
# Menghapus baris duplikat dari DataFrame clean_df
clean_df = clean_df.drop_duplicates()

# Menghitung jumlah baris dan kolom dalam DataFrame clean_df setelah menghapus duplikat
jumlah_review_setelah_hapus_duplikat, jumlah_kolom_setelah_hapus_duplikat = clean_df.shape

print("Jumlah ulasan setelah menghapus duplikat:", jumlah_review_setelah_hapus_duplikat)
