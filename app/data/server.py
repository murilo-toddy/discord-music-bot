from data.queue import Queue


class Server:
    def __init__(self):
        self.queue = Queue()
        self.counter = 0

        self.is_playing = False
        self.is_paused = False
        self.is_loop = False
        self.is_loop_queue = False

    async def increment_counter(self):
        self.counter += 1

    async def reset_counter(self):
        self.counter = 0

    async def set_counter(self, time: int):
        self.counter = time

    def toggle_loop(self):
        self.is_loop = not self.is_loop
        return self.is_loop

    def toggle_loop_queue(self):
        self.is_loop_queue = not self.is_loop_queue
        return self.is_loop_queue
    
    def pause(self):
        self.is_paused = True
    
    def resume(self):
        self.is_paused = False

