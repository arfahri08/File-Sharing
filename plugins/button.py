# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from config import FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL1, FORCE_SUB_CHANNEL2, FORCE_SUB_GRUP 
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if not FORCE_SUB_CHANNEL and not FORCE_SUB_CHANNEL1, FORCE_SUB_CHANNEL2, FORCE_SUB_GRUP:
        buttons = [
            [
                InlineKeyboardButton(text="Bantuan", callback_data="help"),
                InlineKeyboardButton(text="Tutup", callback_data="close"),
            ],
        ]
        return buttons
    if not FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL1 and not FORCE_SUB_CHANNEL2, FORCE_SUB_GRUP:
        buttons = [
            [
                InlineKeyboardButton(text="CHANNEL 2", url=client.invitelink2),
                InlineKeyboardButton(text="GRUP 1", url=client.invitelink2)
            ],
            [
                InlineKeyboardButton(text="Bantuan", callback_data="help"),
                InlineKeyboardButton(text="Tutup", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="Channel 1", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
                InlineKeyboardButton(text="ᴛᴜᴛᴜᴘ", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="BANTUAN", callback_data="help"),
            ],
            [
                InlineKeyboardButton(text="CHANNEL", url=client.invitelink),
                InlineKeyboardButton(text="GRUP", url=client.invitelink2),
            ],
            [InlineKeyboardButton(text="TUTUP", callback_data="close")],
        ]
        return buttons


def fsub_button(client, message):
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="JOIN GRUP", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="COBA LAGI",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="JOIN CHANNEL", url=client.invitelink),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="COBA LAGI",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
                InlineKeyboardButton(text="ᴊᴏɪɴ ɢʀᴏᴜᴘ", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
