import numpy as np
rng = np.random.default_rng()


rank_totals = np.zeros(10000)
ranks = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])
card_deck = np.repeat(ranks, 4)

for i in np.arange(10000):
    cards = rng.choice(card_deck, size = 3)
    rank_total = np.sum(cards)
    if rank_total != 21:
        card_eq_1 = cards == 1
        cards[card_eq_1] = 11
        rank_total = np.sum(cards)
        rank_totals[i] = rank_total
    else:
        rank_totals[i] = rank_total

p_flex_total_21 = np.count_nonzero(rank_totals == 21) / 10000
print(p_flex_total_21)