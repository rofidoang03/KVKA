import sys
import os.path
from moviepy.editor import VideoFileClip

# Fungsi untuk menampilkan banner
def banner():
    print("""
 __   ___  ___      ___  __   ___       __      
| "| /  ")|"  \    /"  || "| /  ")     /""\     
(: |/   /  \   \  //  / (: |/   /     /    \    
|    __/    \   \/. ./  |    __/     /' /\  \   
(   _  \     \.     /   (   _  \    /   __'  \  
|: | \  \     \    /    |: | \  \  /   /  \   \ 
(__|  \__)     \__/     (__|  \__)(___/    \___)
""")

# Fungsi untuk menampilkan pesan bantuan
def pesan_bantuan():
    banner()
    print(f"Penggunaan: python {sys.argv[0]} --file-video <nama_file_video> --file-audio <nama_file_audio>")
    print("\nKonversi file video menjadi file audio.")
    print("\nOpsi:")
    print("\n--help             Tampilkan pesan bantuan ini dan keluar.")
    print("--file-video       Nama file video (.mp4).")
    print("--file-audio       Nama file audio (.mp3).")

# Fungsi untuk melakukan konversi video ke audio
def konversi_video_ke_audio(video_file, audio_file):
    try:
        print("[*] Melakukan konversi...")
        print("")
        
        video = VideoFileClip(video_file)
        audio = video.audio
        audio.write_audiofile(audio_file)
        video.close()
        
        print("")
        print("[*] Konversi selesai.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Fungsi untuk validasi ekstensi file
def validasi_ekstensi(file, ekstensi):
    return file.lower().endswith(ekstensi)

# Fungsi utama program
def utama():
    if len(sys.argv) != 5 or '--help' in sys.argv:
        pesan_bantuan()
    else:
        index_video = sys.argv.index('--file-video') if '--file-video' in sys.argv else -1
        index_audio = sys.argv.index('--file-audio') if '--file-audio' in sys.argv else -1
        
        if index_video != -1 and index_audio != -1:
            file_video = sys.argv[index_video + 1]
            file_audio = sys.argv[index_audio + 1]
            
            if not (validasi_ekstensi(file_video, '.mp4') and validasi_ekstensi(file_audio, '.mp3')):
                print("Ekstensi file tidak valid. Pastikan file video dalam format .mp4 dan file audio dalam format .mp3")
            elif not os.path.isfile(file_video):
                print(f"File video '{file_video}' tidak ditemukan.")
            else:
                konversi_video_ke_audio(file_video, file_audio)
            
        else:
            pesan_bantuan()

# Menjalankan program utama jika file ini dieksekusi secara langsung
if __name__ == "__main__":
    utama()
