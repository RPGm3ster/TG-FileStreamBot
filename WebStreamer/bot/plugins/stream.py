import logging
from pyrogram import filters, errors
from WebStreamer.vars import Var
from urllib.parse import quote_plus
from WebStreamer.bot import StreamBot, logger
from WebStreamer.utils import get_hash, get_name
from pyrogram.enums.parse_mode import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@StreamBot.on_message(
    filters.private
    & (
        filters.document
        | filters.video
        | filters.audio
        | filters.animation
        | filters.voice
        | filters.video_note
        | filters.photo
        | filters.sticker
    ),
    group=4,
)
async def media_receive_handler(_, m: Message):
    user = m.from_user
    if Var.ALLOWED_USERS and not ((str(user.id) in Var.ALLOWED_USERS) or (user.username in Var.ALLOWED_USERS)):
        return await m.reply("You are not <b>allowed to use</b> this <a href='https://github.com/EverythingSuckz/TG-FileStreamBot'>bot</a>.", quote=True)

    if Var.UPDATES_CHANNEL:
        try:
            user = await StreamBot.get_chat_member(
                chat_id=Var.UPDATES_CHANNEL,
                user_id=user.id,
            )
            if user.status == "kicked":
                return await m.reply("Sorry, you are banned to use me.", quote=True)
        except errors.UserNotParticipant:
            return await m.reply(
                f"**الرجاء الانظمام الى الثناة:** {Var.UPDATES_CHANNEL} **ليعمل البوت!**\n\n"
                f"بل انظمام الى القناة البوت سوف تستلم كافة التحديثات.",
                parse_mode="markdown",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🤖 انظم الى القناة ليعمل البوت 🤖", url=Var.UPDATES_CHANNEL)
                        ]
                    ]
                ),
                quote=True,
            )
    log_msg = await m.forward(chat_id=Var.BIN_CHANNEL)
    file_hash = get_hash(log_msg, Var.HASH_LENGTH)
    stream_link = f"{Var.URL}{log_msg.id}/{quote_plus(get_name(m))}?hash={file_hash}"
    short_link = f"{Var.URL}{file_hash}{log_msg.id}"
    logger.info(f"Generated link: {stream_link} for {m.from_user.first_name}")
    try:
        await m.reply_text(
            text="<code>{}</code>\n(<a href='{}'>shortened</a>)".format(
                stream_link, short_link
            ),
            quote=True,
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Open", url=stream_link)]]
            ),
        )
    except errors.ButtonUrlInvalid:
        await m.reply_text(
            text="<code>{}</code>\n\nshortened: {})".format(
                stream_link, short_link
            ),
            quote=True,
            parse_mode=ParseMode.HTML,
        )
