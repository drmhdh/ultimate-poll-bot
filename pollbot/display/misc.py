"""Display helper for misc stuff."""
from pollbot.i18n import i18n
from pollbot.models import Poll
from pollbot.telegram.keyboard import (
    get_help_keyboard,
    get_poll_list_keyboard,
)


def get_help_text_and_keyboard(user, current_category):
    """Create the help message depending on the currently selected help category."""
    categories = [
        "creation",
        "settings",
        "notifications",
        "management",
        "languages",
        "bugs",
        "feature",
    ]

    text = i18n.t(f"misc.help.{current_category}", locale=user.locale)
    keyboard = get_help_keyboard(user, categories, current_category)

    return text, keyboard


def get_poll_list(session, user, closed=False):
    """Get the a list of polls for the user."""
    polls = (
        session.query(Poll)
        .filter(Poll.user == user)
        .filter(Poll.created.is_(True))
        .filter(Poll.closed.is_(closed))
        .all()
    )

    if len(polls) == 0 and closed:
        return i18n.t("list.no_closed_polls", locale=user.locale), None
    elif len(polls) == 0:
        return i18n.t("list.no_polls", locale=user.locale), None

    text = i18n.t("list.polls", locale=user.locale)
    keyboard = get_poll_list_keyboard(polls)

    return text, keyboard
