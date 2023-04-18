from pyrogram import filters
from pyrogram.types import Message

from WebStreamer.vars import Var 
from WebStreamer.bot import StreamBot

@StreamBot.on_message(filters.command(["start", "help"]) & filters.private)
async def start(_, m: Message):
    if not await check_user_membership(m.from_user.id):
        await StreamBot.send_message(chat_id=m.chat.id, text=f"الرجاء الاشتراك في القناة {https://t.me/kekkkkk} لاستخدام البوت.", disable_web_page_preview=True)
        return
    if Var.ALLOWED_USERS and not ((str(m.from_user.id) in Var.ALLOWED_USERS) or (m.from_user.username in Var.ALLOWED_USERS)):
        return await m.reply(
            "You are not in the allowed list of users who can use me. \
            Check <a href='https://github.com/EverythingSuckz/TG-FileStreamBot#optional-vars'>this link</a> for more info.",
            disable_web_page_preview=True, quote=True
        )
    await m.reply(
        f'مرحبا {m.from_user.mention(style="md")},ارسل الي ملف لاقوم بتوليد رابط تشغيل مباشر  , تابع طريقة المشاهدة هنا  @l_l_U .'
    )

async def check_user_membership(user_id: int) -> bool:
    chat = await StreamBot.get_chat(chat_id=Var.CHANNEL_NAME)
    member = await StreamBot.get_chat_member(chat_id=chat.id, user_id=user_id)
    return member.status in ("creator", "administrator", "member")
