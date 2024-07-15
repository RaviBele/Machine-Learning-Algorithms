def repeating_heads(n, x):
    bet_size = 100
    head_chance = 1 / 2
    attempt_win_chance = head_chance**n
    attempt_lose_chance = 1 - attempt_win_chance
    repeating_lose_chance = attempt_lose_chance**x
    repeating_win_chance = 1 - repeating_lose_chance
    bet_payout = bet_size / repeating_win_chance
    return [repeating_win_chance*100, bet_payout]
