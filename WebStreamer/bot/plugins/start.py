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
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"**Nᴇᴡ Usᴇʀ Jᴏɪɴᴇᴅ:** \n\n__Mʏ Nᴇᴡ Fʀɪᴇɴᴅ__ [{m.from_user.first_name}](tg://user?id={m.from_user.id}) __Sᴛᴀʀᴛᴇᴅ Yᴏᴜʀ Bᴏᴛ !!__"
        )
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
                ),
                
            )
   await m.reply(
        f'مرحبا {m.from_user.mention(style="md")},ارسل الي ملف لاقوم بتوليد رابط تشغيل مباشر  , تابع طريقة المشاهدة هنا  @l_l_U .')
    
    )
