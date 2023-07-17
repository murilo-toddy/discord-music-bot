import random
from data.song import Song


class Queue:
    def __init__(self):
        self.queue: list[Song] = []

    def __len__(self):
        return len(self.queue)

    def __getitem__(self, index: int) -> Song:
        return self.queue[index]

    def __setitem__(self, index: int, song: Song):
        self.queue.insert(index, song)

    def append(self, song: Song):
        self.queue.append(song)

    def remove(self, index: int) -> Song:
        return self.queue.pop(index)

    def move(self, from_index: int, to_index: int):
        self.queue.insert(to_index, self.remove(from_index))

    def clear(self):
        self.queue.clear()

    def shuffle(self):
        random.shuffle(self.queue)

