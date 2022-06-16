// Link to kata : https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0

package kata

func RemoveChar(word string) string {
	return word[1 : len(word)-1]
}

// This function take substring with direct byte slice.
// This handles only ASCII correctly.

// Another way would be to turn the string into a rune slice
// And after "cutting" the part that we wanted, turn it back into a string

// runes := []rune(value)
// safeSubstring := string(runes[1:3])
// fmt.Println(safeSubstring)

// Reference here : https://www.dotnetperls.com/substring-go
