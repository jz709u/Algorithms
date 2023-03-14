//: [Previous](@previous)

import Foundation

var greeting = "Hello, playground"

//: [Next](@next)

func combos<T>(elements: ArraySlice<T>, k: Int) -> [[T]] {
    if k == 0 {
        return [[]]
    }

    guard let first = elements.first else {
        return []
    }

    let head = [first]
    let subcombos = combos(elements: elements, k: k - 1)
    var ret = subcombos.map { head + $0 }
    ret += combos(elements: elements.dropFirst(), k: k)

    return ret
}

func combos<T>(elements: Array<T>, k: Int) -> [[T]] {
    return combos(elements: ArraySlice(elements), k: k)
}

//283781779

func roadNetwork(roadNodes: Int, roadFrom: [Int], roadTo: [Int], roadWeight: [Int]) -> Int {
    
    // sum all weights that go into a node
    // O(r)
    var roadNodeToSumOfAllWeights = [Int: Int]()
    for i in 0..<roadFrom.count {
        let from = roadFrom[i]
        let to = roadTo[i]
        let weight = roadWeight[i]
        if let currentWeightFrom = roadNodeToSumOfAllWeights[from] {
            roadNodeToSumOfAllWeights[from] = currentWeightFrom + weight
        } else {
            roadNodeToSumOfAllWeights[from] = weight
        }
        if let currentWeightTo = roadNodeToSumOfAllWeights[to] {
            roadNodeToSumOfAllWeights[to] = currentWeightTo + weight
        } else {
            roadNodeToSumOfAllWeights[to] = weight
        }
    }
    
    // generate all combinations
    let array = Array(1...roadNodes)
    // enumerated == O(1)
    // O(n^2)
    let combos: [(from: Int, to: Int)] = array.enumerated().flatMap { (i, fromNode) in
        array.dropFirst(i + 1).map { toNode in return (from: fromNode, to: toNode) }
    }
    
    // produce of all weights
    // O(n)
    let productOfAllWeights = combos.reduce(into: 1) { result, nodePair in
        if let sumOfAllWeights = roadNodeToSumOfAllWeights[nodePair.to] {
            result *= sumOfAllWeights
        }
    }
    
    // mod 10 ^ 9  + 7
    let moduloM = 1000000007
    return productOfAllWeights % moduloM
}

//3 3
//1 2 3
//2 3 1
//1 3 2

roadNetwork(roadNodes: 3, roadFrom: [1,2,1], roadTo: [2,3,3], roadWeight: [3,1,2])
