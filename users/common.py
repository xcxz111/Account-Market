from telegram import User
import enum


class UserType(enum.Enum):
    """User type enumeration

    """
    ADMIN = 0
    USER = 1


def is_admin(user: User) -> bool:
    """
    Check is user admin

    :param user:
    :type user:
    :return:
    """
    return True  # TODO: replace with actual implementation
