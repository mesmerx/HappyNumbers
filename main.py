class NoCache(Exception):
    pass


class HappyOrNot:
    """ this class share atribbute for the happy validator """
    def __init__(self, cache_file: str = '', cache: bool = True) -> None:
        self.cache = None
        if not cache and cache_file:
            raise NoCache("cache file need cache option active")
        if cache:
            self.cache = {0: False}
        self.cache_file = None
        if cache_file:
            self.cache_file = cache_file
            with open(cache_file, 'a+') as f:
                f.seek(0)
                for line in f.readlines():
                    number, boolean, _ = line.split(' ')
                    self.cache[int(number)] = eval(boolean)

    def happy_or_not(self, number: int) -> bool:
        """ the function to test for happy numbers
        PARAM : TYPE
        ------ -----
        number:  int
            the number to be tested

        RETURN: TYPE
        ------ -----
            bool
                a boolean to indicate true if happy and false if not
        """
        if number == 0:
            return False
        if self.cache:
            if number in self.cache:
                return self.cache[number]
            stacked = set()
            stacked.add(number)
        square_number = number
        phase_square_number = self.sum_square_number(number)
        while square_number != phase_square_number:
            square_number = self.sum_square_number(square_number)
            phase_square_number = self.sum_square_number(phase_square_number)
            phase_square_number = self.sum_square_number(phase_square_number)
            if self.cache:
                stacked.add(square_number)
        if self.cache:
            for stack in stacked:
                self.cache[stack] = square_number == 1
            self.update_cache_file()
        return square_number == 1

    def update_cache_file(self):
        if self.cache_file:
            with open(self.cache_file, 'w') as f:
                for stack, value in sorted(self.cache.items()):
                    print(f'{stack} {value} \n')
                    f.write(f'{stack} {value} \n')

    @staticmethod
    def sum_square_number(number: int) -> int:
        """ the function to square and sum the actual number
        PARAM : TYPE
        -----   ----
        number: int
            the number to be squared

        RETURN : TYPE
        ------ -----
            int
                the squared number
        """
        # doing string conversion help with not doing division and then mod operator,
        # for large numbrs helps in time complexity
        return sum([int(n)**2 for n in str(number)])
