from WaifuPicsPython import WaifuSync

SFW_CATEGORIES = [
    "random",
    "waifu",
    "neko",
    "shinobu",
    "megumin",
    "bully",
    "cuddle",
    "cry",
    "hug",
    "awoo",
    "kiss",
    "lick",
    "pat",
    "smug",
    "bonk",
    "yeet",
    "blush",
    "smile",
    "wave",
    "highfive",
    "handhold",
    "nom",
    "bite",
    "glomp",
    "slap",
    "kill",
    "kick",
    "happy",
    "wink",
    "poke",
    "dance",
    "cringe",
]
NSFW_CATEGORIES = ["random", "waifu", "neko", "trap", "blowjob"]


# "sfw" and "random" are set as defaults
def get_waifu_pic(for_work="sfw", category="random"):
    wafiu_pics = WaifuSync()
    waifu_url = (
        wafiu_pics.nsfw(category) if for_work == "nsfw" else wafiu_pics.sfw(category)
    )
    return waifu_url


def for_work_text(for_work):
    return "NSFW" if for_work == "nsfw" else "SFW"


def get_categories(for_work):
    return NSFW_CATEGORIES if for_work == "nsfw" else SFW_CATEGORIES
