# S3_SCAV_VIDEO

**EXERCICI 1**

Aquest script permet cambiar arxius de video als formats VP8, VP9, h265 i AV1
Es pot executar des de terminal de la seguent manera (posant l'input  el nom de sortida)
EXEMPLE: python3 formatConverter.py 'input.mp4' 'output_name'
L'AV1 es molt lent a l'hora de codificar-se i l'h265 el més ràpid.


**EXERCICI 2**

Aquest script serveix per visualitzar 4 videos diferents a la mateixa pantalla.
Es pot executar des del terminal de la seguent manera:
EXEMPLE: python3 mosaic4videos.py 'output_VP8.webm' 'output_VP9.webm' 'output_h265.mp4' 'output_AV1.mp4'

*https://stackoverflow.com/questions/35034775/how-to-merge-four-videos-on-one-screen-with-ffmpeg*

El VP8 i VP9 són els menys poc eficients en temes de bit rate comparat amb el h265 i l'AV1.


**EXERCICI 3**

Amb aquest script podem realitzar streamings de arxius de video
El podem executar pel terminal de la seguent manera:
EXEMPLE: python3 streaming.py 'input.mp4'

Podem visualitzar l'streaming mitjançant ffplay o bé amb el programa VLC copiant la IP (udp://@224.2.2.2:2222)

No he pogut probar-lo sencer perquè m'anava molt lent, per culpa de la màquina virtual tot i que l'he pogut visualitzar (entretallat).
A continuació deixo una captura de l'streaming.

![ScreenShot SE_Streaming](https://github.com/paumonterop/S2_SCAV_VIDEO/S3_streaming.png?raw=true)

