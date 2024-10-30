class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        asteroids_stack = []
        for asteroid in asteroids:
            while asteroids_stack and asteroid < 0 and asteroids_stack[-1] > 0:
                greater = asteroid + asteroids_stack[-1]
                if greater == 0:
                    asteroids_stack.pop()
                    asteroid = 0
                elif greater < 0:
                    asteroids_stack.pop()
                else:
                    asteroid = 0
                    
            if asteroid:
                asteroids_stack.append(asteroid)

        return asteroids_stack