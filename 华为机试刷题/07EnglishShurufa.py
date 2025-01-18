import re 

str1 = input()
prew = input()

prelen = len(prew)

s = set()
resultWords = []

pattern = re.compile('\w*')

for e in pattern.finditer(str1):
    s.add(e.group())

# print(s)

for e in s:
    if len(e)>=prelen and e[0:prelen] == prew:
        resultWords.append(e)

resultWords.sort()

if resultWords:
    print(' '.join(map(str,resultWords)))

else:
    print(prew)



import re
 
# 使用正则表达式提取单词，并处理包含撇号的单词
def tokenize(text):
    tokens = []
    word_regex = re.compile(r"\b\w+('\w+)?\b")  # 匹配单词，允许撇号连接的单词
    matches = word_regex.finditer(text)
 
    for match in matches:
        word = match.group(0)
        pos = word.find("'")
        if pos != -1:
            # 如果存在撇号，分割单词
            tokens.append(word[:pos])
            tokens.append(word[pos+1:])
        else:
            # 添加整个单词
            tokens.append(word)
    return tokens
 
# 根据前缀过滤并排序单词
def filter_and_sort_words(words, prefix):
    filtered = set()
    for word in words:
        if word.startswith(prefix):
            filtered.add(word)
    return sorted(filtered)
 
def main():
    import sys
    input = sys.stdin.read
    data = input().split('\n')
    
    text = data[0]
    prefix = data[1]
 
    # 对文本进行分词以提取单词
    words = tokenize(text)
 
    # 根据前缀过滤并排序单词
    result = filter_and_sort_words(words, prefix)
 
    # 输出结果
    if not result:
        print(prefix)
    else:
        print(" ".join(result))
 
if __name__ == "__main__":
    main()