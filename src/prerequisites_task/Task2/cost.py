def total_token_cost(messages, token_cost=0.00025)->float:
    """ Calculate the total token cost for a list of messages"""
    total_cost = 0.0
    for i, message in enumerate(messages, start=1):
        total_cost += message["token_count"] * token_cost
    return total_cost