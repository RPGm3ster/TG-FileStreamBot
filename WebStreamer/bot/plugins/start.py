from pyrogram import filters
from pyrogram.types import Message
from WebStreamer.vars import Var 
from WebStreamer.bot import StreamBot

@StreamBot.on_message(filters.command(["start", "help"]) & filters.private)
async def start(_, m: Message):
    if Var.UPDATES_CHANNEL:
        try:
            chat = await StreamBot.get_chat_member(Var.UPDATES_CHANNEL, m.from_user.id)
            if chat.status == "kicked":
                return await m.reply("عذراً، لا يمكنك استخدام هذا البوت. إذا كنت تريد الاستمرار في استخدامه، يرجى الاتصال بمشرف.")
        except UserNotParticipant:
            return await m.reply(f"**يرجى الانضمام إلى قناة التحديثات الخاصة بنا أولاً:**\n\n{Var.UPDATES_CHANNEL}\n\nبعد الانضمام إلى القناة، يمكنك استخدام هذا البوت.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("أضغط هنا للانضمام", url=f"t.me/{Var.UPDATES_CHANNEL}")]]))
        except Exception:
            return await m.reply("عذرًا، حدث خطأ غير معروف. يرجى إعادة المحاولة في وقت لاحق.")
    if Var.ALLOWED_USERS and not ((str(m.from_user.id) in Var.ALLOWED_USERS) or (m.from_user.username in Var.ALLOWED_USERS)):
        return await m.reply(
            "You are not in the allowed list of users who can use me. \
            Check <a href='https://github.com/EverythingSuckz/TG-FileStreamBot#optional-vars'>this link</a> for more info.",
            disable_web_page_preview=True, quote=True
        )
    await m.reply(
        f'مرحبا {m.from_user.mention(style="md")},ارسل الي ملف لاقوم بتوليد رابط تشغيل مباشر  , تابع طريقة المشاهدة هنا  @l_l_U .'
    )
