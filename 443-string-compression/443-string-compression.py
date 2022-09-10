class Solution:
    def compress(self, chars: List[str]) -> int:
        r_index = 0
        
        while r_index < len(chars):
        
            count = 1 

            while r_index + 1 < len(chars) and chars[r_index] == chars[r_index+1]:
                count += 1
                del chars[r_index + 1 ]

            if count > 1:
                for char in str(count):
                    chars.insert(r_index + 1, char)
                    r_index += 1
            r_index += 1
        
        return len(chars)