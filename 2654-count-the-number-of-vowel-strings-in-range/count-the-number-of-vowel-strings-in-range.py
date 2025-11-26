class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        count=0
        vowel = ['a','e','i','o','u']


        for i,word in enumerate(words):
            if word[0].lower() in vowel and word[-1].lower() in vowel and i >= left and i<=right:
                count+=1
            elif len(word) == 1 and word in vowel and i >= left and i<=right:
                count+=1

        return count
