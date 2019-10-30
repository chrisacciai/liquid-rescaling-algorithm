class SeamCarving:
    seamCoordinates = []
    def __init__(self):
        return
    
    # @return the seam's weight
    def run(self, image):

        num_rows = len(image)
        num_cols = len(image[0])
        energies = []

        def findEnergy(image, row, col):
            sum_diff = 0
            num_neighbors = -1
            for i in range(-1,2):
                for j in range(-1,2):
                    if in_bounds(image, row + i, col + j):
                        sum_diff += findPixelDifference(image[row][col], image[row + i][col + j])
                        num_neighbors += 1
            return sum_diff/num_neighbors

        def findPixelDifference(p1, p2):
            return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)**.5

        def in_bounds(image, row, col):
            if row < 0 or col < 0:
                return False
            if row > len(image)-1 or col > len(image[0])-1:
                return False
            return True

        for i in range(0, num_rows):
            row = []
            for j in range(0, num_cols):
                row.append(findEnergy(image, i, j))
            energies.append(row)

        mem = list(energies)

        for r in range(1, num_rows):
            for c in range(0, num_cols):
                if c == 0:
                    index = mem[r - 1][c:c + 2].index(min(mem[r - 1][c:c + 2]))
                    min_e = mem[r - 1][index + c]
                elif c == num_cols - 1:
                    index = mem[r - 1][c - 1:c + 1].index(min(mem[r - 1][c - 1:c + 1]))
                    min_e = mem[r - 1][index + c - 1]                
                else:
                    index = mem[r - 1][c - 1:c + 2].index(min(mem[r - 1][c - 1:c + 2]))
                    min_e = mem[r - 1][index + c - 1]

                mem[r][c] += min_e
    
        index = mem[0].index(min(mem[0]))
        self.seamCoordinates.append(index)
        for r in range(1, num_rows):
            if index == 0:
                index = mem[r].index(min(mem[r][index:index + 2]))
            elif index == num_cols - 1:
                index = mem[r].index(min(mem[r][index - 1:index + 1]))
            else:
                index = mem[r].index(min(mem[r][index - 1:index + 2]))
            
            self.seamCoordinates.append(index)
        
                
        return min(mem[num_rows - 1])

    # @return the ordered list of x-coordinates (column number) of each pixel in the seam
    # as an array
    def getSeam(self):
        return self.seamCoordinates

