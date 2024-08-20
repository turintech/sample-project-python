class StrOps:
    @staticmethod
    def str_reverse(s: str) -> str:
        """Reverse a string

        Args:
            s (str): String to reverse

        Returns:
            str: Reversed string
        """
        ret = ""
        for i in range(len(s)):
            ret += s[len(s) - 1 - i]
        return ret

    @staticmethod
    def palindrome(s: str) -> bool:
        """Check if a string is a palindrome

        Args:
            s (str): String to check

        Returns:
            bool: True if the string is a palindrome, False otherwise
        """
        for i in range(len(s)):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True
