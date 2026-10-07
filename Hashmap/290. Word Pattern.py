class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        
        c_to_word = {}
        word_to_c = {}

        for c, word in zip(pattern, words):
            if c in c_to_word and c_to_word[c] != word:
                return False
            if word in word_to_c and word_to_c[word] != c:
                return False
            
            c_to_word[c] = word
            word_to_c[word] = c

        return True 