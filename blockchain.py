class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        # Make a new block and add it to the chain
        pass

    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction that will go in the next mined Block

        :param sender: <str> Address of the sender
        :param recipient: <str> Address of the recipent        
        :param amount: <int> amount to be transacted
        :return: <int> Index of the block to hold this transaction
        """

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        # Hashes the block
        pass

    @property
    def last_block(self):
        # Returns the last Block in the chain
        pass     