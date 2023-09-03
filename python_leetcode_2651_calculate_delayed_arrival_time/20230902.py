arrivalTime = 15 ; delayedTime = 5      # Output: 20 
arrivalTime = 13 ; delayedTime = 11     # Output: 0


class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime+delayedTime)%24