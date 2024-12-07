// INPUT
String filePath = '2024\\day05\\input.txt'

def (List orderingRules, List updates) = input = new File(filePath)
    .text
    .split(/(?m)^\s*$/)
    .collect { it.trim().split(/\r?\n/) }

orderingRules = orderingRules*.split(/\|/)
updates = updates*.split(',')

orderingRules = orderingRules.collect { rule -> rule*.toInteger() }
updates = updates.collect { update -> update.toList()*.toInteger() }


// FUNCTIONS
boolean isValidUpdate(List update, List orderingRules) {
    List tests = []
    for (rule in orderingRules) {
        int before = rule[0]
        int after = rule[1]
        if (update.contains(before) && update.contains(after)) {
            boolean obeysRule = update.indexOf(before) < update.indexOf(after)
            tests << obeysRule
        }
    }
    return tests.every { result -> result == true } as boolean
}


// PART 1
List validUpdates = []
for (update in updates) {
    if (isValidUpdate(update, orderingRules)) {
        validUpdates << update
    }
}

int part1 = 0
for (update in validUpdates) {
    int middleIndex = (update.size() - 1) / 2
    part1 += update*.toInteger()[middleIndex]
}

print 'Part 1: ' + part1 + '\n'

// PART 2
// List invalidUpdates = []
// for (update in updates) {
//     if (!isValidUpdate(update, orderingRules)) {
//         while (!isValidUpdate(update, orderingRules)) {
//             Collections.shuffle(update, new Random())
//         }
//         invalidUpdates << update
//     }

// }

// int part2 = 0
// for (update in invalidUpdates) {
//     middleIndex = (update.size() - 1) / 2
//     part2 += update*.toInteger()[middleIndex]
// }

// print 'Part 2: ' + part2 + '\n'
