class Codec:
    def __init__(self):
        
        self.store = {}
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        """
        v = hash(longUrl)
        self.store['http://tinyurl.com/' + str(v)] = longUrl
        return 'http://tinyurl.com/' + str(v)
    
    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        """
       
        return self.store[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))