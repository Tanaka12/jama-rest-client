from typing_extensions import Self

class AttachmentRequest:
    attachment: int

    def __init__(self):
        self.attachment = 0

    def __eq__(self, other: Self):
        return self.attachment == other.attachment