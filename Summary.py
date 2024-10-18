class Result:
    def __init__(self, data, bot, top, bot_L, top_L, F, R, L, M, bot_CF, top_CF, RF, mode):
        self.top = top
        self.limit = L
        self.ranges = R
        self.bottom = bot
        self.midpoint = M
        self.frequency = F
        self.classval = data
        self.top_limit = top_L
        self.bottom_limit = bot_L
        self.mode = mode
        self.bottom_cumulative_frequency = bot_CF
        self.top_cumulative_frequency = top_CF
        self.relative_frequency = RF
        self.percentage_relative_frequency = [f"{rf:.2f}%" for rf in self.relative_frequency]
