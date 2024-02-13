class Colors:
    red = (255, 0, 0)
    yellow = (255, 255, 0)
    green = (34, 139, 34)
    salmon = (255, 160, 122)
    gold = (255, 215, 0)
    indigo = (75, 0, 130)
    thistle = (216, 191, 216)
    turq = (64, 224, 208)
    pink = (255, 192, 203)
    background = (128, 128, 128)

    @classmethod
    def get_color(cls):
        return [cls.turq, cls.yellow, cls.green, cls.salmon, cls.gold, cls.indigo, cls.thistle, cls.red, cls.pink]