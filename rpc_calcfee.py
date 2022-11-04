from bitcoin.rpc import RawProxy

p = RawProxy()

txid = "904cc05ebf56cd3db2eaffc4350982ac2ce00dcf7b03273a6983b6dbb929b208"

tx = p.getrawtransaction(txid)

fee = p.calculate_fee(tx)

print(fee)
