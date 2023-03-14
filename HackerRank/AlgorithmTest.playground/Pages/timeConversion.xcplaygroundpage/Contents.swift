//: [Previous](@previous)

import Foundation

var greeting = "Hello, playground"

//: [Next](@next)
/// https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
func timeConversion(s: String) -> String {
    // Write your code here
    let ampm = String(s.suffix(2))
    let minute = String(s[s.index(s.startIndex, offsetBy: 3)..<s.index(s.startIndex, offsetBy: 5)])
    let second = String(s[s.index(s.startIndex, offsetBy: 6)..<s.index(s.startIndex, offsetBy: 8)])
    let hour = Int(String(s[s.index(s.startIndex, offsetBy: 0)..<s.index(s.startIndex, offsetBy: 2)]))
    guard var _hour = hour else { return "" }
     if ampm == "AM" && _hour == 12 {
        _hour = 0
    } else if ampm == "PM" && _hour != 12 {
        _hour += 12
    }
    if _hour == 0 {
        return "00:\(minute):\(second)"
    } else if _hour < 10 {
        return "0\(_hour):\(minute):\(second)"
    }
    return "\(_hour):\(minute):\(second)"
}

timeConversion(s: "06:40:03AM")
