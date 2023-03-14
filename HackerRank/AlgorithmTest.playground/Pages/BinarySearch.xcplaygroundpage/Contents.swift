//: [Previous](@previous)

import Foundation

func recursiveBinarySearch(array: [Int], find value: Int) -> Bool {
    func _binarySearch(array: ArraySlice<Int>, find value: Int) -> Bool {
        print("lookin in array \(array) for: \(value)")
        if array.count == 0 { return false }
        let midDistance = array.distance(from: array.startIndex, to: array.endIndex) / 2
        let midIndex = array.index(array.startIndex, offsetBy: midDistance)
        if array[midIndex] == value {
            return true
        } else if value > array[midIndex] {
            let indexAfterMid = array.index(after: midIndex)
            return _binarySearch(array: array[indexAfterMid...], find: value)
        } else {
            return _binarySearch(array: array[..<midIndex], find: value)
        }
    }
    
    let sortedA = array.sorted()
    return _binarySearch(array: sortedA[...], find: value)
}

recursiveBinarySearch(array: [1,2,45,50,242,10,500], find: 300)

//: [Next](@next)
