def entropy_to_years(entropy: float, guesses_per_second: int) -> int:
    """Calculate the number of years needed to guess a passphrase with the given entropy.

    Args:
        entropy (int): Entropy of the passphrase.
        guesses_per_second (int): Number of guesses per second.

    Returns:
        int: The approximate number of years need to guess the passphrase.
    """
    seconds = 2 ** (entropy - 1) / guesses_per_second
    seconds_per_year = 60 * 60 * 24 * 365.25
    years = int(seconds / seconds_per_year)
    return years


def flavour_text(entropy: float) -> str:

    guess_rate = 10_000_000_000
    # According to this stack overflow https://stackoverflow.com/questions/4764026/how-many-sha256-hashes-can-a-modern-computer-compute
    # you could do 622 million SHA2 hashes per second in 2012.
    # 10 billion seemed like a reasonable number in 2024 but it's not really based on much.

    years_to_guess = entropy_to_years(entropy, 10_000_000_000)
    flavour_text = f"It would take approximately {years_to_guess:,} years to guess this passphrase while guessing at a rate of {guess_rate:,} attempts per second."
    if years_to_guess < 1:
        flavour_text += "\nThat's not long enough! This passphrase is insecure!!"
    elif 1 <= years_to_guess < 250:
        flavour_text += "\nWhile that may seem like a lot, improvements in hardware over time may mean that your passphrase is vulnerable to a motivated attacker. We strongly recommend you use a stronger passphrase."
    elif 250 <= years_to_guess <= 500:
        flavour_text += "\nThat's longer than we've known about oxygen."
    elif 500 <= years_to_guess <= 2000:
        flavour_text += "\nThat's longer than we have known the Earth orbits the Sun."
    elif 2050 <= years_to_guess < 4500:
        flavour_text += "\nTo guess it today you would have had to have started before the birth of the Roman empire."
    elif 4500 <= years_to_guess < 11000:
        flavour_text += "\nTo guess it today you would have had to have started before the construction of the Pyramids of Giza!"
    elif 11000 <= years_to_guess < 300_000:
        flavour_text += "\nTo guess it today you would have had to have started before the founding of any known historical cities!"
    elif 300_000 <= years_to_guess < 65_000_000:
        flavour_text += "\nThat's longer than the Homo Sapiens have walked on Earth."
    elif 65_000_000 <= years_to_guess < 4_000_000_000:
        flavour_text += "\nTo guess it today you would have had to have started before the dinosaurs were wiped out by an asteroid!"
    elif 4_000_000_000 <= years_to_guess < 5_000_000_000:
        flavour_text += "\nTo guess it today you would have had to have started before life on earth began!"
    elif 4_000_000_000 <= years_to_guess < 5_000_000_000:
        flavour_text += "\nThis passphrase is unlikely to be guessed before the sun's increasing luminosity makes the Earth uninhabitable."
    elif 5_000_000_000 <= years_to_guess < 100_000_000_000:
        flavour_text += "\nThis passphrase is unlikely to be guessed before the sun's transformation into a red giant engulfs the Earth and everything in it."
    elif 10**11 <= years_to_guess < 10**100:
        flavour_text += "\nThis passphrase is unlikely to be guessed before the expansion of the universe due to dark energy causes the stars in the sky to blink out."
    else:
        flavour_text += "\nThis passphrase should withstand any attempts of guessing until the theoretical heat death of the universe."

    return flavour_text
