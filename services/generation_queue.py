from dataclasses import dataclass, replace
from pydantic import BaseModel
from uuid import uuid4


class GenerationRequest(BaseModel):
    prompt: str


class GenerationQueueItem(GenerationRequest, BaseModel):
    id: str


class GenerationQueue:
    def __init__(self):
        self.queue = []

    def push_back(self, item: GenerationRequest):
        self.queue.append(GenerationQueueItem(**item.model_dump(), id=str(uuid4())))

    def pop_front(self):
        return self.queue.pop(0)

    def __len__(self):
        return len(self.queue)

    def __iter__(self):
        return iter(self.queue)

    def get_queue(self):
        return self.queue

    queue: list[GenerationQueueItem]
