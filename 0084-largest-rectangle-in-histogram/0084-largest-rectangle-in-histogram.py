class Solution: 
  def largestRectangleArea(self, heights: List[int]) -> int:
    heights= [0] + heights + [0]
    monostack = []
    ret = 0
    for i in range(len(heights)):
      if not monostack or heights[i] >= heights[i-1]:
        monostack.append(i)
      else:
        while monostack and heights[monostack[-1]] > heights[i]:
          index = monostack.pop()
          ret = max(ret, heights[index]*(i - monostack[-1] - 1))
        monostack.append(i)
    return ret


      



