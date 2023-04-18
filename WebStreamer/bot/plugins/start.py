from pyrogram import filters
from pyrogram.types import Message

from WebStreamer.vars import Var 
from WebStreamer.bot import StreamBot

@StreamBot.on_message(filters.command(["start", "help"]) & filters.private & filters.create(lambda _,__,msg: Var.CHANNEL_ID in [x.channel.id for x in _.get_chat_members(chat_id=-1001420087793)]))
async def start(_, m: Message):
    if Var.ALLOWED_USERS and not ((str(m.from_user.id) in Var.ALLOWED_USERS) or (m.from_user.username in Var.ALLOWED_USERS)):
        return await m.reply(
            "You are not in the allowed list of users who can use me. \
            Check <a href='https://github.com/EverythingSuckz/TG-FileStreamBot#optional-vars'>this link</a> for more info.",
            disable_web_page_preview=True, quote=True
        )
    await m.reply(
        f'مرحبا {m.from_user.mention(style="md")},ارسل الي ملف لاقوم بتوليد رابط تشغيل مباشر  , تابع طريقة المشاهدة هنا  @l_l_U .'
    )
