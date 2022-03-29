from Transfer import Transfer


class Movement():
    """
        A class representing movements
        Attributes
        ----------
        Follows the structure in https://docs.fintoc.com/reference/movements-object
    """
    def __init__(self, mov, currency="clp"):
        """
        Handles cases where mov has different key structures
        Params
        ------
        mov : dict
            object folliwing one of the structures provided by instructions.
        """
        if mov['type'] == 'outbound':
            mov['amount'] = -abs(mov['amount'])
            self.recipient_account = mov['movement_meta']
        else:
            self.sender_account = mov['movement_meta']

        self.id = mov.get('id', None)
        self.object = 'movement' if mov['movement_meta'] else ''
        self.amount = mov['amount']
        self.post_date = mov['accountable_date']
        self.description = mov['description']
        self.transaction_date = mov.get('date', None)
        self.currency = currency
        if mov['movement_meta']:
            self.reference_id = self.id
        else:
            self.reference_id = mov['document_number']
        self.type = 'transfer' if mov['movement_meta'] else 'check'
        self.comment = mov['movement_meta'].get('comment', None)

        self.pending = 'false'  # TODO: track checks pending state
        self.recipient_account = Transfer(mov['movement_meta'])
        self.sender_account = Transfer(mov['movement_meta'])

if __name__ == '__main__':
    pass
