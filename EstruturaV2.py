import collections
import random

class Lista:
    def __init__(self):
        self.MusicList = []

    def __len__(self):
        return len(self.MusicList)

    def __getitem__(self, index):
        return self.MusicList[index]
    
    def __setitem__(self, index, url):
        self.MusicList.insert(index,url)

    def append(self,url):
        self.MusicList.append(url)

    def remove(self,index):
        return self.MusicList.pop(index)

    def imprime(self):
        print(self.MusicList)

    def move(self,indiceInicial,IndiceFinal):
        self.MusicList.insert(IndiceFinal,self.MusicList.pop(indiceInicial))

    def clean(self):
        self.MusicList.clear()

    def shuffle(self):
        random.shuffle(self.MusicList)
