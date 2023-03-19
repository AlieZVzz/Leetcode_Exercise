from itertools import takewhile
def VerifySquenceOfBST(self, seq):
    if not seq:
        return False
    p = seq[-1]
    left_sub = list(takewhile(lambda x: x < p, seq[:-1]))
    right_sub = seq[len(left_sub):-1]
    if not all(x>p for x in right_sub):
        return False
    left = right = True
    if left_sub:
        left = self.VerifySquenceOfBST(left_sub)
    if right_sub:
        right = self.VerifySquenceOfBST(right_sub)
    return left and right