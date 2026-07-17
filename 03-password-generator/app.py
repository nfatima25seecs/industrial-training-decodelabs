"""
Secure Random Password Generator
DecodeLabs Industrial Training Kit | Project 3

Built to the enterprise guidance in the brief:
  - secrets (CSPRNG) instead of random. The random module uses the Mersenne
    Twister, which is deterministic and often seeded from system time, so its
    output is predictable and unfit for credentials.
  - string module for character pools, not hand-typed arrays.
  - list + ''.join() instead of += in a loop. Strings are immutable, so += keeps
    allocating new objects (O(n^2)); building a list and joining once is O(n).
  - entropy reported as E = L * log2(R).
"""

import math
import secrets
import string

# Cryptographically secure shuffler: pulls from os.urandom, not Mersenne Twister.
_secure_random = secrets.SystemRandom()


def get_int(prompt, minimum, maximum):
    """Phase 1: capture and validate the target length. Input is the first point
    of failure, so loop until we get a clean integer inside [minimum, maximum].
    The ceiling matters: without it, a huge number tries to build an impossibly
    long string and hangs the program."""
    while True:
        raw = input(prompt).strip()
        if not raw.isdigit():
            print("  Please enter a whole number.")
            continue
        value = int(raw)
        if value < minimum:
            print(f"  Length must be at least {minimum}.")
            continue
        if value > maximum:
            print(f"  Length must be {maximum} or less. Anything beyond that adds no real security.")
            continue
        return value


def ask_yes_no(prompt, default=True):
    hint = "Y/n" if default else "y/N"
    raw = input(f"{prompt} ({hint}): ").strip().lower()
    return default if not raw else raw.startswith("y")


def build_pools(use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    """Return the selected character classes, sourced from the string module."""
    pools = []
    if use_lower:
        pools.append(string.ascii_lowercase)
    if use_upper:
        pools.append(string.ascii_uppercase)
    if use_digits:
        pools.append(string.digits)
    if use_symbols:
        pools.append(string.punctuation)
    if not pools:
        raise ValueError("At least one character class must be enabled.")
    return pools


def generate_password(length, pools, guarantee_each=True):
    """Phase 2: turn a length integer into a complex string.

    With guarantee_each on, seed one character from every selected class, fill
    the rest from the combined pool, then securely shuffle so the guaranteed
    characters aren't pinned to the front.
    """
    combined = "".join(pools)
    if length < len(pools):
        raise ValueError("Length is smaller than the number of character classes.")

    chars = [secrets.choice(pool) for pool in pools] if guarantee_each else []
    while len(chars) < length:
        chars.append(secrets.choice(combined))

    _secure_random.shuffle(chars)          # secure shuffle, not random.shuffle
    return "".join(chars), len(combined)   # join once: O(n), not O(n^2)


def entropy_bits(length, pool_size):
    """Phase 3: E = L * log2(R)."""
    return length * math.log2(pool_size)


def strength_label(bits):
    if bits < 28:
        return "very weak"
    if bits < 40:
        return "weak"
    if bits < 70:
        return "reasonable"
    if bits < 110:
        return "strong"
    return "very strong"


def main():
    print("Secure Password Generator\n")
    length = get_int("Password length (16 to 128, 16+ recommended): ", minimum=4, maximum=128)
    use_symbols = ask_yes_no("Include symbols?", default=True)

    pools = build_pools(use_symbols=use_symbols)
    password, pool_size = generate_password(length, pools)
    bits = entropy_bits(length, pool_size)

    print(f"\nPassword: {password}")
    print(f"Pool size (R): {pool_size} characters")
    print(f"Entropy (E = L x log2 R): {bits:.1f} bits  ->  {strength_label(bits)}")

    if length < 16:
        print("\nNote: the brief and NIST 2024 favor length. Consider 16+.")


if __name__ == "__main__":
    main()