import os
import subprocess

print("ATENCAO: O ARQUIVO FFMPEG.EXE E O ARQUIVO FFMPEG.PY DEVEM ESTAR NA MESMA PASTA!")

caminho = os.path.dirname(os.path.abspath(__file__))
original = input("Inserir o nome do arquivo a converter (sem extensao): ") + '.mkv'
final = input("inserir o nome do arquivo convertido (sem extensao): ") + '.mp4'

os.chdir(caminho)

#ffmpeg -i nomedovideo.wmv -c:v libx264 -crf 23 -c:a aac -q:a 100 nomedonovovideo.mp4
#subprocess.call(['ffmpeg', '-i', original, '-c:v' , 'libx264', '-crf', '23', '-c:a', 'aac' , '-q:a','100',  final]) <-> WMV pra MP4
subprocess.call(['ffmpeg', '-i', original,'-s', '720x480', '-c:a', 'aac' ,  final]) # <<< mkv pra mp4


input("Aperte qualquer tecla para sair")