from pyrogram.types import InlineKeyboardButton

import config
from TGNMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="Recruit Me", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text="Support", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text="Recruit Me", url=f"https://t.me/{app.username}?startgroup=true"),
            InlineKeyboardButton(text="Commands", callback_data="settings_back_helper"),
        ],
        [
            InlineKeyboardButton(text="Developer", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="Support", url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text="Opacity", url=f"https://t.me/iopacity"),
        ]
    ]
    return buttons
