import threading
import time
from collections import Counter

class MapperThread(threading.Thread):
    def __init__(self, mapper_id, words, result_dict, meta_dict, lock):
        super().__init__()
        self.mapper_id = mapper_id
        self.words = words
        self.result_dict = result_dict
        self.meta_dict = meta_dict 
        self.lock = lock
    def run(self):
        start = time.time()
        local_count = Counter(self.words)
        end = time.time()

        with self.lock:
            self.result_dict[self.mapper_id] = local_count
            self.meta_dict[self.mapper_id] = {
                "words_processed": len(self.words),
                "time_taken": round(end - start, 4)
            }
