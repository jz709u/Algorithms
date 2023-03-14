//: [Previous](@previous)

import Foundation

/// https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
///
/// 
func miniMaxSum(arr: [Int]) -> Void {
    // Write your code here
    
    let sorted = arr.sorted()
    let min = sorted
        .prefix(4)
        .reduce(into: UInt(0)) { $0 += UInt($1) }

    let max = sorted
        .suffix(4)
        .reduce(into: UInt(0)) { $0 += UInt($1) }
    print("\(min) \(max)")
}



//: [Next](@next)
