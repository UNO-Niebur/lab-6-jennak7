#WordCount.py
#Name: Jenna Kramer
#Date: 02/28/26
#Assignment: Lab 6

def main():
  try:
    textFile = open("gettysberg.txt", 'r')
    lineCount = 0
    wordCount = 0
    characterCount = 0

    for line in textFile:
      lineCount = lineCount + 1
      words = line.split()

      # print(words)
      for w in words: 
        wordCount = wordCount + 1
        for characters in w:
          characterCount = characterCount + 1

    print("Lines:", lineCount)
    print("Words:", wordCount)
    print("Characters:", characterCount)
  except FileNotFoundError:
    print("File not found")
  

if __name__ == '__main__':
  main()
