/*
* The function is expected to return an INTEGER.
* The function accepts INTEGER_ARRAY candles as parameter.
 https://www.hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=true
*/

func birthdayCakeCandles(candles: [Int]) -> Int {
    
    var max = 0
    var count = 0
    for i in candles {
        if i > max {
            max = i
            count = 1
        } else if i == max {
            count += 1
        }
    }
    return count
}
