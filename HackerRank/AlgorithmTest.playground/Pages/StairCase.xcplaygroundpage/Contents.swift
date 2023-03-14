//: [Previous](@previous)

import Foundation
/// https://www.hackerrank.com/challenges/staircase/problem?isFullScreen=true
func staircase(n: Int) -> Void {
    if n == 0 { return }
    for i in 1...n {
        print(String.init(repeating: " ", count: n - i)
        + String.init(repeating: "#", count: i))
    }
}

