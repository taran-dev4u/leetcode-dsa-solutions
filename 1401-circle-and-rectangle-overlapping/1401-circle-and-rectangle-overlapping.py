class Solution:

    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        closest_x = max(x1, min(xCenter, x2))
        closest_y = max(y1, min(yCenter, y2))
        dist_x = closest_x - xCenter
        dist_y = closest_y - yCenter
        return dist_x * dist_x + dist_y * dist_y <= radius * radius
