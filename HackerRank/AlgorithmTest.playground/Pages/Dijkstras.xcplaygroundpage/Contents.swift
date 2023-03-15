//: [Previous](@previous)

import Foundation

class Graph {
    let source: Int
    let dest: Int
    var nodes: [Node]
    
    init(source: Int,
         dest: Int,
         nodes: Int,
         edges: [[Edge]]
    ) {
        self.source = source
        self.dest = dest
        var _nodes = [Node]()
        for node in 0..<nodes {
            let _edges = edges[node]
            _nodes += [Node(id: node, edges: _edges)]
        }
        _nodes[source].score = 0
        self.nodes = _nodes
    }
}

class Node: CustomDebugStringConvertible {
    var id: Int
    var score: Double = .infinity
    var visited: Bool = false
    var edges: [Edge]
    var routeToNode: Node?
    init(id: Int, edges: [Edge]) {
        self.id = id
        self.edges = edges
    }
    var isNotVisited: Bool { !visited }
    var debugDescription: String {
        self.description
    }
    var description: String {
        "id \(id) score: \(score) visited: \(visited) edges: \(edges) routeToNode: \(routeToNode?.id)"
    }
}

class Edge: CustomDebugStringConvertible {
    let neighborID: Int
    let weight: Double
    init(neighborID: Int, weight: Double) {
        self.neighborID = neighborID
        self.weight = weight
    }
    
    var debugDescription: String {
        "neighbor \(neighborID) weight: \(weight)"
    }
}

struct Path {
    let targetNode: Node
    let score: Double
    init(targetNode: Node) {
        //var routes = [Node]()
        score = targetNode.score
        self.targetNode = targetNode
    }
    var path: String {
        var begin = " <- score:\(targetNode.score) id:\(targetNode.id)"
        var newNode = targetNode.routeToNode
        while newNode != nil {
            begin += " <- score:\(newNode!.score) id:\(newNode!.id)"
            newNode = newNode?.routeToNode
        }
        return begin
    }
}

func nodeWithLowestScore(graph: Graph) -> Node? {
    var result: Node?
    for node in graph.nodes {
        if !node.visited && node.score < result?.score ?? .infinity  {
            result = node
        }
    }
    return result
}

func dijkstra(graph: Graph) -> Path? {
    while let currentNode = nodeWithLowestScore(graph: graph) {
        currentNode.visited = true
        for edge in currentNode.edges where graph.nodes[edge.neighborID].isNotVisited {
            let newScore = currentNode.score + edge.weight
            if newScore < graph.nodes[edge.neighborID].score {
                graph.nodes[edge.neighborID].score = newScore
                graph.nodes[edge.neighborID].routeToNode = currentNode
            }
        }
        if currentNode.id == graph.dest {
            return .init(targetNode: currentNode)
        }
    }
    return nil
}

// Example usage:
let edges = [
    [Edge(neighborID: 1, weight: 4), Edge(neighborID: 2, weight: 1)], // 0: -1-> 2
    [Edge(neighborID: 3, weight: 1)],                                 // 1: -1-> 3
    [Edge(neighborID: 1, weight: 2), Edge(neighborID: 3, weight: 5)], // 2: -2-> 1
    [Edge(neighborID: 4, weight: 3)],                                 // 3: -3-> 4
    [Edge(neighborID: 0, weight: 1), Edge(neighborID: 3, weight: 1)]
]
let shortestDistances = dijkstra(graph: .init(source: 0, dest: 3, nodes: 5, edges: edges))
print(shortestDistances?.path)


//: [Next](@next)
