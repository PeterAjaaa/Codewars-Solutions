// Link to kata : https://www.codewars.com/kata/56606694ec01347ce800001b

package kata

func IsTriangle(a, b, c int) bool {
	if a+b > c && b+c > a && c+a > b {
		return true
	} else {
		return false
	}
}

// A quick way to check if a sequence of numbers is a "triangle-sequence" is to check
// if the sequence met these 3 conditions :
// a + b > c
// b + c > a
// c + a > b
