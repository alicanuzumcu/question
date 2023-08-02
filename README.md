# question
Elimininating duplicated letters and finding the longest word with length. 
For example, input:'ALICCAN' => output:'ALIC' and length:4
input:'ABBCDDEFGGGH' => output:'DEFG' and length:4

Examples are clear to understand logic i think, however we should be careful about small and big letters because
computers understand as like different letters. To get rid of this problem we ı have used a built in function which 
makes all letters big so the problem is solved now.
For example if we wouldn't solve the problem it would be like that, input:'ALICcAN' => output:'ALICcAN' and length:7

To sperate nonduplicated words ı make two empty lists and then create a for loop. If the word is not duplicated we will
add it to the second list(name:listt) else if we have duplicated letter the second list will be added to the first list (word_box).

In the final part we should define the longest , calculate the length and integrate the letters which inside of the list.
