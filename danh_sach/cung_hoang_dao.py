def slove(day, moth):
    if(moth == 3):
        if(day >= 21):
            return 'Bach Duong'
        else:
            return 'Song Ngu'
    elif(moth == 4):
        if(day <= 19):
            return 'Bach Duong'
        else:
            return 'Kim Nguu'
    elif(moth == 5):
        if(day <= 20):
            return 'Kim Nguu'
        else:
            return 'Song Tu'
    elif(moth == 6):
        if(day <= 20):
            return 'Song Tu'
        else:
            return 'Cu Giai'
    elif(moth == 7):
        if(day <= 22):
            return 'Cu Giai'
        else:
            return 'Su Tu'
    elif(moth == 8):
        if(day <= 22):
            return 'Su Tu'
        else:
            return 'Xu Nu'
    elif(moth == 9):
        if(day <= 22):
            return 'Xu Nu'
        else:
            return 'Thien Binh'
    elif(moth == 10):
        if(day <= 22):
            return 'Thien Binh'
        else:
            return 'Thien Yet'
    elif(moth == 11):
        if(day <= 22):
            return 'Thien Yet'
        else:
            return 'Nhan Ma'
    elif(moth == 12):
        if(day <= 21):
            return 'Nhan Ma'
        else:
            return 'Ma Ket'
    elif(moth == 1):
        if(day <= 19):
            return 'Ma Ket'
        else:
            return 'Bao Binh'
    elif(moth == 2):
        if(day <= 18):
            return 'Bao Binh'
        else:
            return 'Song Ngu'

t = int(input())
while(t > 0):
    t -= 1
    day, moth = map(int, input().split())
    print(slove(day, moth))
    
