class InMemoryDB:
    def __init__(self):
        self.keys = dict()
        self.num_active_transactions = 0
        self.active_key = ''

    def get(self, key):
        if(self.num_active_transactions != 0): # this means there is an open transaction
            return None
        try:
            return self.keys[key][0]
        except:
            return None
    
    def put(self, key, val):
        if(self.num_active_transactions != 1):
            raise Exception("Error: Transaction is not active or there is more than one in progress. Please call put(key, val)" 
                " only when ONE transaction is active. There are currently " + str(self.num_active_transactions) 
                + " active transactions in progress.")
        if key not in self.keys:
            self.keys[key] = [val, None] # second element in list is future "old" value for reversal
            self.active_key = key
        else:
            self.keys[key] = [val, self.keys[key][0]] # second element in list is "old" value (old first element) for future reversal
            self.active_key = key

    def begin_transaction(self):
        if(self.num_active_transactions == 0):
            self.num_active_transactions += 1
        else:
            raise Exception("Error: Transaction already in progress. Do not call begin_transaction() until current transaction finished.")

    def commit(self):
        if(self.num_active_transactions != 1):
            raise Exception("Error: Transaction is not active or there is more than one in progress. Please call commit()" 
                " only when ONE transaction is active. There are currently " + str(self.num_active_transactions) 
                + " active transactions in progress.")
        self.keys[self.active_key] = [self.keys[self.active_key][0], None] # Removes "old" value as rollback can no longer occur
        self.num_active_transactions = 0

    def rollback(self):
        if(self.num_active_transactions != 1):
             raise Exception("Error: Transaction is not active or there is more than one in progress. Please call rollback()" 
                " only when ONE transaction is active. There are currently " + str(self.num_active_transactions) 
                + " active transactions in progress.")
        self.keys[self.active_key] = [self.keys[self.active_key][1], None] # moves old value (second element in list) back to original position
        self.num_active_transactions = 0
        


if __name__ == '__main__':
    inmemoryDB = InMemoryDB()

    inmemoryDB.begin_transaction()
    inmemoryDB.begin_transaction()

    # should return null, because A doesn't exist in the DB yet
    print('should return null, because A doesn\'t exist in the DB yet - inmemoryDB.get(\'A\'): ' + str(inmemoryDB.get('A')))

    # should throw an error because a transaction is not in progress
    inmemoryDB.put('A', 5) # successfully causes error - comment this line out to test next items

    # starts a new transaction
    inmemoryDB.begin_transaction()

    # set's value of A to 5, but its not committed yet
    inmemoryDB.put('A', 5)

    # should return null, because updates to A are not committed yet
    print('should return null, because updates to A are not committed yet - inmemoryDB.get(\'A\'): ' + str(inmemoryDB.get('A')))

    # update A's value to 6 within the transaction
    inmemoryDB.put('A', 6)

    # commits the open transaction
    inmemoryDB.commit()

    # should return 6, that was the last value of A to be committed
    print('should return 6, that was the last value of A to be committed - inmemoryDB.get(\'A\'): ' + str(inmemoryDB.get('A')))

    # throws an error, because there is no open transaction
    inmemoryDB.commit() # successfully throws error - comment this line out to test next items

    # throws an error because there is no ongoing transaction
    inmemoryDB.rollback() # successfully throws error - comment this line out to test next items

    # should return null because B does not exist in the database
    print('should return null because B does not exist in the database - inmemoryDB.get(\'B\'): ' + str(inmemoryDB.get('B')))

    # starts a new transaction
    inmemoryDB.begin_transaction()

    # Set key B's value to 10 within the transaction
    inmemoryDB.put('B', 10)

    # Rollback the transaction - revert any changes made to B
    inmemoryDB.rollback()

    #  Should return null because changes to B were rolled back
    print('Should return null because changes to B were rolled back - inmemoryDB.get(\'B\'): ' + str(inmemoryDB.get('B')))