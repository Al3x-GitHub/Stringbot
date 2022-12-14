from pyrogram.types import Message
from pyrogram import Client, filters

from env import OWNER_ID
from StringGenBot.db import SESSION
from StringGenBot.db.users_sql import Users, num_users


@Client.on_message(~filters.service, group=1)
async def users_sql(_, msg: Message):
    if msg.from_user:
        q = SESSION.query(Users).get(int(msg.from_user.id))
        if not q:
            SESSION.add(Users(msg.from_user.id))
            SESSION.commit()
        else:
            SESSION.close()


@Client.on_message(filters.user(OWNER_ID) & filters.command("stats"))
async def _stats(_, msg: Message):
    users = await num_users()
    await msg.reply(f"ยป ๐๐ฎ๐ซ๐ซ๐๐ง๐ญ ๐๐ญ๐๐ญ๐ฌ ๐๐ ๐๐ญ๐ซ๐ข๐ง๐  ๐๐๐ง. ๐๐จ๐ญ :\n\n {users} ๐๐ฌ๐๐ซ๐ฌ", quote=True)
