import json
from Movement import Movement
from os.path import join


class BankStatement():
    """
    A class to represent an account bank statements
    Attributes
    --------------
    current_state : dict
        Fast index of movements
    sorted_state : list
        Sorted state of movements, ordered by (date, amount) from low to high
    path : string
        Path to search for json statements files
    """
    def __init__(self, path):
        self.current_state = {}
        self.sorted_state = []
        self.path = path

    def update(self, snapshot_file_name):
        """
        Update bank statements with a new snapshot
        Params
        --------
            snapshot_file_name : string
                File name of snapshot. Expected a JSON format.
        """
        repeatedChecksKeys = {}
        with open(join(self.path, snapshot_file_name)) as json_file:
            account_snapshot = json.loads(json_file.read())
            for i, mov in enumerate(account_snapshot['movements']):
                movement = Movement(mov, account_snapshot['currency'])
                mov_id_tuple = (movement.amount, movement.transaction_date,
                                movement.id)

                if movement.recipient_account or movement.sender_account:
                    k = repeatedChecksKeys.get(mov_id_tuple, 0) + 1
                    repeatedChecksKeys[mov_id_tuple] = k
                    self.current_state[(k, *mov_id_tuple)] = movement

    def sort_statements(self):
        """Sorts current state, utility for printing.
        Sorts by post_date and amount"""
        self.sorted_state = [*self.current_state.values()]
        self.sorted_state.sort(key=lambda x: (x.post_date, x.amount))

    def show_movements(self):
        self.sort_statements()
        print(len(self.sorted_state))
        """Print movements"""
        for movement in self.sorted_state:
            print(f'''{movement.post_date} | {movement.amount} |
                {movement.description}''')


if __name__ == '__main__':
    pass
