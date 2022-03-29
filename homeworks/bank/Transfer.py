class Transfer():
    """
    Represents a transfer
    Attributes
    ----------
    holder_id : string
        sender or receiver rut
    holder_name : string
        sender or receiver name
    number : string
        sender or receiver account number
    institution : dict
        id : string
            bank id
        name : string
            bank name
        country : string
            bank country
    """
    def __init__(self, movMeta):
        """
        Params
        ------
            movMeta : dict
                Contains the information about the receiver or sender account.
                Follows format provided by instructions,
                and the ones in the fintoc documentation.
        """
        self.holder_id = movMeta.get(
            'sender_rut',
            movMeta.get('recipient_rut')
            )
        # assumed 'me' as the sender
        if not movMeta.get('recipient_name'):
            self.holder_name = 'me'
        else:
            self.holder_name = movMeta.get('recipient_name')
        self.number = movMeta.get(
            'sender_account',
            movMeta.get('recipient_account')
            )

        id = movMeta.get('sender_bank', movMeta.get('recipient_bank'))
        bank_name = movMeta.get('sender_bank_raw_name',
                                movMeta.get('recipient_bank_raw_name'))
        self.institution = {'id':  id,
                            'name': bank_name,
                            'country': bank_name[:2] if bank_name else bank_name}

if __name__ == '__main__':
    pass
