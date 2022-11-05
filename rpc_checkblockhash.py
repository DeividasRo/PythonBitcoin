from bitcoin.rpc import RawProxy
from binascii import unhexlify, hexlify
import hashlib
import codecs
import textwrap


def fixHexZeroes(string, size):
    return '0'*(2+size-len(string)) + string[2:]


def littleEndian(string):
    splited = [str(string)[i:i + 2] for i in range(0, len(str(string)), 2)]
    splited.reverse()
    return "".join(splited)


p = RawProxy()


block = p.getblock(p.getbestblockhash())

block_hash = block['hash']


version_hex = fixHexZeroes(hex(block['version']), 8)
previousblockhash_hex = block['previousblockhash']
merkleroot_hex = block['merkleroot']
time_hex = fixHexZeroes(hex(block['time']), 8)
bits_hex = block['bits']
nonce_hex = fixHexZeroes(hex(block['nonce']), 8)


version_le = littleEndian(version_hex)
previousblockhash_le = littleEndian(previousblockhash_hex)
merkleroot_le = littleEndian(merkleroot_hex)
time_le = littleEndian(time_hex)
bits_le = littleEndian(bits_hex)
nonce_le = littleEndian(nonce_hex)


header_hex = version_le + previousblockhash_le + \
    merkleroot_le + time_le + bits_le + nonce_le

header_bin = codecs.decode(header_hex, 'hex')

# Hashing header info twice
hash = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()

hash = codecs.encode(hash, 'hex_codec').decode('ascii')

hash = littleEndian(hash)

print("Block Hash:", block_hash)
#print("Version:", version_le)
#print("Previous Block Hash:", previousblockhash_le)
#print("Merkle Root:", merkleroot_le)
#print("Time:", time_le)
#print("Bits:", bits_le)
#print("Nonce:", nonce_le)
print("Calculated Hash: ", hash)
print("VERIFICATION SUCCESSFUL" if block_hash ==
      hash else "VERIFICATION FAILED")
