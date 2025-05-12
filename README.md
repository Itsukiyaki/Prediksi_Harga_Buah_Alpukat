# Prediksi Harga Jual Buah Alpukat

## Repository Outline

1. README.md - Penjelasan gambaran umum project
2. app.py - Script untuk menjalankan aplikasi
3. avocado.csv - Dataset asli yang digunakan dalam project
4. best_rnd_reg_model.pkl - Model machine learning yang telah dilatih
5. description.md - Deskripsi dan dokumentasi project
6. eda.py - Script untuk exploratory data analysis
7. images.jpg - Gambar yang digunakan dalam project
8. eldi_inf.ipynb - Notebook untuk inference model
9. eldi.ipynb - Notebook untuk pengolahan data dan training model
10. prediction.py - Script untuk prediksi harga jual buah alpukat
11. requirements.txt - Daftar dependencies yang dibutuhkan
12. url.txt - File yang berisi URL terkait project
13. Dataset/ - Folder yang berisi dataset dan notebook terkait
14. deployment/ - Folder yang berisi file untuk deployment aplikasi

## Problem Background
Buah Alpukat merupakan salah satu buah yang cukup populer di Indonesia, terutama ketika mendekati bulan suci Ramadhan. Jus Alpukat menjadi salah satu menu takjil yang diminati masyarakat. Selain rasanya yang enak, buah Alpukat juga memiliki beberapa manfaat, salah satunya buah Alpukat dapat membantu penderita Diabetes untuk mengatur gula darah. Meskipun mengandung karbohidrat, indeks glikemik pada buah Alpukat sangat rendah, sehingga tidak mempengaruhi gula darah. Sayangnya meskipun permintaan akan buah Alpukat cukup tinggi, banyak petani yang kesulitan menentukan harga jual dari buah Alpukat, tidak jarang petani menjual buah Alpukat tanpa mendapatkan untung. Program yang dibuat diharapkan dapat memberikan rekomendasi kepada petani mengenai harga jual dari buah Alpukat yang tepat.  

## Project Output
Output dari project ini adalah model machine learning yang dapat digunakan untuk melakukan prediksi dari harga jual buah alpukat. Dibuat juga webapps menggunakan Streamlit berdasarkan dari model machine learning yang telah dibuat.

## Data
Dataset yang digunakan pada project ini berasal dari Kaggle. Dataset ini terdiri dari 14 kolom dan 18248 baris data. Tidak ditemukan adanya missing value pada dataset ini, hanya saja terdapat banyak outlier, meskipun terdapat banyak outlier hal ini dapat dianggap normal terutama pada dataset seperti ini. Terdapat beberapa kolom yang tipe datanya tidak sesuai dengan makna dari kolom seperti kolom Date yang bertipe data object dan beberapa kolom numerikal yang seharusnya bertipe data integer tetapi bertipe data float, sehingga harus dilakukan pengubahan tipe data pada kolom-kolom ini.

## Method
Project Machine Learning ini menggunakan model supervised learning dengan model KNeighborsRegressor, SVR, DecisionTreeRegressor, RandomForestRegressor dan GradientBoostingRegressor.

## Stacks
Bahasa pemrograman yang digunakan pada project ini adalah Python. Tools yang digunakan adalah Streamlit, Streamlit digunakan untuk membuat webapps. Digunakan juga Huggingface untuk melakukan deployment model yang telah dibuat. Library yang digunakan terdiri dari Pandas, Numpy, Matplotlib, Seaborn, Scipy, SKlearn dan Phik

## Reference
Link Dataset : https://www.kaggle.com/datasets/neuromusic/avocado-prices

Link Deployment : https://huggingface.co/spaces/eldim/Prediksi_Harga_Alpukat

---
