class Solution:
    def construct(self, grid):
        def helper(x, y, sz):
            if sz == 1:
                return Node(grid[x][y], True, None, None, None, None)

            h = sz // 2
            tl = helper(x, y, h)
            tr = helper(x, y + h, h)
            bl = helper(x + h, y, h)
            br = helper(x + h, y + h, h)

            children = [tl, tr, bl, br]

            leaves = all(c.isLeaf for c in children)
            allMatch = all(c.val == tl.val for c in children)

            isLeaf = leaves and allMatch

            if isLeaf:
                return Node(tl.val, True, None, None, None, None)
            else:
                return Node(1, False, tl, tr, bl, br)

        return helper(0, 0, len(grid))
