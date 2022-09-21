import telegram
from django.core.management.base import BaseCommand
import re
from django.conf import settings
import logging
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, filters, MessageHandler

from bot.models import Bot, Channel

class Command(BaseCommand):

    def handle(self, *args, **options):
        logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            level=logging.INFO
        )
        token = Bot.objects.get(name=settings.BOT_NAME).token
        channels = []
        for channel in Channel.objects.all():
            channels.append(channel)

        async def repost(update, context):
            for channel in channels:
                if channel.telegram_id == update.effective_chat.id:
                    continue

                print(update)

                if update.channel_post.text_markdown_v2:
                    message = update.channel_post.text_markdown_v2.replace(
                        channel.username_alias[0], channel.username_alias[1]).replace(
                        channel.promo_replacement[0], channel.promo_replacement[1])
                    await context.bot.send_message(chat_id=channel.telegram_id, text=message, parse_mode=telegram.constants.ParseMode.MARKDOWN_V2)
                elif update.channel_post.caption:
                    caption = update.channel_post.caption.replace(
                        channel.username_alias[0], channel.username_alias[1])
                    await context.bot.copy_message(
                        chat_id=channel.telegram_id, message_id=update.effective_message.id, from_chat_id=update.effective_chat.id, caption=caption)
                else:
                    await context.bot.copy_message(
                        chat_id=channel.telegram_id, message_id=update.effective_message.id, from_chat_id=update.effective_chat.id)


        application = ApplicationBuilder().token(token).build()
        repost_handler = MessageHandler(filters.ALL, repost)
        application.add_handler(repost_handler)
        application.run_polling()

# maybe this function is good idea, maybe not...
"""
        async def repost(update, context):
            for channel in channels:
                print(update)
                if channel.telegram_id != update.effective_chat.id:
                    message = update.channel_post.text
                    try:
                        pin_username = re.search("(?<!\w)@\w+", message).group()
                        if pin_username == "@Vijaysignal":
                            message = message.replace(pin_username, '@UsernameReplasement')
                    except AttributeError:
                        pass
                    await context.bot.send_message(chat_id=channel.telegram_id, text=message)
"""