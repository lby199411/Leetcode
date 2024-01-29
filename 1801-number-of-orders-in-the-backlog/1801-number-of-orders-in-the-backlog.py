class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        # two heap
        buy, sell = [], []
        for order in orders:
            price, amount, tp = order
            if tp == 0:  # buy
                if not sell or sell[0][0] > price:
                    heapq.heappush(buy, (-price, amount))
                else:
                    while sell and amount and sell[0][0] <= price:
                        s_price, s_amount = heapq.heappop(sell)
                        if s_amount == amount:
                            amount = 0
                        elif s_amount > amount:
                            heapq.heappush(sell, (s_price, s_amount - amount))
                            amount = 0
                        else:
                            amount = amount - s_amount
                    if amount:
                        heapq.heappush(buy, (-price, amount))

            else:        # sell
                if not buy or -buy[0][0] < price:
                    heapq.heappush(sell, (price, amount))
                else:
                    while buy and amount and -buy[0][0] >= price:
                        b_price, b_amount = heapq.heappop(buy)
                        if b_amount == amount:
                            amount = 0
                        elif b_amount >amount:
                            heapq.heappush(buy, (b_price, b_amount - amount))
                            amount = 0
                        else:
                            amount = amount - b_amount
                    if amount:
                        heapq.heappush(sell, (price, amount))
        ret = 0
        for pair in buy:
            ret += pair[1]
        for pair in sell:
            ret += pair[1]
        return ret % (10**9 + 7)



