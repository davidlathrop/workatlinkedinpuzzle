import re
import string

class RegCommon:

    _permutations = None
    row_matches = []
    col_matches = []

    @staticmethod
    def permutations():
        if RegCommon._permutations is None:
            RegCommon._permutations = []
            for one in string.ascii_uppercase:
                for two in string.ascii_uppercase:
                    for three in string.ascii_uppercase:
                        for four in string.ascii_uppercase:
                            word = "{}{}{}{}".format(one, two, three, four)
                            RegCommon._permutations.append(word)

        return RegCommon._permutations

    @staticmethod
    def compile_regex(tests):
        _test = '^{0}$'

        return [re.compile(_test.format(test)) for test in tests]
