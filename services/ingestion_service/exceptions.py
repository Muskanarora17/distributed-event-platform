from uuid import UUID


class DuplicateEventError(Exception):
    def __init__(self, event_id: UUID):
        self.event_id = event_id
        super().__init__(f"Event with ID {event_id} already exists.")