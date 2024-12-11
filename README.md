# CIS4930: Welcome to the In-Memory Transactions Database!

## Setup
1. Download the InMemoryDB.py
2. Install or verify current installation of Python 3 - https://www.python.org/downloads/ 
You can verify current installation by running `python3 --version`
3. Run the file with `python3 InMemoryDB.py`

*Note*: If you run the code in its current state, you will come across errors intentionally produced by the test script in the file.
To test items after these error lines, comment them out by adding `#` to the beginning of the line.

## Special Notes
You may notice that the value for each key in the `keys` dictionary in the InMemoryDB class is a list consisting of two elements.
This is intentional - the first element of the list is the actual current value of the key, the second element is the previous value
that is used in the rollback operation. This second element is populated by anything other than None *only* while a transaction is active.

## How this assignment can be modified in the future
For this assignment to become an "official" assignment in the future, I would suggest adding a requirement that there must also be a 
transaction history stored in the database. In a real life scenario this would obviously be critical for many reasons, including tax reasons,
keeping track of an account's balance, and for disputing and reversing already-completed transactions (for example, if someone's card info
got stolen). Additionally, I would add transaction IDs to these transactions that can be used in a dispute (transactionID) method that 
either temporarily reverses transaction while the dispute is investigated or provides the "victim" a temporary credit.

The instructions in this assignment were somewhat vague, but I saw this as an upside as these vague requirements are likely, in my opinion,
more reflective of the real world. Additionally, it motivated me to think critically about the requirements, figure them out through the 
provided test cases, and allowed me to better exercise my creativity in approaching the problem.
