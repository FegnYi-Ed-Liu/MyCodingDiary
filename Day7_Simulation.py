import numpy as np
import scipy.stats as st

deck_of_cards = \
    [('Heart', 0), ('Heart', 1), ('Heart', 2), ('Heart', 3), ('Heart', 4),
     ('Heart', 5), ('Heart', 6), ('Heart', 7), ('Heart', 8),
     ('Heart', 9), ('Heart', 10), ('Heart', 11), ('Heart', 12),
     ('Club', 0), ('Club', 1), ('Club', 2), ('Club', 3),
     ('Club', 4), ('Club', 5), ('Club', 6), ('Club', 7),
     ('Club', 8), ('Club', 9), ('Club', 10), ('Club', 11),
     ('Club', 12), ('Spade', 0), ('Spade', 1), ('Spade', 2),
     ('Spade', 3), ('Spade', 4), ('Spade', 5), ('Spade', 6),
     ('Spade', 7), ('Spade', 8), ('Spade', 9), ('Spade', 10),
     ('Spade', 11), ('Spade', 12), ('Diamond', 0), ('Diamond', 1),
     ('Diamond', 2), ('Diamond', 3), ('Diamond', 4), ('Diamond', 5),
     ('Diamond', 6), ('Diamond', 7), ('Diamond', 8), ('Diamond', 9),
     ('Diamond', 10), ('Diamond', 11), ('Diamond', 12)]

# Shuffle the deck
np.random.shuffle(deck_of_cards)

# Print out the top three cards
card_choices_after_shuffle = deck_of_cards[0:3]
print(card_choices_after_shuffle)

# Shuffle deck & count card occurrences in the hand
n_sims, two_kind = 10000, 0
for i in range(n_sims):
    np.random.shuffle(deck_of_cards)
    hand, cards_in_hand = deck_of_cards[0:5], {}
    for [suite, numeric_value] in hand:
        # Count occurrences of each numeric value
        cards_in_hand[numeric_value] = cards_in_hand.get(numeric_value, 0) + 1

    # Condition for getting at least 2 of a kind
    if max(cards_in_hand.values()) >= 2:
        two_kind += 1

print("Probability of seeing at least two of a kind = {} ".format(two_kind / n_sims))

# Initialize model parameters & simulate dice throw
die, probabilities, num_dice = [1, 2, 3, 4, 5, 6], [1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6], 2
sims, wins = 100, 0

for i in range(sims):
    outcomes = np.random.choice(die, size=num_dice, p=probabilities)
    # Increment `wins` by 1 if the dice show same number
    if outcomes[0] == outcomes[1]:
        wins = wins + 1

print("In {} games, you win {} times".format(sims, wins))

# Pre-defined constant variables
lottery_ticket_cost, num_tickets, grand_prize = 10, 1000, 10000

# Probability of winning
chance_of_winning = 1 / num_tickets

# Simulate a single drawing of the lottery
gains = [-lottery_ticket_cost, grand_prize - lottery_ticket_cost]
probability = [1 - chance_of_winning, chance_of_winning]
outcome = np.random.choice(a=gains, size=1, p=probability, replace=True)

print("Outcome of one drawing of the lottery is {}".format(outcome))

# Draw a sample of birthdays & check if each birthday is unique
days = np.arange(1, 366)
ppl = 2


def birthday_sim(people):
    sims, unique_birthdays = 2000, 0
    for _ in range(sims):
        draw = np.random.choice(days, size=people, replace=True)
        if len(draw) == len(set(draw)):
            unique_birthdays += 1
    out = 1 - unique_birthdays / sims
    return out


# Break out of the loop if probability greater than 0.5
while ppl > 0:
    prop_bds = birthday_sim(ppl)
    if prop_bds > 0.5:
        break
    ppl += 1

print("With {} people, there's a 50% chance that two share a birthday.".format(ppl))

wrench_lengths = np.array([8.9143694, 10.99734545, 10.2829785, 8.49370529, 9.42139975,
                           11.65143654, 7.57332076, 9.57108737, 11.26593626, 9.1332596,
                           9.32111385, 9.90529103, 11.49138963, 9.361098, 9.55601804,
                           9.56564872, 12.20593008, 12.18678609, 11.0040539, 10.3861864,
                           10.73736858, 11.49073203, 9.06416613, 11.17582904, 8.74611933,
                           9.3622485, 10.9071052, 8.5713193, 9.85993128, 9.1382451,
                           9.74438063, 7.20141089, 8.2284669, 9.30012277, 10.92746243,
                           9.82636432, 10.00284592, 10.68822271, 9.12046366, 10.28362732,
                           9.19463348, 8.27233051, 9.60910021, 10.57380586, 10.33858905,
                           9.98816951, 12.39236527, 10.41291216, 10.97873601, 12.23814334,
                           8.70591468, 8.96121179, 11.74371223, 9.20193726, 10.02968323,
                           11.06931597, 10.89070639, 11.75488618, 11.49564414, 11.06939267,
                           9.22729129, 10.79486267, 10.31427199, 8.67373454, 11.41729905,
                           10.80723653, 10.04549008, 9.76690794, 8.80169886, 10.19952407,
                           10.46843912, 9.16884502, 11.16220405, 8.90279695, 7.87689965,
                           11.03972709, 9.59663396, 9.87397041, 9.16248328, 8.39403724,
                           11.25523737, 9.31113102, 11.66095249, 10.80730819, 9.68524185,
                           8.9140976, 9.26753801, 8.78747687, 12.08711336, 10.16444123,
                           11.15020554, 8.73264795, 10.18103513, 11.17786194, 9.66498924,
                           11.03111446, 8.91543209, 8.63652846, 10.37940061, 9.62082357])

# Draw some random sample with replacement and append mean to mean_lengths.
mean_lengths, sims = [], 1000
for i in range(sims):
    temp_sample = np.random.choice(wrench_lengths, replace=True, size=len(wrench_lengths))
    sample_mean = np.mean(temp_sample)
    mean_lengths.append(sample_mean)

# Calculate bootstrapped mean and 95% confidence interval.
boot_mean = np.mean(mean_lengths)
boot_95_ci = np.percentile(mean_lengths, [2.5, 97.5])
print("Bootstrapped Mean Length = {}, 95% CI = {}".format(boot_mean, boot_95_ci))

# Initialize effect_size, control_mean, control_sd
effect_size, sample_size, control_mean, control_sd = 0.05, 50, 1, 0.5

# Simulate control_time_spent and treatment_time_spent, assuming equal variance
control_time_spent = np.random.normal(loc=control_mean, scale=control_sd, size=sample_size)
treatment_time_spent = np.random.normal(loc=control_mean * (1 + effect_size), scale=control_sd, size=sample_size)

# Run the t-test and get the p_value
t_stat, p_value = st.ttest_ind(treatment_time_spent, control_time_spent)
stat_sig = p_value < 0.05
print("P-value: {}, Statistically Significant? {}".format(p_value, stat_sig))

sample_size = 50

# Keep incrementing sample size by 10 till we reach required power
while 1:
    control_time_spent = np.random.normal(loc=control_mean, scale=control_sd, size=(sample_size, sims))
    treatment_time_spent = np.random.normal(loc=control_mean * (1 + effect_size), scale=control_sd,
                                            size=(sample_size, sims))
    t, p = st.ttest_ind(treatment_time_spent, control_time_spent)

    # Power is the fraction of times in the simulation when the p-value was less than 0.05
    power = (p < 0.05).sum() / sims
    if power > 0.8:
        break
    else:
        sample_size += 10
print("For 80% power, sample size required = {}".format(sample_size))
