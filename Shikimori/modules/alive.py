from Shikimori import ALIVE_MEDIA, UPDATE_CHANNEL, SUPPORT_CHAT, OWNER_USERNAME, dispatcher, NETWORK, NETWORK_USERNAME
from Shikimori.modules.disable import DisableAbleCommandHandler
from telegram import ParseMode, Update,InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

PHOTO = ALIVE_MEDIA

def awake(update: Update, context: CallbackContext):
    message = update.effective_message
    buttons = [
        [
        InlineKeyboardButton(
            text="Updates",
            url=f"https://t.me/{UPDATE_CHANNEL}"),
        InlineKeyboardButton(
            text="Support",
            url=f"https://t.me/{SUPPORT_CHAT}"),
        ],
     ]
    
    first_name = update.effective_user.first_name
    user = message.from_user

    TEXT = f"""
    <b>Hi <a href="tg://user?id={user.id}">{first_name}</a>, I'm Shikomori Robot.

⚪ I'm Working Properly

    """
    if NETWORK:
        TEXT = TEXT + f'\n⚪ <b>I am Powered by : <a href="https://t.me/{NETWORK_USERNAME}">{NETWORK}</a>\n\n' + 'Thanks For Adding Me Here ❤️</b>'
    
    else:
        TEXT = TEXT + "\n<b>Thanks For Adding Me Here ❤️</b>"

    message.reply_animation(PHOTO, caption=TEXT, reply_markup=InlineKeyboardMarkup(buttons),parse_mode=ParseMode.HTML)

ALIVE_HANDLER = DisableAbleCommandHandler("alive", awake, run_async=True)
dispatcher.add_handler(ALIVE_HANDLER)
__command_list__ = ["alive"]
__handlers__ = [
    ALIVE_HANDLER,
]

__mod_name__ = "Alive ✨"
__help__ = """
*ALIVE*
 ❍ `/alive` :Check BOT status
"""
