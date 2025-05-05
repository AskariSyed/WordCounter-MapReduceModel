import threading
from collections import Counter

class WordCounterThread(threading.Thread):
    def __init__(self, thread_id, words, result_dict, lock, progress):
        super().__init__()
        self.thread_id = thread_id
        self.words = words
        self.result_dict = result_dict
        self.lock = lock
        self.progress = progress

    def run(self):
        local_counter = Counter(self.words)
        with self.lock:
            self.result_dict[self.thread_id] = local_counter
            self.progress[self.thread_id] = len(self.words)
