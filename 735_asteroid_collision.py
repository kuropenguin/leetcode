from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        plus_asteroids = []
        minus_asteroids = []
        for idx in range(len(asteroids)):
            asteroid = asteroids[idx]
            if asteroid > 0:
                plus_asteroids.append({idx: asteroid})
            else:
                minus_asteroids.append({idx: asteroid})
        while len(plus_asteroids) > 0 and len(minus_asteroids) > 0:
            plus_asteroid_dict = plus_asteroids.pop()
            minus_asteroid_dict = minus_asteroids.pop()

            plus_asteroid_idx = list(plus_asteroid_dict.keys())[0]
            minus_asteroid_idx = list(minus_asteroid_dict.keys())[0]
            plus_asteroid = list(plus_asteroid_dict.values())[0]
            minus_asteroid = list(minus_asteroid_dict.values())[0]
        return plus_asteroids + minus_asteroids


solution = Solution()

asteroids = [5, 10, -5]
result = solution.asteroidCollision(asteroids=asteroids)
print(result)
print(result == [5, 10])

asteroids = [8, -8]
result = solution.asteroidCollision(asteroids=asteroids)
print(result)
print(result == [])

asteroids = [10, 2, -5]
result = solution.asteroidCollision(asteroids=asteroids)
print(result)
print(result == [10])


asteroids = [-2, -1, 1, 2]
result = solution.asteroidCollision(asteroids=asteroids)
print(result)
print(result == [-2, -1, 1, 2])
