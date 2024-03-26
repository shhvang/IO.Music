from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="Pause",
            description=f"Pause the ongoing track",
            thumb_url="https://telegra.ph/file/8614d3234c8ad55dd348d.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="Resume",
            description=f"Resume the paused stream",
            thumb_url="https://telegra.ph/file/63232848f8ae2e2057ede.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="Skip",
            description=f"Skip the ongoing track",
            thumb_url="https://telegra.ph/file/b7eeb38b47b4f1b565a18.jpg",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="End",
            description="End the queue",
            thumb_url="https://telegra.ph/file/88e3a1713cdf64f2287b4.jpg",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="Shuffle",
            description="Shuffle the queued tracks",
            thumb_url="https://telegra.ph/file/7b05b1005d65e1a9b5c0b.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="Loop",
            description="Loop/Repeat the ongoing stream ",
            thumb_url="https://telegra.ph/file/6e9d4b28afe792e249fa0.jpg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
