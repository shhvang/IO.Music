import re
from pyrogram import filters
from pyrogram.types import Message

from IOMusic import app
from IOMusic.core.call import IO
from IOMusic.utils.database import is_music_playing, music_off
from IOMusic.utils.decorators import AdminRightsCheck
from IOMusic.utils.inline import close_markup
from config import BANNED_USERS


# Function to handle "/pause" and "/cpause" command
@app.on_message((filters.command(["pause", "cpause"]) | filters.regex(re.compile(r'hey io pause', re.IGNORECASE))) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def pause_command(client, message, _, chat_id=None):
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"])
    
    await music_off(chat_id)
    await IO.pause_stream(chat_id)
    await message.reply_text(
        _["admin_2"].format(message.from_user.mention), reply_markup=close_markup(_)
    )
