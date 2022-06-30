from WaifuPicsPython import WaifuSync

def your_function():
    wafiu_pics = WaifuSync()
    megumin_image_url = wafiu_pics.sfw('megumin')
    # returns 1 url as a string
    waifu_images = wafiu_pics.sfw('waifu', many=True)
    # returns 30 urls in a list
    random_sfw_image = wafiu_pics.sfw('random')
    # returns 1 random sfw image
    lewd_waifu = wafiu_pics.nsfw('waifu')
    # returns 1 nsfw waifu url as a string
    lewd_nekos = wafiu_pics.nsfw('neko', many=True)
    # returns 30 nsfw neko urls in a list
    random_nsfw_images = wafiu_pics.nsfw('random', many=True)
    # returns 30 random nsfw images

    return random_nsfw_images

print(your_function())