"""
    A strategy is an opponent.
    A strategy only has access to:
        * Secret number
        * History of past transactions in previous rounds
"""

from main import History
from main import Player
import constants
from enum import Enum

class Response(str, Enum):
    """ Strategies return a Response to the market maker.
    When a strategy lifts a market makers offer, they are buying.
    When a strategy hits a market makers bid, they are selling.
    A strategy can also choose to not trade.
    """
    HIT = "sells"
    LIFT = "buys "
    NO_TRADE = "--"


class StrategyTemplate(Player):
    """ All opponent strategies inherit this """
    def __init__(self, name):
        super().__init__(name)

    def get_action(self):
        raise NotImplementedError

    def get_secret(self):
        return self.secret

    def get_past_transactions(self):
        return self.past_transactions

class BaselineStrat(StrategyTemplate):
    """ Opponent sees fair value as expected value * num players """
    def get_prev_round(transactions, prev_round):
        matching_rounds = []
        for sublist in transactions:
            if sublist[0] == prev_round:
                matching_rounds.append(sublist)
        return matching_rounds

    def get_action(
        self,
        bid,
        ask,
        history : History,
        round_num
    ) -> Response:
        prev_round = round_num - 1
        if (prev_round == 0):
            fair_value = self.secret + ((constants.MAX_SECRET - constants.MIN_SECRET)/2)* (constants.NUM_OPPONENTS)
        else:
            last_round_transacs = #TODO
        # Opponent will buy if ask is < fair_value
        # and sell if bid is > fair_value. Otherwise, no trade.
        if(ask < fair_value):
            return Response.LIFT
        elif(bid > fair_value):
            return Response.HIT
        else:
            return Response.NO_TRADE
