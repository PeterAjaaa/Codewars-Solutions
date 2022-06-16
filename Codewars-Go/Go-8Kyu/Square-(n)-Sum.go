// Link to kata : https://www.codewars.com/kata/515e271a311df0350d00000f/

package kata

func SquareSum(numbers []int) int {
	var final int

	for _, item := range numbers {
		final += item * item
	}
	return final
}
