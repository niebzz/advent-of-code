import java.util.regex.Pattern
import java.util.regex.Matcher

// INPUT
String filePath = '2024\\day03\\input.txt'

String input = new File(filePath).text

// REGEX
Pattern mulPattern = Pattern.compile(/mul\(\d{1,3},\d{1,3}\)/)
Pattern doPattern = Pattern.compile(/do\(\)/)
Pattern dontPattern = Pattern.compile(/don't\(\)/)

Matcher mulMatcher = input =~ mulPattern
Matcher doMatcher = input =~ doPattern
Matcher dontMatcher = input =~ dontPattern

List mulIndeces = []
List doIndeces = [0] // default condition is enabled
List dontIndeces = []

while (mulMatcher.find()) { mulIndeces << mulMatcher.start() }
while (doMatcher.find()) { doIndeces << doMatcher.start() }
while (dontMatcher.find()) { dontIndeces << dontMatcher.start() }


// PART 1
List instructions = mulMatcher.findAll()

int totalSum = 0
for (instruction in instructions) {
    List digits = instruction.findAll(/\d+/)*.toInteger()
    assert digits.size() == 2
    totalSum += digits[0] * digits[1]
}
print totalSum


// PART 2
List enableDisableList = []

i = 0
boolean instructionsEnabled = true
while (i <= input.size()) {
    if (doIndeces.contains(i)) { instructionsEnabled = true }
    if (dontIndeces.contains(i)) {instructionsEnabled = false }

    if (instructionsEnabled) { enableDisableList += 'ENABLE'}
    else { enableDisableList += 'DISABLE' }

    i += 1
}

int totalSumPartII = 0
instructions.eachWithIndex { instruction, i -> 
    String enableOrDisable = enableDisableList[mulIndeces[i]]
    if (enableOrDisable == "ENABLE") {
        List digits = instruction.findAll(/\d+/)*.toInteger()
        assert digits.size() == 2
        totalSumPartII += digits[0] * digits[1]
    }
}

print '\n'
print totalSumPartII
