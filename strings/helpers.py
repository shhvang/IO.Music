HELP_1 = """<b><u>Admin Commands -</b></u>

Just add a letter <b>ᴄ</b> in the start of the regular commands to be able to use them in channels.

/pause : pause the track
/resume : resume the track
/skip : skip to the next track
/skip <number> : skip to the particular track in queue
/end ᴏʀ /stop : clears the queue and ends the stream
/player : get an interactive player panel
/queue : shows the track queue
"""

HELP_2 = """
<b><u>Auth Users -</b></u>

Authorized users can mimic admin commands, they don't need to be chat admin.

/auth [username/userid] : authorize a user
/unauth [ᴜsᴇʀɴᴀᴍᴇ/ᴜsᴇʀ_ɪᴅ] : (un)authorize a user
/authusers : shows the list of authorized users 
"""

HELP_3 = """
<u><b>Broadcast Feature</b></u> [ᴏɴʟʏ ғᴏʀ sᴜᴅᴏᴇʀs] :

/broadcast [Message or reply to a Message] : Broadcast a message to served chats of the bot.

<u>Broadcasting Modes -</u>
<b>-pin</b> : pins your broadcasted message in served chats
<b>-pinloud</b> : pins the message with notification 
<b>-user</b> : broadcasts the message to users who have started the bot
<b>-assistant</b> : broadcast your message from the assistant account of the bot
<b>-nobot</b> : forces the bot to not broadcast the message

<b>Example:</b> <code>/broadcast -user -assistant -pin Testing Broadcast</code>
"""

HELP_4 = """<u><b>Chat Blacklist Feature -</b></u> [ᴏɴʟʏ ғᴏʀ sᴜᴅᴏᴇʀs]

Restricting selected chats (if required) from using our bot.

/blacklistchat [ᴄʜᴀᴛ ɪᴅ] : blacklist a chat
/whitelistchat [ᴄʜᴀᴛ ɪᴅ] : whitelist a chat 
/blacklistedchat : shows the list of blacklisted chats
"""

HELP_5 = """
<u><b>Block Users -</b></u> [ᴏɴʟʏ ғᴏʀ sᴜᴅᴏᴇʀs]

Restricting selected users (if required) from using the bot and its functions.

/block [ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴜsᴇʀ] : block a user
/unblock [ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴜsᴇʀ] : unblock a user
/blockedusers : shows the list of blocked users
"""

HELP_6 = """
<u><b>Channel Play Commands -</b></u>

You can stream audio/video in a channel.

/cplay : plays the requested track in Channel's VC.
/cvplay : streams the requested video track in Channel's VC 
/cplayforce or /cvplayforce : stops the ongoing stream and plays the requested track

/channelplay [ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ɪᴅ] or [ᴅɪsᴀʙʟᴇ] : connect channel to a group and start playing tracks from the group.
"""

HELP_7 = """
<u><b>Global Ban Feature -</b></u> [ᴏɴʟʏ ғᴏʀ sᴜᴅᴏᴇʀs] :

/gban [ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴜsᴇʀ] : globally bans the user from using the bot
/ungban [ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴩʟʏ ᴛᴏ ᴀ ᴜsᴇʀ] : globally unbans the user
/gbannedusers : shows the current list of <b>Globally Banned Users</b>
"""

HELP_8 = """
<b><u>Loop Stream -</b></u>

<b>Starts streaming the ongoing stream on loop.</b>

/loop [enable/disable] : enable/disable loop in your chat
/loop [1, 2, 3, ...] : enables the loop (n) number of times
"""

HELP_9 = """
<u><b>Maintenance Mode -</b></u> [ᴏɴʟʏ ғᴏʀ sᴜᴅᴏᴇʀs] :

/logs : get logs of the bot

/logger [ᴇɴᴀʙʟᴇ/ᴅɪsᴀʙʟᴇ] : bot will start logging the activities happening with the bot

/maintenance [ᴇɴᴀʙʟᴇ/ᴅɪsᴀʙʟᴇ] : enable/disable maintenance mode
"""

HELP_10 = """
<b><u>Ping / Stats -</b></u>

/start : starts the bot
/help : get help with explanation of commands

/ping : ping the bot

/stats : shows the stats of the bot
"""

HELP_11 = """
<u><b>Play Commands -</b></u>

<b>v :</b> stands for video play
<b>force :</b> stands for force play

/play ᴏʀ /vplay : starts streaming the requested track in VC

/playforce ᴏʀ /vplayforce : stops the ongoing stream and plays the requested track in VC
"""

HELP_12 = """
<b><u>Shuffle / Queue -</b></u>

/shuffle : shuffle the queue
/queue : shows the queue
"""

HELP_13 = """
<b><u>Seek Stream -</b></u>

/seek [ᴅᴜʀᴀᴛɪᴏɴ ɪɴ sᴇᴄᴏɴᴅs] : seek the stream to the desired duration 
/seekback [ᴅᴜʀᴀᴛɪᴏɴ ɪɴ sᴇᴄᴏɴᴅs] : seekback the stream to the desired duration 
"""

HELP_14 = """
<b><u>Song Download -</b></u>

/song [sᴏɴɢ ɴᴀᴍᴇ/ʏᴛ ᴜʀʟ] : download any track from youtube in mp3/mp4 format
"""

HELP_15 = """
<b><u>Speed Commands -</b></u>

You can control the playback speed of the ongoing stream [ᴀᴅᴍɪɴs ᴏɴʟʏ].

/speed or /playback : for adjusting the audio playback speed in group
/cspeed or /cplayback : for adjusting the audio playback speed in channel
"""
