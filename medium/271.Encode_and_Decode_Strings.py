# 271. Encode and Decode Strings
# https://leetcode.com/problems/encode-and-decode-strings/
# https://leetcode.com/problems/encode-and-decode-strings/discuss/70448/1%2B7-lines-Python-(length-prefixes)

class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        result = ''
        for s in strs:
            result+= str(len(s))+':'+s
        return result
        # return ''.join('%d:' % len(s) + s for s in strs)


    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        strs = []
        i = 0
        while i < len(s):
            j = s.find(':', i)
            _len = int(s[i:j])
            i = j+1+_len
            strs.append(s[j+1:i])
        return strs

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
