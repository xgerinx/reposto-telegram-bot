from django.contrib import admin

from bot.models import Bot, OutputChannel, UsernameReplacement, PromocodeReplacement, InputChannel


class UsernameReplacementInline(admin.TabularInline):
    model = UsernameReplacement
    extra = 1


class PromocodeReplacementInline(admin.TabularInline):
    model = PromocodeReplacement
    extra = 1


class ChannelAdmin(admin.ModelAdmin):
    fields = ['title', 'telegram_id', 'bot', 'external_link', 'pin_message_link']
    readonly_fields = ['title', 'telegram_id', 'bot']
    inlines = [
        UsernameReplacementInline,
        PromocodeReplacementInline
    ]


class InputChannelInline(admin.TabularInline):
    model = InputChannel
    extra = 1


class RepostChannelInline(admin.TabularInline):
    model = OutputChannel
    extra = 1
    fields = ['title', 'telegram_id']


class BotAdmin(admin.ModelAdmin):
    inlines = [
        InputChannelInline,
        RepostChannelInline
    ]


admin.site.register(Bot, BotAdmin)
admin.site.register(OutputChannel, ChannelAdmin)
