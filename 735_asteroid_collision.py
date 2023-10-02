from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        for new_asteroid in asteroids:
            if new_asteroid > 0:
                result.append(new_asteroid)
            else:
                minus_asteroid = new_asteroid
                while True:
                    if len(result) == 0:
                        result.append(minus_asteroid)
                        break
                    old_asteroid = result.pop()
                    if old_asteroid < 0:
                        result.append(old_asteroid)
                        result.append(minus_asteroid)
                        break
                    plus_asteroid = old_asteroid
                    if abs(minus_asteroid) == abs(plus_asteroid):
                        break
                    if abs(plus_asteroid) > abs(minus_asteroid):
                        result.append(plus_asteroid)
                        break
        return result


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
