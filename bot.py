import env
import logging
from pyrogram import Client, idle
from pyromod import listen  # type: ignore
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid

logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

app = Client(
    "bot",
    api_id=env.API_ID,
    api_hash=env.API_HASH,
    bot_token=env.BOT_TOKEN,
    in_memory=True,
    plugins=dict(root="StringGenBot"),
)


if __name__ == "__main__":
    print("𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐓𝐡𝐞 𝐒𝐭𝐫𝐢𝐧𝐠 𝐆𝐞𝐧𝐞𝐫𝐚𝐭𝐨𝐫 𝐁𝐨𝐭...")
    try:
        app.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    uname = app.get_me().username
    print(f"@{uname} started successfully !")
    idle()
    app.stop()
    print("𝐁𝐨𝐭 𝐒𝐭𝐨𝐩𝐩𝐞𝐝. 𝐁𝐲𝐞!")
