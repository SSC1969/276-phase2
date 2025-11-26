# tests/test_leaderboard_ui.py

from typing import Any, Dict, List

import pytest
from nicegui import ui
from nicegui.testing import User

# Load the NiceGUI user plugin without needing pytest.ini
pytest_plugins = ["nicegui.testing.user_plugin"]

from game import leaderboard_ui


@pytest.fixture(autouse=True)
def mock_fetch_leaderboard(monkeypatch: pytest.MonkeyPatch) -> None:
    """Provide deterministic leaderboard data for all tests in this file."""

    fake_rows: List[Dict[str, Any]] = [
        {
            "entry_id": 1,
            "user_id": 101,
            "daily_streak": 5,
            "longest_daily_streak": 8,
            "average_daily_guesses": 4,
            "average_daily_time": "32.0s",
            "longest_survival_streak": 12,
            "high_score": 1400,
            "rank": 1,
        },
        {
            "entry_id": 2,
            "user_id": 202,
            "daily_streak": 3,
            "longest_daily_streak": 6,
            "average_daily_guesses": 5,
            "average_daily_time": "40.5s",
            "longest_survival_streak": 9,
            "high_score": 1200,
            "rank": 2,
        },
    ]

    def fake_fetch() -> List[Dict[str, Any]]:
        return fake_rows

    # Replace the real backend call with our fake data
    monkeypatch.setattr(leaderboard_ui, "fetch_leaderboard", fake_fetch)


async def test_leaderboard_page_loads(user: User) -> None:
    """The leaderboard page should render with a title, table, and refresh button."""
    await user.open("/leaderboard")

    # These are visible according to the debug tree
    await user.should_see("Leaderboard")   # page title label
    await user.should_see("Refresh")       # refresh button label

    # Assert that a table component is present
    await user.should_see(kind=ui.table)


async def test_leaderboard_refresh_button_does_not_crash(user: User) -> None:
    """
    Clicking the Refresh button should keep the page usable.
    We don't assert on data; just that the UI is still there.
    """
    await user.open("/leaderboard")

    # Click the Refresh button by its label
    user.find("Refresh").click()

    # Page should still show the title and the table afterwards
    await user.should_see("Leaderboard")
    await user.should_see(kind=ui.table)
