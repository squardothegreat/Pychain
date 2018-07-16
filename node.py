from uuid import uuid4

from bchain import Blockchain
from verification import Verification


class Node:
    def __init__(self):
        # self.id = str(uuid4())
        self.id = 'Johnny'
        self.blockchain = Blockchain(self.id)
        

    # Gets the transaction value
    def get_transaction_value(self):
        tx_recipient = input('Enter the recipient of the transaction: ')
        tx_amount = float(input('Your transaction amount please: '))
        return tx_recipient, tx_amount

    # Gets your input
    def get_user_choice(self): 
        user_input = input('Your choice: ')
        return user_input


    def print_blockchain_elements(self):
        for block in self.blockchain.get_chain(): 
            print('Outputting Block')
            print(block)
        else:
            print('-' * 20)

    def listen_for_input(self):
        waiting_for_input = True
        while waiting_for_input:
            print('Please Choose')
            print('1: Add a new transaction value')
            print('2: Mine a new block')
            print('3: Output the blockchain blocks')
            print('4: Check Transaction validity')
            print('q: Quit')
            user_choice = self.get_user_choice()
            if user_choice == '1':
                tx_data = self.get_transaction_value()
                recipient, amount = tx_data
                # Add the transaction amount to the blockchain
                if self.blockchain.add_transaction(recipient, self.id, amount=amount):
                    print('Added Transaction!')
                else:
                    print('Transaction Failed!')
                print(self.blockchain.get_open_transactions())
            elif user_choice == '2': 
                self.blockchain.mine_block()
            elif user_choice == '3':
                self.print_blockchain_elements()
            elif user_choice == '4':
                if Verification.verify_transactions(self.blockchain.get_open_transactions(), self.blockchain.get_balance):
                    print('All transactions are valid')
                else:
                    print('There are invalid transactions')
            elif user_choice == 'q':
                # This will lead to the loop to exist because it's running condition
                waiting_for_input = False
            else:
                print('Input was invalid. Pease pick a value from the list!')
            if not Verification.verify_chain(self.blockchain.get_chain()):
                self.print_blockchain_elements()
                print('Invalid blockchain!')
                break
            print('Balance of {}: {:6.2f}'.format(self.id, self.blockchain.get_balance()))
        else: 
            print('User Left!')

        print('Done!')

node = Node()
node.listen_for_input()