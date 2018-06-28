from apps.common import seed
from trezor.crypto.curve import secp256k1
from trezor.messages.RippleSignTx import RippleSignTx
from trezor.messages.RippleSignedTx import RippleSignedTx
from trezor.messages.RippleTxTypeRequest import RippleTxTypeRequest
from trezor.messages.RipplePaymentTxType import RipplePaymentTxType
from trezor.messages.wire_types import RipplePaymentTxType
from .serializer import serialize_object
from ubinascii import hexlify


async def sign_tx(ctx, msg: RippleSignTx):
    node = await seed.derive_node(ctx, msg.address_n)

    tx_type = await ctx.call(RippleTxTypeRequest(), RipplePaymentTxType)

    # todo serialize
    # todo hash
    serialized = serialize_object({
        "TransactionType": "Payment",
        "Account": msg.account,
        "Destination": tx_type.destination,
        "Amount": tx_type.amount,
        "Fee": msg.fee,
        "Sequence": msg.sequence,
        "SigningPubKey": node.public_key()
    })

    print(serialized)

    # digest = (tx)
    signature = secp256k1.sign(node.private_key(), digest)

    return RippleSignedTx(signature)
    # seckey = node.private_key()
    # pubkey = node.public_key()

# ('30440220134ac7015ac832a52fd0ed46910e74fdce01bc4703d93d3d4000e2e83cca88e002200156f9f3d326c34c08ddd29e94af6e002a8b7707d6fad5e50f9a940cf1a93571'))

