// Link to kata : https://www.codewars.com/kata/56cd44e1aa4ac7879200010b

package kata

import "unicode"

type MyString string

func (s MyString) IsUpperCase() bool {
	x := []rune(s)

	for _, item := range x {
		if unicode.IsLower(item) == true {
			return false
		}
	}
	return true
}
