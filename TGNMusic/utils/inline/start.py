from pyrogram.types import InlineKeyboardButton

import config
from TGNMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["Recruit Me"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["Support"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["Recruit Me"],
                url=f"https://t.me/{app.username}?startgroup=true"),
            InlineKeyboardButton(text=_["Commands"], callback_data="settings_back_helper")
        ],
        [
            InlineKeyboardButton(text=_["Developer"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_["Support"], url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text=_["Opacity"], url=f"https://t.me/iopacity")
        ]
    ]
    return buttons
