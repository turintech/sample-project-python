class StrOps:
    @staticmethod
    def str_reverse(s: str) -> str:

        return s[::-1]

    @staticmethod
    def palindrome(s: str) -> bool:

        for i in range(len(s) // 2):  # Only iterate through half the string
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True