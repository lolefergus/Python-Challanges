# six balls per over
import math

class OversCalculator:
    def total_overs(balls) -> float:
        overs = math.floor(balls/6)
        part = balls%6
        return float(str(overs)+"."+str(part))
