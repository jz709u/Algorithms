//: [Previous](@previous)

import Foundation

func sumTailRecursion(array: [Int], result: Int = 0) -> Int {
    if array.count == 0 {
        return result
    }
    return sumTailRecursion(array: Array(array[1...]), result: result + array[0])
}

sumTailRecursion(array: [1,20,2,3,4,10])

func sumNoTailRecurion(array: [Int]) -> Int {
    if array.count == 0 {
        return 0
    }
    return array[0] + sumNoTailRecurion(array: Array(array[1...]))
}

sumNoTailRecurion(array: [12,5,1,2,20])

func sumWithoutRecursion(array: [Int]) -> Int {
    var result = 0
    for i in array {
        result += i
    }
    return result
}

sumWithoutRecursion(array: [12,5,1,2,20])


//: [Next](@next)
