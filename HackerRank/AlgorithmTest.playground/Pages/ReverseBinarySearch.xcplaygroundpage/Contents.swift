//: [Previous](@previous)

import Foundation

var greeting = "Hello, playground"

//: [Next](@next)
extension Array where Element == Int {
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

"]"
