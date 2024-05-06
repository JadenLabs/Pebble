import math


def experience_for_level(level: int, multiplier: int) -> int:
    return multiplier * level**2


def level_for_experience(experience: int, multiplier: int) -> int:
    return math.sqrt(experience / multiplier)


def cooldown_grace(
    seconds_since_last_message: int, strictness: int, cooldown: int
) -> int:
    grace = strictness ** (seconds_since_last_message - 60)
    grace = 1 if grace > 1 else grace
    return grace


if __name__ == "__main__":
    xp = experience_for_level(5, 200)
    print(xp)
    level = level_for_experience(xp, 200)
    print(level)

    fair_message = cooldown_grace(60, 1.25, 60)
    print(fair_message)
    unfair_message = cooldown_grace(45, 1.25, 60)
    print(unfair_message)
