class DigitCounter:

    def digits_count(num) -> int:
        if num != 0:
            num //= 10
            dig = DigitCounter.digits_count(num)
            # if only one digit return 1 to catch edgecase where 0 not triggered
            if dig == 1 and num == 0:
                return 1
            else:
                return dig + 1
        else: # return 1 not 0 for edge case where num is 0
            return 1


