import csv
import math
import random
import pandas as pd
'''
from pandas import DataFrame
from sklearn.cluster import KMeans
'''
import numpy as np
import matplotlib.pyplot as plt
akar = math.sqrt

def program():
    dataset = pd.read_csv("Data-jumlah-penumpang-bus-09-September.csv")
    print (dataset)

    # mengambil kolom 2 dan 4
    kol_madya = dataset.iloc[:, 3].values
    kol_mandiri = dataset.iloc[:, 4].values
    print(kol_madya,kol_mandiri)

    def mencari_centroid_dst():
        # mengambil letak centroid pertama acak
        random1 = []
        for i in range(30):
            random1.append(i)
        hasil_random1 = random.choice(random1)

        # hasil centroid pertama acak
        cen_pertama1 = kol_madya[hasil_random1]
        cen_pertama2 = kol_mandiri[hasil_random1]
    
        # mengambil letak centroid kedua acak
        random2 = []
        for j in range(30):
            random2.append(j)
        hasil_random2 = random.choice(random2)

        # hasil centroid kedua acak
        cen_kedua1 = kol_madya[hasil_random2]
        cen_kedua2 = kol_mandiri[hasil_random2]
    
        if (cen_pertama1==cen_kedua1 and cen_pertama2==cen_kedua2):
            mencari_centroid_dst()
        else:
            print ("Centroid pertama = ",cen_pertama1,"dan",cen_pertama2)
            print ("Centroid kedua = ",cen_kedua1,"dan",cen_kedua2)

            # menghitung distance ke centroid 1 dan centroid 2
            hasil_hitung_pertama1 = []
            hasil_hitung_pertama2 = []
            hasil1 = []
            hasil2 = []
            anggota1_kiri = []
            anggota1_kanan = []
            anggota2_kanan = []
            anggota2_kiri = []
            jml_awal1 = []
            jml_awal2 = []

            for a in range(30):
                for b in range(30):
                    if (a==b):
                        jarak1 = akar(((cen_pertama1 - kol_madya[a])**2) + ((cen_pertama2 - kol_mandiri[a])**2))
                        jarak2 = akar(((cen_kedua1 - kol_madya[a])**2) + ((cen_kedua2 - kol_mandiri[a])**2))
                        if(jarak1 < jarak2):
                            hasil1.append(jarak1)
                            anggota1_kiri.append(kol_madya[a])
                            anggota1_kanan.append(kol_mandiri[a])
                            hasil_hitung_pertama1.append(jarak1)
                            jml_awal1.append(jarak1)
                            hasil_hitung_pertama2.append(jarak2)
                        else:
                            hasil2.append(jarak2)
                            anggota2_kanan.append(kol_mandiri[a])
                            anggota2_kiri.append(kol_madya[a])
                            hasil_hitung_pertama2.append(jarak2)
                            jml_awal2.append(jarak2)
                            hasil_hitung_pertama1.append(jarak1)

            # menghitung rata-rata tiap kolom sebagai pusat yang baru
   
            hasil1_baru = []
            hasil2_baru = []
            anggota_clus1 = []
            anggota_clus2 = []
            seluruh_kiri = []
            seluruh_kanan = []

            '''
            Data = {'x':dataset.iloc[:, 2],
                    'y':dataset.iloc[:, 4]}
            
            df = DataFrame(Data,columns=['x','y'])

            kmeans = KMeans(n_clusters=2).fit(df)
            '''
            
            rata1_a = sum(anggota1_kiri) / len(anggota1_kiri)
            rata1_b = sum(anggota1_kanan) / len(anggota1_kanan)
            rata2_a = sum(anggota2_kiri) / len(anggota2_kiri)
            rata2_b = sum(anggota2_kanan) / len(anggota2_kanan)
            for j in range(30):
                for k in range(30):
                    if(j==k):
                        dist1 = akar(((rata1_a - kol_madya[j])**2) + ((rata1_b - kol_mandiri[j])**2))
                        dist2 = akar(((rata2_a - kol_madya[j])**2) + ((rata2_b - kol_mandiri[j])**2))
                        if (dist1<dist2):
                            hasil1_baru.append(dist1)
                            seluruh_kiri.append(dist1)
                            seluruh_kanan.append(dist2)
                            anggota_clus1.append(kol_madya[j])
                        else:
                            hasil2_baru.append(dist2)
                            seluruh_kanan.append(dist2)
                            seluruh_kiri.append(dist1)
                            anggota_clus2.append(kol_madya[j])
            if (len(hasil1)==len(hasil1_baru) and len(hasil2)==len(hasil2_baru)):
                plt.scatter(seluruh_kiri,seluruh_kanan,c='brown')
                plt.show()
                
                '''
                plt.scatter(df['x'], df['y'], c=kmeans.labels_.astype(float), s=50, alpha=0.5)
                plt.show()
                '''
                
                print ("Data cluster pertama adalah :",anggota1_kiri,anggota1_kanan)
                print ("Data cluster kedua adalah :",anggota2_kiri,anggota2_kanan)
            
    mencari_centroid_dst()


  

a = 'y'
while(a=='y'):
    program()
    a = str(input('tekan y sampai didapatkan tampilan cluster....'))



