from project.bank_app import BankApp

bank = BankApp(3)

bank.add_loan('StudentLoan')
bank.add_loan('MortgageLoan')

print(bank.add_client('Student', 'Kristian Kovachev', '0000000001', 500))
print(bank.add_client('Adult', 'Martina Kovacheva', '0000000002', 1000))
print(bank.add_client('Adult', 'Natalia Kovacheva', '0000000003', 3000))

print(bank.grant_loan('StudentLoan', '0000000001'))
print(bank.grant_loan('MortgageLoan', '0000000002'))

print(bank.remove_client('0000000003'))

print(bank.increase_loan_interest('StudentLoan'))

print(bank.increase_clients_interest(3.5))

print(bank.get_statistics())
