import random

class Queue:
    def __init__(self):
        self.music_list = []

    def __len__(self):
        return len(self.music_list)

    def __getitem__(self, index):
        return self.music_list[index]
    
    def __setitem__(self, index, url):
        self.music_list.insert(index,url)

    def append(self,url):
        self.music_list.append(url)

    def remove(self, index):
        return self.music_list.pop(index)

    def imprime(self):
        print(self.music_list)

    def move(self, starting_index, final_index):
        self.music_list.insert(final_index,self.MusicList.pop(starting_index))

    def clear(self):
        self.music_list.clear()

    def shuffle(self):
        random.shuffle(self.music_list)
