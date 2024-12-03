String filePath = '2024\\day02\\input.txt'

List input = new File(filePath).text.readLines()*.split()

input.eachWithIndex { row, i -> input[i] = row*.toInteger() }

// PART 1
List getAdjacent1D(List list, int index) {
    if (index < 0 || index >= list.size()) {
        return [null, null, null]
    }

    Object l = index > 0 ? list[index - 1] : null
    Object c = list[index]
    Object r = index < list.size() - 1 ? list[index + 1] : null

    return [l, c, r]
}

boolean isSafeNumber(List adjValues) {
    assert adjValues.size() == 3

    def l = adjValues[0]
    def c = adjValues[1]
    def r = adjValues[2]

    if (!l){ 
        int diff = Math.abs(r-c)
        if (diff < 1 || diff > 3) { return false }
    }
    else if (!r){ 
        int diff = Math.abs(c-l)
        if (diff < 1 || diff > 3) { return false }
    }
    else {
        boolean isPos = c-l > 0 || r-c > 0
        boolean isNeg = c-l < 0 || r-c < 0
        if (isPos && isNeg) { return false }

        int diff1 = Math.abs(c-l)
        int diff2 = Math.abs(r-c)
        if (diff1 < 1 || diff1 > 3 || diff2 < 1 || diff2 > 3) { return false }
    }
    return true
}

boolean isSafeRow(List row) {
    List safetyValues = []
    row.eachWithIndex { num, i ->
        List adjNums = getAdjacent1D(row, i)
        safetyValues += isSafeNumber(adjNums)
    }
    return !safetyValues.any { bool -> bool == false }
}


int countSafeReports = 0
for (row in input) {
    if (isSafeRow(row)) { countSafeReports += 1}
}


// PART 2
List generatePossibleRows(List row) {
    return (0..<row.size()).collect { indexToRemove ->
        row[0..<indexToRemove] + row[(indexToRemove + 1)..<row.size()] }
}

boolean isSafeRowPartII(List row){
    if (isSafeRow(row)) {
        return true
    }
    List possibleRows = generatePossibleRows(row)

    for (possibleRow in possibleRows) {
        if (isSafeRow(possibleRow)) {
            return true
        }
    }
    return false
}

int countSafeReportsPartII = 0
for (row in input) {
    if (isSafeRowPartII(row)) { countSafeReportsPartII += 1}
}

print countSafeReports // Part 1
print("\n")
print countSafeReportsPartII // Part 2
