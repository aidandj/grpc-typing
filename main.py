from typing import reveal_type
from typed import dummy_pb2_grpc as typed_grpc
from typed import dummy_pb2 as typed_messages
from untyped import dummy_pb2_grpc as untyped_grpc
from untyped import dummy_pb2 as untyped_messages

def main():
    typed_stub = typed_grpc.DummyServiceStub()
    reveal_type(typed_stub.UnaryUnary)  # Revealed type is 'UnaryUnaryMultiCallable[DummyRequest, DummyReply]'
    untyped_stub = untyped_grpc.DummyServiceStub()
    reveal_type(untyped_stub.UnaryUnary)  # Revealed type is 'Any'

    reveal_type(typed_stub.UnaryUnary.with_call)
    reveal_type(untyped_stub.UnaryUnary.with_call)

    typed_response = typed_stub.UnaryUnary(request=typed_messages.DummyRequest())
    reveal_type(typed_response)  # Revealed type is 'typed_messages.DummyReply'
    untyped_response = untyped_stub.UnaryUnary(request=untyped_messages.DummyRequest())
    reveal_type(untyped_response)  # Revealed type is 'Any'

if __name__ == "__main__":
    main()
