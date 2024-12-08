// IMPORTS
import java.util.regex.Pattern
import java.util.regex.Matcher

// INPUT
String filePath = '2024\\day07\\input.txt'

List input = new File(filePath).text.split('\n').collect { it.split(':') }

Map calibrationMap = [:]
input.each { row ->
    Pattern digits = Pattern.compile(/(\d+)/)
    Matcher matches = row[1] =~ digits
    BigInteger key = row[0].toBigInteger()
    List values = matches.findAll().flatten()*.toBigInteger().withIndex()
        .findAll { _, index -> index % 2 == 0 }
        .collect { num -> num[0] }

    calibrationMap[key] = values
}

// PART 1
Set validCalibrations = []
List<String> possibleOps = ['add', 'multiply']

calibrationMap.each { key, values ->
    BigInteger numOperations = values.size() - 1
    List<String> possibleConfigs = (1..numOperations).collect { possibleOps }.combinations()

    for (operators in possibleConfigs) {
        BigInteger result = values[0]
        operators.eachWithIndex { operator, index ->
            if (operator == 'add') {
                result += values[index + 1]
            }
            else if (operator == 'multiply') {
                result *= values[index + 1]
            }
        }

        if (result == key) {
            validCalibrations << result
        // print values
        // print result
        // print '\n'
        }
    }
}

BigInteger part1 = validCalibrations.sum()
print part1
