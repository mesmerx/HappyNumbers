class HappyOrNot:
    """ this class share atribbute for the happy validator """
    def __init__(self, cache_file: str = '', cache: bool = True) -> None:
        pass

    def happy_or_not(self, number: int) -> bool:
        """ the function to test for happy numbers
        PARAM : TYPE
        ------ -----
        number:  int
            the number to be tested

        RETURN: TYPE
        ------ -----
            bool
                a boolean to indicate true if happya nd false if not
        """
        if number == 0:
            return False

        # doing string conversion help with not doing division and then mod operator,
        # for large numbrs helps in time complexity
        sum_square_number = 0
        while sum_square_number != 1:
            sum_square_number = sum([int(n)**2 for n in str(number)])
            if sum_square_number == 1:
                return True
