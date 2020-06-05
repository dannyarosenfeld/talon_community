import time
from talon.voice import Key, press, Str, Context
from ..utils import extract_num_from_m

ctx = Context("Sublime", bundle="com.sublimetext.2")

keymap = {
"select":"select ",
"star":" * ",
"from":"from ",
"customer": " customer c",
"join": " join ",
"utility account":" utility_acct ua",
"on":" on ",
"custom": " customer_notification_contact cnc",
"service point":" service_point",
"util":" util_",
"contact":"contact",
"preferences":"preferences",
"eyed":".id",
"bop":"_id"

}

ctx.keymap(keymap)


