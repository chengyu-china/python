# 定义一个字典类型，并使用字典的get方法
def card_value(card):
    card_map = {"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13,"A":14}
    return card_map.get(card,0)
# 判断一个数组是不是连续递增的，连续递增1
def cards_match(card_numbers):
    i = 1
    while i < len(card_numbers):
        if card_numbers[i] - card_numbers[i-1] != 1:
            return False
            break
        else:
            i += 1
    return True

# 使用双指针算法，初始的offset是5。 如果这个是连续递增的list，则 j+1，再判断新的list是不是连续递增的list
def find_sequences(card_numbers):

    sequences = []  # 用来存储最后的结果

    i , j = 0,5

    pre = 0

    if len(card_numbers) < 5:
        return sequences
    else:
        while j <= len(card_numbers):
            if cards_match(card_numbers[i:j]):
                if j == len(card_numbers): # 终止条件
                    sequences.append(card_numbers[i:j]) 
                    break
                else:
                    j += 1 
                    pre = 1 # 这个是一个标记为，表示在 j+1之前的list 是满足条件的。 
            elif pre == 1: # 如果j+1之后不满足条件，这list 到j截止。
                sequences.append(card_numbers[i:j-1])
                i = j - 1 # 下一个长度为5的list
                j = i + 5 
                pre = 0
            else: # 表示长度5的不满足，则窗口向前移动。
                i += 1 
                j += 1
    
        return sequences


def main():
    input_cards = input().split()
    # 下面的用法很精炼，
    card_numbers = [card_value(card) for card in input_cards if card_value(card) != 0]

    card_numbers.sort()

    sequences = find_sequences(card_numbers)

    if not sequences:
        print("No")
    else:
        for seq in sequences:
            output_seq = []
            for e in seq:
                if e == 11:
                    output_seq.append('J')
                elif e == 12:
                    output_seq.append('Q')
                elif e == 13:
                    output_seq.append('K')
                elif e == 14:
                    output_seq.append('A')
                else:
                    output_seq.append(str(e))
            # 快速的返回list，切去掉list 两头的 '[]'
            print(''.join(output_seq))


if __name__ == "__main__":
    main()



# 3 4 5 6 7 9 10 J Q K A 8 9 

