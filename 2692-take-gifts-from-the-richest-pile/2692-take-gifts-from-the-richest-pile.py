class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gheap = [-gift for gift in gifts]

        for i in range(0, k):
            heapq.heapify(gheap)
            # print("hpfy: ",gheap)
            pile = -heapq.heappop(gheap)
            # print("bsq: ",pile)
            pile = floor(sqrt(pile))
            # print("as:", pile)
            gheap.append(-pile)

        # gheap = [-gift for gift in gheap]

        return -sum(gheap)
        