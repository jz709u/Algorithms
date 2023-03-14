//: [Previous](@previous)

import Foundation

func _max(array: [Int], result: Int = .min) -> Int {
    if array.count == 0 { return result }
    return _max(array: Array(array[1...]), result: max(array[0], result))
}

_max(array: [1,2,5,24,2,42,100])
//: [Next](@next)
