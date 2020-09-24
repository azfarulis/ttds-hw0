# LAB 0

How to read a text file from hard-disk. This lab is optional for those who are not fully confident about their programming skills. There is nothing specific to be done in this lab more than reading a text file from HD word by word, which is the most basic skill you need to have to be able to take the course.

# PROGRAMMING LANGUAGES

You need to have Perl or Python on your machine (you still can use something else) if you prefer.
If you are using Dice, then you should have them there. Check with demonstrators how to run them.

## DOWNLOAD A SAMPLE TEXT FILE

Download the following file, which has the text of the Bible: [link](http://www.gutenberg.org/cache/epub/10/pg10.txt)

## SKILLS TO DO WITH THE FILE

You need to be confident with the following skills with any programming language when dealing with a text file:

- Reading and Writing into text files
- Reading text by word, and calling functions to process word if required (e.g. lower case word letters)
- Regular expressions would be very useful to know

## USEFUL TIPS

**Useful Shell Commands** 
Print frequency of unique terms in a given collection: 
- `cat text.file | tr " " "\n" | tr "A-Z" "a-z" | sort | uniq -c | sort -n > terms.freq`
- `cat text.file | perl -p -e "s/[^\w]+/\n/g" | tr "A-Z" "a-z" | sort | uniq -c | sort -n > terms.freq`