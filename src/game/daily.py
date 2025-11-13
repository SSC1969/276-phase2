from datetime import date, timedelta

from country import Country, get_country, get_random_country

from phase2.statistics import RoundStatistics


def get_daily_country() -> Country:
    """
    Gets a country for today's date, deterministically
    """
    country = get_random_country()
    return country


def handle_guess(input: str) -> bool:
    """
    Processes the given input, returning True if the guess was valid
    or False otherwise. Ends the game if either end condition is reached
    (reached max guesses or guessed correctly)
    """
    country = get_country(input)

    if not country:
        return False

    # hand country off to other gameplay functions

    pass


def compare_countries(guess: Country, answer: Country):
    """
    Check if the two countries, match.
    If not, compare the following statistics for two countries:
    - Population
    - Geographical Size
    - Currencies
    - Languages
    - Timezones
    - Region
    """
    pass


def end_game(won: bool, mode: str = "daily"):
    """
    End the game in either a win or a loss, and pass this game's statistics
    on to be processed in statistics.py, and show a breakdown of this game's
    stats to the user
    """

    # TODO (milestone 2): Get the user id of the currently playing user, if there is one

    # TODO: Get this round's stats properly
    round_time: timedelta = timedelta()
    round_guesses: int = 0

    round_stats = RoundStatistics(
        time_to_complete=round_time, won=won, guesses=round_guesses, mode=mode
    )

    if mode == "daily":
        round_stats.daily_date = date.today()

    # TODO: Add round to the rounds database

    # TODO: Show game stats in UI
