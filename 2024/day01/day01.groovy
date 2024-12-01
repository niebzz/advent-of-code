String filepath = '2024\\day01\\input.txt'

List input = new File(filepath).text.split()*.toInteger()

List list1 = []
List list2 = []

input.eachWithIndex { num, i ->
    if (i % 2 == 0) { list1 += num } // odd numbers
    if (i % 2 != 0) { list2 += num } // even numbers
}

// PART 1
int totalDistance = 0
[list1.sort(), list2.sort()].transpose().each { loc1, loc2 ->
    totalDistance += Math.abs(loc1 - loc2)
}

print totalDistance

// PART 2
int similarityScore = 0
for (id in list1) {
    numOccurences = list2.count(id)
    similarityScore += (id * numOccurences)
}

print similarityScore
