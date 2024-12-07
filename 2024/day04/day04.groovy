// INPUT
String filePath = '2024\\day04\\input.txt'

List input = new File(filePath).readLines()

// PART 1
String borderAdd = '....'
input.eachWithIndex { row, i ->
    String newStr = borderAdd + row + borderAdd
    input[i] = newStr
}

int maxCol = input[0].size()
String newRow = '.' * maxCol
for (_ in (1..borderAdd.size())) {
    input.addAll(0, newRow)
    input.add(newRow)
}


String startNode = "X"
int part1 = 0
input.eachWithIndex { row, r ->
    row.eachWithIndex { col, c ->
        if (col == startNode) {
            for (dr in (-1..1)) {
                for (dc in (-1..1)) {
                    String adj1 = input[r + dr][c + dc]
                    String adj2 = input[r + (2 * dr)][c + (2 * dc)]
                    String adj3 = input[r + (3 * dr)][c + (3 * dc)]
                    if (adj1 == 'M' && adj2 == 'A' && adj3 == 'S') {
                        part1 += 1
                    }
                }
            }
        }
    }
}

print 'Part1: ' + part1
print '\n'

// PART 2
startNode = 'A'

int part2 = 0
input.eachWithIndex { row, r ->
    row.eachWithIndex { col, c ->
        if (col == startNode) {
            String corner1 = input[r - 1][c - 1]
            String corner2 = input[r - 1][c + 1]
            String corner3 = input[r + 1][c - 1]
            String corner4 = input[r + 1][c + 1]
            List corners = [corner1, corner2, corner3, corner4]

            int countM = corners.count('M') 
            int countS = corners.count('S')
            if (countM == 2 && countS == 2) {
                part2 += 1
            }
        }
    }
}

print 'Part2: ' + part2
