import os, sys

# Amb aquest script podem realitzar streamings de arxius de video
# El podem executar pel terminal de la seguent manera:
# EXEMPLE: python3 streaming.py 'input.mp4'


def streaming():
    os.system("ffmpeg -re -i {} -an -c:v copy -f mpegts udp://@224.2.2.2:2222".format(sys.argv[1]))


streaming()