## Welcome to Hilangin.bg GitHub Pages

## Informasi Kelompok

**Proyek Senior TI**

Kelompok **Hilangin.bg**

|Nama|NIM|Peran|
|---|---|---|
|**Handoko Wisnu Murti (Ketua)**|**19/444054/TK/49250**|**Project Manager/AI Engineer**|
|Brandon Cynwell Pasaribu|19/444043/TK/49239|Software Engineer Project Manager/AI Engineer|
|Muhammad Fariz Al-Pasha|19/444061/TK/49257|Cloud Engineer|
|Gerrit Ezra Yudi Kairupan|19/446777/TK/49882|UI/UX Designer/AI Engineer|
___
Hilangin.bg adalah aplikasi web yang dapat menghilangkan background foto maupun video. Selain itu akan disediakan fitur untuk menggantikan background dengan template yang telah disediakan dan bisa menambahkan background yang diinginkan.
____
>Update : 20 April 2022

## Penugasan Virtual Network dan Load Balancing
Berikut skematik yang digunakan pada website kami
```markdown
![gambar skematik](https://user-images.githubusercontent.com/83200319/164254578-f74ef5b2-c996-4d7b-8409-28b9c8246766.jpeg)
```
Paparan
```markdown
Topologi jaringan pada project Hilangin.bg ini menampung beberapa komponen seperti : 
- Virtual Network Private (Hilangin.bg-VNet) merupakan jaringan virtual yang menampun seluruh komponen yang terdapat dalam aplikasi. Komponen yang terdapat pada jaringan ini mencakup sebuah subnet yang berisi frontend dan backend aplikasi.
- Dua virtual machine pada satu subnet, yaitu subnet Hilangin.bg-SubNet. Hilangin.bg-SubNet mempunyai dua virtual machine, yaitu hilangin-fe dan hilangin-be. Virtual machine hilangin-fe berfungsi untuk merepresentasikan bagian front-end, sedangkan virtual machine hilangin-be berguna untuk mengatur bagian back-end.
- Virtual Machine Network Interface Card (VMNic), VMNic terdapat 2 jenis VMNic, yaitu VMNic untuk hilangin-fe bernama hilangin-fe-VMNic dan VMNic untuk hilangin-be bernama hilangin-be-VMNic. Kedua VMNic tersebut memiliki fungsi yang sama, yakni menghubungkan virtual machine dengan jaringan internet.
Pada virtual machine frontend terhubung dengan azure function yang mengatur fungsi utama pada aplikasi Hilangin.bg. Azure function menyediakan API back-end untuk aplikasi web serta bertugas sebagai pemroses ketika terdapat foto/video yang diunggah
- Blob storage menyimpan semua berkas gambar yang telah diunggah ke aplikasi web serta segala berkas status yang dikonsumsi oleh aplikasi web. 
- Event grid bertugas untuk memicu adanya pemrosesan pada azure function ketika gambar berhasil diunggah
- Computer Vision adalah bagian dari cognitive service yang digunakan untuk mengambil segala informasi mengenai foto/video yang diunggah. Komponen inilah yang dapat mengekstrak berbagai fitur visual pada gambar/video seperti objek, wajah, dan deskripsi teks secara otomatis. 
- Azure Cosmos DB adalah database yang berfungsi untuk menyimpan sementara foto/video yang dikirimkan oleh interaksi pengguna. Foto/video yang dikirimkan oleh pengguna akan masuk ke dalam Azure Cosmos DB. Kemudian, setelah dilakukan proses penghilangan background, hasil foto/video yang sudah dihilangkan background-nya akan disimpan lagi ke dalam Azure Cosmos DB. Hasil foto/video yang sudah diproses akan dikirimkan kembali ke pengguna.

