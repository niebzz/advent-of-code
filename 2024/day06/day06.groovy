// INPUT
String filePath = '2024\\day06\\input.txt'

List input = new File(filePath).text.split('\n').collect { row -> row.toList() }


// FUNCTIONS
void grid(List<List> grid) { 
    grid.each { row -> print row.join('') }
}

List move(List position, int direction, List<List> grid) {
    int up = 0
    int right = 90
    int down = 180
    int left = 270
    List possibleDirections = [up, right, left, down]
    assert possibleDirections.contains(direction)
    assert position.size() == 2

    int r = position[0]
    int c = position[1]
    int newR = r
    int newC = c
    int newDir = direction

    if (newDir == up) { newR = r - 1 }
    else if (newDir == down) { newR = r + 1 }
    else if (newDir == left) { newC = c - 1 }
    else if (newDir == right) { newC = c + 1 }

    if (grid[newR][newC] == '#') {
        newDir = (direction + 90) % 360 // 90° right turn
        newR = r
        newC = c 
    }

    List newPos = [newR, newC]

    return [newPos, newDir]
}


// PART 1
Set<List> visitedPositions = []

input.eachWithIndex { row, r ->
    row.eachWithIndex { col, c ->
        if (col == '^') { visitedPositions << [r, c] }
    }
}

List newPos = visitedPositions[0]
int newDir = 0
List newData = [newPos, newDir]

while (true) {
    try {
        newData = move(newPos, newDir, input)
        newPos = newData[0]
        newDir = newData[1]
        // print newData
        // print '\n'
        if (newPos.any { index -> index < 0 }) { 
            break
    }
        visitedPositions << newPos
    } catch (NullPointerException) { 
        break 
} 
}

int part1 = visitedPositions.size()
print "Part 1: ${part1}"
