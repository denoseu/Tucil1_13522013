# Tucil 1 Strategi Algoritma (IF2211)
## Denise Felicia Tiowanni: 13522013

## Table of Contents
* [Deskripsi Program](#cyberpunk-2077)
* [Struktur Program](#structure)
* [How to Run](#setup)


## Cyberpunk 2077 Breach Protocol <a href="cyberpunk-2077"></a>
Cyberpunk 2077 Breach Protocol adalah minigame meretas pada permainan video Cyberpunk 2077. 
Minigame ini merupakan simulasi peretasan jaringan local dari ICE (Intrusion Countermeasures Electronics) 
pada permainan Cyberpunk 2077. Komponen pada permainan ini antara lain adalah token, matriks, sekuens, dan bufffer.

## Struktur Program <a href="structure"></a>
![Example screenshot](./img/screenshot.png)


## How to Run <a href="setup"></a>
1. Clone repository ini dengan 
    ```
    git clone https://github.com/NopalAul/Algeo02-22013
    ```
2. Di dalam direktori tersebut, buat virtual environment dengan
    ```
    python -m venv myenv
    ```
3. Aktivasi virtual environment dengan
    - Windows:
        ```
        myenv\Scripts\activate
        ```
    - macOS & Linux:
        ```
        source myenv/bin/activate
        ```
4. Install dahulu requierements dengan melakukan 
    ```
    pip install -r requirements.txt
    ```
5. Pindah ke direktori *website* dengan `cd src/website`
6. Install requierements website dengan command <code>npm install</code>
7. Jalankan website dengan <code>npm start</code>
8. Buka terminal baru, aktivasi lagi virtual environment, pindah ke direktori *backend* dengan `cd src/backend`
9. Jalankan file python dengan <code>python app.py</code>
10. Buka <code>http://localhost:3000</code> pada peramban dan website sudah dapat digunakan