// Link to kata : https://www.codewars.com/kata/57f780909f7e8e3183000078

package kata

func Grow(arr []int) int {
	final := 1

	for _, item := range arr {
		final *= item
	}
	return final
}
