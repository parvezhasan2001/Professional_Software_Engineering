
from collections import defaultdict
from typing import Callable, Dict, List, Any

class EventBus:
    def __init__(self):
        self._subs: Dict[str, List[Callable[..., None]]] = defaultdict(list)

    def subscribe(self, event_name: str, fn: Callable[..., None]):
        self._subs[event_name].append(fn)

    def publish(self, event_name: str, **payload: Any):
        for fn in self._subs.get(event_name, []):
            fn(payload)

# Global event bus for simplicity
bus = EventBus()
