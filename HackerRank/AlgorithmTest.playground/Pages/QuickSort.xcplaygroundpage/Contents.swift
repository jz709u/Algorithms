//: [Previous](@previous)

import Foundation

func quickSort(array: [Int]) -> [Int] {
    func _quickSort(arraySlice: [Int]) -> [Int] {
        print("array slice \(arraySlice)")
        if arraySlice.count < 2 {
            return Array(arraySlice)
        }
        let middle = arraySlice.distance(from: arraySlice.startIndex, to: arraySlice.endIndex) / 2
        let pivotIndex = arraySlice.index(arraySlice.startIndex, offsetBy: middle)
        let less = arraySlice
            .enumerated()
            .compactMap { $0 != pivotIndex && arraySlice[pivotIndex] > $1 ? $1 : nil }
        let greater = arraySlice
            .enumerated()
            .compactMap { $0 != pivotIndex && arraySlice[pivotIndex] < $1 ? $1 : nil }
        
        return _quickSort(arraySlice: less) + [arraySlice[pivotIndex]] + _quickSort(arraySlice: greater)
    }
    
    return _quickSort(arraySlice: array)
}

print(quickSort(array: [1,52,24,242,22,2,3]))

//: [Next](@next)
