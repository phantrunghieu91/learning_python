class Solution:
  def myRoot(self, x: int) -> int:
    if x < 2:
      return x
    s, e = 0, x
    while s <= e:
      m = ( s + e ) // 2
      if m * m == x:
        return m
      if m * m < x:
        s = m + 1
      else:
        e = m - 1
    return e
  
# test cases
sol = Solution()
# print(sol.myRoot(4)) # 2
print(sol.myRoot(8)) # 2