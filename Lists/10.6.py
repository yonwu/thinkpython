def is_anagram(s1, s2):
    if sorted(s1) == sorted(s2):
        return True
    return False


if __name__ == "__main__":
    print(is_anagram("abc", "bac"))
    print(is_anagram("abcd", "abce"))
