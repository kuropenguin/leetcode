class RecentCounter:

    def __init__(self):
        self.list = []

    def ping(self, t: int) -> int:
        self.list.append(t)
        min_range = t - 3000
        while len(self.list) > 0:
            if self.list[0] < min_range:
                self.list.pop(0)
            else:
                break
        return len(self.list)


recentCounter = RecentCounter()

result = recentCounter.ping(t=1)
print(result)
result = recentCounter.ping(t=100)
print(result)
result = recentCounter.ping(t=3001)
print(result)
result = recentCounter.ping(t=3002)
print(result)
