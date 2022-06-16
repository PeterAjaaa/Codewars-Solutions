// Link to kata : https://www.codewars.com/kata/576bb71bbbcf0951d5000044/

package kata

func CountPositivesSumNegatives(numbers []int) []int {
	var res []int
	var count int
	var final int

	for _, item := range numbers {
		if item > 0 {
			count += 1
		} else {
			final += item
		}
	}
	return append(res, count, final)
}
