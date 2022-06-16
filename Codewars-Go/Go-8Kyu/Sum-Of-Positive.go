// Link to kata : https://www.codewars.com/kata/5715eaedb436cf5606000381

package kata

func PositiveSum(numbers []int) int {
	var final int

	for _, item := range numbers {
		if item >= 0 {
			final += item
		}
	}
	return final
}
