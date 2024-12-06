import threading
import time
from dataclasses import dataclass, replace
from pydantic import BaseModel
from uuid import uuid4

from services.ai.stable_diffusion import GenerateImageMeta


class GenerationQueueItem(GenerateImageMeta, BaseModel):
    id: str


class GenerationQueue:
    def __init__(self):
        self.queue = []

    def push_back(self, item: GenerateImageMeta):
        self.queue.append(GenerationQueueItem(**item.model_dump(), id=str(uuid4())))

    def pop_front(self):
        return self.queue.pop(0)

    def __len__(self):
        return len(self.queue)

    def __iter__(self):
        return iter(self.queue)

    def get_queue(self):
        return self.queue

    def process(self):
        while True:
            if len(self.queue) > 0:
                item = self.pop_front()
                print(f"Processing item {item.id}...")
                print("Data:", item)
            else:
                time.sleep(1)

    queue: list[GenerationQueueItem]


generationQueue = GenerationQueue()

generationQueueThread = threading.Thread(
    target=generationQueue.process, daemon=True, args=(generationQueue)
)
generationQueueThread.start()
