# if multiple of 3 output fizz
# if multiple of 5 output buzz
# if both FizzBuzz
# if neither output number
class FizzBuzz:
    def fizz_buzz(num) -> str:
        ret = str(num)
        if num%3 == 0:
            ret="Fizz"
            if num%5 == 0:
                ret+="Buzz"
        elif num%5 == 0:
            ret = "Buzz"
        return ret
