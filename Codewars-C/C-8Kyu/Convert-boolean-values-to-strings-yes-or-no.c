// Link to kata : https://www.codewars.com/kata/53369039d7ab3ac506000467/

const char *bool_to_word (int value);

const char *bool_to_word (int value){
  if (value == 1){
    return "Yes";
  }else{
    return "No";
  }
}
