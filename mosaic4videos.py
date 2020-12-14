# Aquest script serveix per visualitzar 4 videos diferents a la mateixa pantalla.
# EXEMPLE: python3 mosaic4videos.py 'output_VP8.webm' 'output_VP9.webm' 'output_h265.mp4' 'output_AV1.mp4'

import os, sys


def merge4video():

    os.system('ffmpeg -i {} -i {} -i {} -i {} -filter_complex "[0:v][1:v]hstack[top]; '
              '[2:v][3:v]hstack[bottom]; [top][bottom]vstack,format=yuv420p[v]; '
              '[0:a][1:a][2:a][3:a]amerge=inputs=4[a]" '
              '-map "[v]" -map "[a]" -ac 2 output.mp4'.format(sys.argv[1],sys.argv[2],
              sys.argv[3],sys.argv[4]))

merge4video()

