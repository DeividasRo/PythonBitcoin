from bitcoin.rpc import RawProxy

p = RawProxy()

#txid = "4410c8d14ff9f87ceeed1d65cb58e7c7b2422b2d7529afc675208ce2ce09ed7d"

txid = input("Enter TXID: ")
print()

try:
    raw_tx = p.getrawtransaction(txid)
except:
    print("Invalid TXID.")
    exit()
decoded_tx = p.decoderawtransaction(raw_tx)

vin_sum = 0
vout_sum = 0

# Sum all inputs
for output in decoded_tx['vin']:
    prev_raw_tx = p.getrawtransaction(output['txid'])
    prev_decoded_tx = p.decoderawtransaction(prev_raw_tx)
    # output['vout'] - input'o transakcijos output'o indeksas
    vin_sum += prev_decoded_tx['vout'][output['vout']]['value']

# Sum all outputs
for output in decoded_tx['vout']:
    vout_sum += output['value']

# Calculate fee
fee = vin_sum - vout_sum

#print("TXID:", txid)
print("Transaction fee:", fee, "BTC")
