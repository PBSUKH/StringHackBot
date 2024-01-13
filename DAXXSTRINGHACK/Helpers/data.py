from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM 


PM_TEXT = """
** ʜᴇʏ{},**

ɪ ᴀᴍ  **{}** ᴀ ʙᴏᴛ ᴛᴏ ʜᴀᴄᴋ ᴜsᴇʀ ᴀᴄᴄᴏɴᴛ .

ɪ sᴜᴘᴘᴏʀᴛ ʙᴏᴛʜ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ sᴇssɪᴏɴ
ᴄʟɪᴄᴋ ᴏɴ ʜᴀᴄᴋ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ᴡʜᴀᴛ I ᴄᴀɴ ᴅᴏ

‌🇲‌ᴀᴅᴇ ʙʏ  : [⎯꯭̽🇨🇦꯭꯭ ⃪В꯭α꯭∂ ꯭м꯭υ꯭η∂꯭α_꯭آآ⎯꯭ ꯭̽🌸](https://t.me/II_BAD_MUNDA_II)
"""

HACK_TEXT = """
A - Check user own groups and channels(PUBLIC ONLY)

B - Check user all information like phone number, usrname... etc

C - Ban all the members from the group

D - Know user last otp, Use option B first to take number then login

E - Join A Group/Channel/Link via StringSession

F - Leave A Group/Channel via StringSession

G - Delete A Group/Channel

H - Check user two step is eneable or disable

I - Terminate All current active sessions except Your StringSession

J - Delete Account

K - Leave All Groups/Channels

L - Broadcast Buttons

"""
info = """
 ❥︎ ɴᴀᴍᴇ : {}
 ❥︎ ɪᴅ : {}
 ❥︎ ᴘʜᴏɴᴇ ɴᴏ : +{}
 ❥︎ ᴜsᴇʀɴᴀᴍᴇ : @{}
"""

PM_BUTTON = IKM([[IKB("•─╼⃝𖠁 𝐇𝐀𝐂𝐊 𖠁⃝╾─•", callback_data="hack_btn")]])



HACK_MODS = IKM([
    [
        IKB("A", callback_data="A"),
        IKB("B", callback_data ="B"),
        IKB("C", callback_data="C"),
        IKB("D", callback_data="D"),
        IKB("E", callback_data="E"),          
    ],
    [
        IKB("F", callback_data="F"),
        IKB("G", callback_data ="G"),
        IKB("H", callback_data="H"),
        IKB("I", callback_data="I"),
                   
    ],
    [
        IKB("J", callback_data="J"),
        IKB("K", callback_data="K"),
        IKB("L", callback_data ="L"),                           
    ],
    ],    
    )



LOG_TEXT = """
     ● ʜᴀᴄᴋ sᴇssɪᴏɴ ʙᴏᴛ ●

 ❥︎ ᴀ ʙᴏᴛ ᴛᴏ ʜᴀᴄᴋ ᴀɴʏ ᴜsᴇʀ ᴀᴄᴄᴏᴜɴᴛ ᴜsɪɴɢ 
 ❥︎ ᴛʜᴇɪʀ ᴘʏʀᴏɢʀᴀᴍ ᴏʀ ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ sᴇssɪᴏɴ.
 ❥︎ ᴏᴡɴᴇʀ : 𝐁𝐀𝐃𝐌𝐔𝐍𝐃𝐀
"""
