import random


class Tactic:
    user_agent_list = [
        # firefox
        #"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        # 360
        #"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
        # safari - windows
        #"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        # IE9.0
        #"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
        # chrome
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    ]

    def rand_user_agent(self):
        return {'User-Agent': random.choice(self.user_agent_list)}
