import json
from collections import defaultdict

class RestAPI:
    def __init__(self, database=None):
        self.users = {}
        if database:
            for user in database['users']:
                self.users[user['name']] = user

    def get(self, url, payload=None):
        if url == '/users':
            if payload:
                data = json.loads(payload)
                users = [self.users[name] for name in data['users'] if name in self.users]
            else:
                users = list(self.users.values())
            return json.dumps({"users": sorted(users, key=lambda x: x['name'])})

    def post(self, url, payload):
        data = json.loads(payload)
        
        if url == '/add':
            name = data['user']
            if name not in self.users:
                self.users[name] = {
                    "name": name,
                    "owes": {},
                    "owed_by": {},
                    "balance": 0.0
                }
            return json.dumps(self.users[name])

        elif url == '/iou':
            lender = data['lender']
            borrower = data['borrower']
            amount = data['amount']

            self._update_iou(lender, borrower, amount)
            self._update_iou(borrower, lender, -amount)

            return json.dumps({
                "users": sorted(
                    [self.users[lender], self.users[borrower]],
                    key=lambda x: x['name']
                )
            })

    def _update_iou(self, user1, user2, amount):
        if user2 not in self.users[user1]['owes'] and user2 not in self.users[user1]['owed_by']:
            if amount > 0:
                self.users[user1]['owed_by'][user2] = amount
            elif amount < 0:
                self.users[user1]['owes'][user2] = -amount
        else:
            if user2 in self.users[user1]['owed_by']:
                self.users[user1]['owed_by'][user2] += amount
                if self.users[user1]['owed_by'][user2] <= 0:
                    if self.users[user1]['owed_by'][user2] < 0:
                        self.users[user1]['owes'][user2] = -self.users[user1]['owed_by'][user2]
                    del self.users[user1]['owed_by'][user2]
            else:
                self.users[user1]['owes'][user2] -= amount
                if self.users[user1]['owes'][user2] <= 0:
                    if self.users[user1]['owes'][user2] < 0:
                        self.users[user1]['owed_by'][user2] = -self.users[user1]['owes'][user2]
                    del self.users[user1]['owes'][user2]

        self._update_balance(user1)

    def _update_balance(self, user):
        self.users[user]['balance'] = sum(self.users[user]['owed_by'].values()) - sum(self.users[user]['owes'].values())