
accounts = {
    'checking': 1958.00,
    'savings': 3695.50
}


def add_balance(amount: float, name: str = 'checking') -> float:
    """Function to update the balance of an account and
    return new balance"""
    accounts[name] += amount
    return accounts[name]

transactions = [
    (-180.67, 'checking'),
    (-220.00, 'checking'),
    (220.00, 'savings'),
    (-15.70, 'checking'),
    (-23.90, 'checking'),
    (-13.00, 'checking'),
    (1579.50, 'checking'),
    (-600.50, 'checking'),
    (600.50, 'savings')
]

for t in transactions:
    add_balance(*t)  # -> can be instead of add_balance(t[0], t[1]) This unpacks args.
    add_balance(amount=t[0], name=t[1])  # <- can write like so too.

