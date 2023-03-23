# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from pyrogram import filters
from pyrogram.types import Message

from WebStreamer.vars import Var 
from WebStreamer.bot import StreamBot
from pyrogram import filters, Client
from pyrogram.errors import UserNotParticipant
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from WebStreamer.utils.database import Database
db = Database(Var.DATABASE_URL, Var.name)


@StreamBot.on_message(filters.command(["start", "help"]) & filters.private)
async def start(_, m: Message):
    if Var.ALLOWED_USERS and not ((str(m.from_user.id) in Var.ALLOWED_USERS) or (m.from_user.username in Var.ALLOWED_USERS)):
        return await m.reply(
            "You are not in the allowed list of users who can use me. \
            Check <a href='https://github.com/EverythingSuckz/TG-FileStreamBot#optional-vars'>this link</a> for more info.",
            disable_web_page_preview=True, quote=True
        )
    await m.reply(
        f'مرحبا {m.from_user.mention(style="md")},ارسل الي ملف لاقوم بتوليد رابط تشغيل مباشر  , تابع طريقة المشاهدة هنا  @l_l_U .')
    
    ),
    
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await Client.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == "kicked":
                await Client.send_message(
                    chat_id=m.chat.id,
                    text="You are banned!\n\n  **Cᴏɴᴛᴀᴄᴛ Dᴇᴠᴇʟᴏᴘᴇʀ [MARDUK](https://t.me/AKKK7) ʜᴇ Wɪʟʟ Hᴇʟᴘ Yᴏᴜ**",
                    
                    disable_web_page_preview=True
                )
                return 
        except UserNotParticipant:
            await Client.send_message(
                chat_id=m.chat.id,
                text="""<i>🔐انظم الى القناة ليعمل البوت🔐</i>""",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("انظم الان 🔓", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                )
