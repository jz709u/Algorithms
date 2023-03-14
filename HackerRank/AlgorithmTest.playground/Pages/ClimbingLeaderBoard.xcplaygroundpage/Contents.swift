/// https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem?isFullScreen=true


/*
 * Complete the 'climbingLeaderboard' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY ranked
 *  2. INTEGER_ARRAY player
 */
extension Array where Element == Int {
    func uniqueRanked() -> [Int:Int] {
        var rank = 1
        return reduce(into: [Int:Int](), { results, val in
            if results[val] != nil {

            } else {
                results[val] = rank
                rank += 1
            }
        })
    }
}

extension RandomAccessCollection where Element == Int {
    /// Finds such index N that predicate is true for all elements up to
    /// but not including the index N, and is false for all elements
    /// starting with index N.
    /// Behavior is undefined if there is no such N.
    func reverseBinarySearch(value: Int) -> Index {
        var low = endIndex
        var high = startIndex
        print("reverse binary search for \(value)")
        while low != high {
            let midDistance = distance(from: high, to: low) / 2
            let mid = index(high, offsetBy: midDistance)
            print("value: \(self[mid]) mid index: \(mid) mid distance \(midDistance)")
            if value == self[mid] {
                return mid
            } else if value < self[mid] {
                high = index(after: mid)
            } else {
                low = mid
            }
            print("low \(low) high \(high)")
            print("all indicies: \(self.indices)")
        }
        return low
    }
}

func climbingLeaderboard(ranked: [Int], player: [Int]) -> [Int] {
    let uniqueRanked = ranked.uniqueRanked()

    return player.reduce(into: [Int]()) { results, score in
        if let rank = uniqueRanked[score] {
            results += [rank]
        } else if let lastRank = ranked.last,
            let rank = uniqueRanked[lastRank],
            score < lastRank {
            results += [rank + 1]
        } else if let rank = uniqueRanked[ranked[ranked.reverseBinarySearch(value: score)]] {
            results += [rank]
        }

    }
}

//climbingLeaderboard(ranked: [100, 80, 70, 50, 40, 20, 10, 5], player: [5, 25, 50, 120])




//let sorted = [1000,100,10,5,2]
//print(sorted.reverseBinarySearch(value: 1100))

//let x = [2,3,4,12,0]
//
//var start = x.startIndex
//var end = x.endIndex
//while start != end {
//    print(x[start])
//    start = x.index(after: start)
//}
//x[x.index(before: end)]
import Foundation


/// Floating Points
var exponent: Float = -pow(2, -149)
let asDouble = Double(exponent)
//let asInt = Int(exponent)

//exponent +
//let sig = 100
//let x = Float(sign: 1, exponent: exponent, significand: sig)

