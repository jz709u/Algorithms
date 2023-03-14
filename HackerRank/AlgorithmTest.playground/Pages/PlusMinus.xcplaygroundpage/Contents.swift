//: [Previous](@previous)
import Foundation
/// https://www.hackerrank.com/challenges/plus-minus/problem?isFullScreen=true
func plusMinus(arr: [Int]) -> Void {
    // Write your code here
    
    var pos = 0
    var neg = 0
    var zero = 0
    let count = Float(arr.count)
    for x in arr {
        if x > 0 {
            pos += 1
        } else if x == 0 {
            zero += 1
        } else {
            neg += 1
        }
    }
    print(String(format: "%.6f", Float(pos) / count))
    print(String(format: "%.6f", Float(neg) / count))
    print(String(format: "%.6f", Float(zero) / count))
}
plusMinus(arr: [1,2,3,4,5,10,2])
