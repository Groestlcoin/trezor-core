# Automatically generated by pb2py
import protobuf as p


class EntropyAck(p.MessageType):
    MESSAGE_WIRE_TYPE = 36
    FIELDS = {
        1: ('entropy', p.BytesType, 0),
    }

    def __init__(
        self,
        entropy: bytes = None
    ) -> None:
        self.entropy = entropy
