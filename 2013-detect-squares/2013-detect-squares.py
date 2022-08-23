class DetectSquares:

    def __init__(self):
        self.ptsCounter = collections.defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.ptsCounter[tuple(point)] += 1
        self.pts.append(point)
        

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        
        for x,y in self.pts:
            if (abs(px-x)!= abs(py-y)) or px == x or py ==y:
                continue
            res += self.ptsCounter[(px, y)] * self.ptsCounter[(x,py)]
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)