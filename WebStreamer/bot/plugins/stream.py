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
        return await m.reply("You are not allowed to use this bot.", quote=True)

    # Forward user info along with the media to the BIN_CHANNEL
    forward_message = await m.forward(chat_id=Var.BIN_CHANNEL)
    
    # Add user information to the forwarded message
    user_info_text = (
        f"👤 User Info:\n"
        f"Name: {user.first_name}\n"
        f"Username: @{user.username}\n"
        f"User ID: {user.id}"
    )
    await forward_message.reply_text(user_info_text, quote=True)

    file_hash = get_hash(forward_message, Var.HASH_LENGTH)
    stream_link = f"{Var.URL}{forward_message.id}/{quote_plus(get_name(m))}?hash={file_hash}"
    short_link = f"{Var.URL}{file_hash}{forward_message.id}"
    logger.info(f"Generated link: {stream_link} for {m.from_user.first_name}")
    
    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔗 Open Stream", url=stream_link)],
        [InlineKeyboardButton("🌐 Short Link", url=short_link)]
    ])

    try:
        await m.reply_text(
            text=f"📽️ Your media is ready for streaming!\n\n{stream_link}\n\n"
                 f"<i>Your short link:</i> {short_link}",
            quote=True,
            parse_mode=ParseMode.HTML,
            reply_markup=reply_markup,
        )
    except errors.ButtonUrlInvalid:
        await m.reply_text(
            text=f"📽️ Your media is ready for streaming!\n\n{stream_link}\n\n"
                 f"<i>Your short link:</i> {short_link}",
            quote=True,
            parse_mode=ParseMode.HTML,
        )
        
