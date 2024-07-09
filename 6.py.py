def number_to_words(n):
    if n == 1000:
        return "one thousand"
        
    ones = ["","one","two","three","four","five","six","seven","eight","nine"]
    teens = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seveteen","eighteen","nineteen"]
    tens =["","","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
    words = ""
    hundreds = n// 100
    remainder = n % 100
    
    if hundreds > 0:
        words += ones[hundreds] + "hundred"
        if remainder > 0:
            words += "and"
    if remainder < 10:
        words += ones [remainder]
    elif remainder < 20:
        words += teens[remainder-10]
    else:
        tens_digit = remainder // 10
        ones_digit = remainder % 10
        words += tens[tens_digit]
        if ones_digit > 0:
            words += " " + ones[ones_digit]
    return words
     
def count_letters_in_words():
    total_letters = 0
    for  i in range(1,1001):
        words = number_to_words(i)
        
    words = words.replace(" ","").replace("-","")
    total_letters += len(words)
    return total_letters
total_letters = count_letters_in_words()
print(total_letters)
  
        
        