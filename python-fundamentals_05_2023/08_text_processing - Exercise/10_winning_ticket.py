    ticket_list = input().split(', ')


    def valid_ticket(ticket):
        if len(ticket) == 20:
            return True
        return False


    def winning_ticket(ticket):
        valid_symbols = ['@', '#', '$', '^']
        half_length = len(ticket) // 2
        first_half = ticket[:half_length]
        second_half = ticket[half_length:]

        for i in range(len(valid_symbols)):
            count_one = first_half.count(valid_symbols[i])
            count_two = second_half.count(valid_symbols[i])

            if count_one == 10 and count_two == 10:
                return f'ticket {ticket}" - 10$ Jackpot!'
            elif count_one >= 6 and count_two >= 6:
                return f'ticket {ticket}" - 6$'
        return f'ticket {ticket}" - no match'


    for ticket in ticket_list:
        ticket = ''.join(ticket)
        if valid_ticket(ticket) == True:
            print(winning_ticket(ticket))
        else:
            print("invalid ticket")
