class Calculator:
    @classmethod
    def calculate(self, total: float, tip: int, num: int) -> float:
        """Method to calculate tip"""
        val = (total * (tip / 100)) / num
        return val + (total / num)