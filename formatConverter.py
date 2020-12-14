# Aquest script permet cambiar arxius de video als formats VP8, VP9, h265 i AV1
# Es pot executar des de terminal de la seguent manera (posant l'input  el nom de sortida)
# EXEMPLE: python3 formatConverter.py 'input.mp4' 'output_name'

import sys, os

def convertFormat():

    print('Selecciona el format de sortida:')
    opt = input('\n\t 1. VP8 \n\t 2. VP9 \n\t 3. h265 \n\t 4. AV1 \n\t 5. Tots els formats anteriors \n')
    input_video = sys.argv[1]
    output_name = sys.argv[2]

    if opt == '1':
        os.system("ffmpeg -i {} -c:v libvpx -b:v 1258k -c:a libvorbis {}.webm".format(input_video, output_name))
    elif opt == '2':
        os.system("ffmpeg -i {} -c:v libvpx-vp9 -b:v 1258k {}.webm".format(input_video, output_name))
    elif opt == '3':
        os.system("ffmpeg -i {} -c:v libx265 -crf 28 -c:a aac -b:a 1258k {}.mp4".format(input_video, output_name))
    elif opt == '4':
        os.system("ffmpeg -i {} -c:v libaom-av1 -b:v 1258k -strict experimental {}.mkv".format(input_video, output_name))
    elif opt == '5':
        os.system("ffmpeg -i {} -c:v libvpx -b:v 1258k -c:a libvorbis {}_VP8.webm".format(input_video, output_name))
        os.system("ffmpeg -i {} -c:v libvpx-vp9 -b:v 1258k {}_VP9.webm".format(input_video, output_name))
        os.system("ffmpeg -i {} -c:v libx265 -crf 28 -c:a aac -b:a 1258k {}_h265.mp4".format(input_video, output_name))
        os.system("ffmpeg -i {} -c:v libaom-av1 -b:v 1258k -strict experimental {}_AV1.mkv".format(input_video, output_name))
    else:
        print('Aquesta opció no existeix.')
        convertFormat()


convertFormat()

