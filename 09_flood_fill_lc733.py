from typing import List

# https://leetcode.com/problems/flood-fill/


class Solution:
    # using recursion to solve the problem on hands
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def fill(oc, nr, nc):
            # check if current row/col is not out of bounds, also check if current pixel is same as original color
            if nr >= len(image) or nc >= len(image[0]) or nr < 0 or nc < 0 or image[nr][nc] != oc:
                return
            # if so, set it to new color
            image[nr][nc] = color

            # recursively do the same for all 4 adjacent pixels
            fill(oc, nr+1, nc)
            fill(oc, nr-1, nc)
            fill(oc, nr, nc+1)
            fill(oc, nr, nc-1)

        # if the pixel is already in new color, simply return image
        if image[sr][sc] == color:
            return image

        # if not, invoke the recursive function
        fill(image[sr][sc], sr, sc)

        # return modified image
        return image

        # time complexity: O(mn), m = rows, n = cols
