// Link to kata: https://www.codewars.com/kata/56efc695740d30f963000557/

package kata

import (
	"strings"
	"unicode"
)

func ToAlternatingCase(str string) string {
	final, runes := []string{}, []rune(str)

	for i := range runes {
		if unicode.IsUpper(runes[i]) == true {
			final = append(final, strings.ToLower(string(runes[i])))
		} else if unicode.IsLower(runes[i]) == true {
			final = append(final, strings.ToUpper(string(runes[i])))
		} else {
			final = append(final, string(runes[i]))
		}
	}
	return strings.Join(final, "")
}
