class Solution(object):
    def strongPasswordChecker(self, password):
        """
        :type password: str
        :rtype: int
        """

        def length_checker(min, max, password):
            """
            Objective return true if the string is min to max charcters.
            :type password: str
            :type min: int
            :type max: int
            :rtype: int
            """
            if min is None:
                min = 6
            if max is None:
                max = 20
            if max >= len(password) >= min:
                return 0
            elif max < len(password):
                return max - len(password)
            elif min > len(password):
                return min - len(password)
            return 0

        def one_checker(password):
            """
            Objective: return one for each charcter which can be changed to meet the three conditions.
            :param password:
            :return:
            """

            def upper_checker(_):
                return _.isupper()

            def lower_checker(_):
                return _.islower()

            def int_checker(_):
                try:
                    return type(int(_)) == int
                except ValueError:
                    return False

            upper = False
            lower = False
            int_ = False

            for _ in password:
                if not upper:
                    upper = upper_checker(_)
                if not lower:
                    lower = lower_checker(_)
                if not int_:
                    int_ = int_checker(_)

            if upper and lower and int_:
                return 0

            count = 0

            if not upper:
                count = count + 1
            elif not lower:
                count = count + 1
            elif not int_:
                count = count + 1
            return count

        def repeat_checker(repeat, password):
            """
            Objective return true if str has less than repeat repeats
            :type password: object
            :param repeat: int
            :param password: str
            :return:
            """
            if repeat is None:
                repeat = 3

            result = 0
            done = []

            def conseq_checker(i, password, conq):
                if len(password) > 0:
                    if i == password[0]:
                        return conseq_checker(i, password[1:], conq=conq + 1)
                return conq

            for i in password:
                if i not in done:
                    var = conseq_checker(i, password[password.index(i):], 0)
                    if var == repeat:
                        result = result + 1
                        done.append(i)
                    elif var > repeat:
                        result = result + 1
                        password = password[repeat:]
            return result

        result = 0

        if length_checker(None, None, password) > 0:
            return length_checker(None, None, password)
        elif length_checker(None, None, password) < 0:
            result = abs(length_checker(None, None, password))

        if repeat_checker(None, password) >= one_checker(password):
            return repeat_checker(None, password)
        elif one_checker(password) >= repeat_checker(None, password):
            return one_checker(password) + result
        else:
            return result

        # TEST
        # print("Pass is too short excpecting 2 and got", length_checker(None, None, "pass"))
        # print("Passsssssssssssssssssss is too long excpecting 3 and got",
        #       length_checker(None, None, "Passsssssssssssssssssss"))
        # print("Password has a good length excpecting 0 and got", length_checker(None, None, "Password"))
        # print("Password has one capital but it does not have a number expecting 1 and got", one_checker("Password"))
        # print("PASSWORD1 has all caps and a number but no lowercase so expecting 1 and got", one_checker("PASSWORD1"))
        # print("password1 has all lower and a number but no lowercase so expecting 1 and got", one_checker("password1"))
        # print("Password1 has caps, lowers, and a number expecting 0 and got", one_checker("Password1"))
        # print("Paasword should have 0 ", repeat_checker(None, "Paasword"))
        # print("Paaasword should have 1 ", repeat_checker(None, "Paaasword"))
        # print("Paaasw000rd should have 2 ", repeat_checker(None, "Paaasw000rd"))
        # print("Paaasw000rfffdd should have 3 ", repeat_checker(None, "Paaasw000rfffdd"))


# LEETCODE TEST
checker = Solution()

# print("Expecting a value of 5 for password = a.", checker.strongPasswordChecker('a'),
#       5 == checker.strongPasswordChecker('a'))
# print("Expecting a value of 3 for password = aA1.", checker.strongPasswordChecker('aA1'),
#       3 == checker.strongPasswordChecker('aA1'))
# print("Expecting a value of 0 for password = 1337C0d3.", checker.strongPasswordChecker('1337C0d3'),
#       0 == checker.strongPasswordChecker('1337C0d3'))
# print('Expecting a value of 3 for password = Paaasw000rfffdd.', checker.strongPasswordChecker('Paaasw000rfffdd'),
#       3 == checker.strongPasswordChecker('Paaasw000rfffdd'))
# print('Expecting a value of 1 for password = "aaa123".', checker.strongPasswordChecker("aaa123"),
#       1 == checker.strongPasswordChecker("aaa123"))
# print('Expecting a value of 2 for password = "aaa111".', checker.strongPasswordChecker("aaa111"),
#       2 == checker.strongPasswordChecker("aaa111"))
# print('Expecting a value of 3 for password = "1111111111".', checker.strongPasswordChecker("1111111111"),
#       3 == checker.strongPasswordChecker("1111111111"))
# print('Expecting a value of 2 for password = "ABABABABABABABABABAB1".',
#       checker.strongPasswordChecker("ABABABABABABABABABAB1"),
#       2 == checker.strongPasswordChecker("ABABABABABABABABABAB1"))
print('Expecting a value of 8 for password = "bbaaaaaaaaaaaaaaacccccc".',
      checker.strongPasswordChecker("bbaaaaaaaaaaaaaaacccccc"),
      8 == checker.strongPasswordChecker("bbaaaaaaaaaaaaaaacccccc"))
