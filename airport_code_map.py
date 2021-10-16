# coding=utf-8
import random
import time

SUBJECT_LIST = ["三字代码", "城市", "机场名称", "省份"]
SUBJECT_DICT = {
    "三字代码": 0,
    "城市": 1,
    "机场名称": 2,
    "省份": 3
}

def read_file(filename):
    """传入一个文件名，读取文件并将文件内容以列表类型返回"""
    try:
        f = open(r".\%s" % filename, "r", encoding="utf-8")
        content = f.readlines()
        for i in range(content.__len__()):
            content[i] = content[i].replace('\n', '')
        f.close()
        return content
    except Exception as ret:
        print(ret, "读取文件错误")


def sort_list(data):
    """整理列表，分割每个元素"""
    sorted_data = list()
    for i in data:
        if type(i) == str:
            sorted_data.append(i.split(" "))
    return sorted_data


def print_whole(data):
    """打印所有城市"""
    for i in range(data.__len__()):
        print(data[i])

def random_quest_number(quest):
    return random.randint(0, quest.__len__()-1)

def gen_random_sequence_list(data):
    result = list()
    for i in range(data.__len__()):
        result.append(i)
    random.shuffle(result)
    return result

def gen_normal_sequence_list(data):
    result = list()
    for i in range(data.__len__()):
        result.append(i)
    return result

def gen_quiz(data, quest=None, key=1):
    """根据数据生成单个题目"""
    if quest == None:
        quest = random_quest_number(data)
    answer = list()  # 用于记录用户填写的答案
    result = [quest, False]  # 用于记录回答的结果，[题号，是否有错题]

    # 提问并接收作答
    for i in range(4):
        if i != key:
            answer.append(
                (i, input("%s\"%s\"的 %s 是：" % (SUBJECT_LIST[key], data[quest][key], SUBJECT_LIST[i])))
                )

    # 比对答案，返回结果
    for i in answer:
        sequence = i[0]
        if i[1] == data[quest][sequence]:
            pass
        else:
            print("回答错误，%s 的 %s 是 \"%s\"" % (
                data[quest][key], SUBJECT_LIST[sequence], data[quest][sequence]))
            result[1] = True
    return result


def quiz(data, key=1, mode="1"):
    """生成一个完整的试卷"""
    if mode == "2":
        sequence_list = gen_random_sequence_list(data)
    else:
        sequence_list = gen_normal_sequence_list(data)
    result = list()
    for i in sequence_list:
        ret = gen_quiz(data, i, key)
        if ret[1]:
            result.append(ret[0])
        print()
    return result


def print_result(data, result):
    total = data.__len__()
    correct = total - result.__len__()
    percent = (correct/total)*100
    print()
    print("==================考试结束=====================")
    print()
    if result == []:
        print("恭喜你，全部正确")
        return
    print("你答对的题目数为%s/%s，正确率为%s%%" % (correct, total, percent))
    time.sleep(3)
    print()
    print("你的错题为：")
    for i in result:
        print(data[i])

def get_key():
    while True:
        msg = input("你想考察\"三字代码\", \"城市\", \"机场名称\", \"省份\"中的哪一项？\n>>")
        result = SUBJECT_DICT.get(msg)
        if result:
            print()
            print()
            break
        else:
            print()
            print("非法输入，请输入你想考察的科目名称，例：城市")
            print("你不需要输入双引号")
            print("--------------------------------")
    return result

def gen_mode():
    while True:
        mode = input("如何考试？\n输入1顺序考试\n输入2乱序考试\n>>")
        if mode in ("1", "2"):
            return mode
        else:
            print()
            print("非法输入，请输入\"1\"或\"2\"")
            print("你不需要输入双引号")
            print("--------------------------------")


def list_filter(data, sequence):
    """过滤列表，保留特定的信息"""
    new_data = list()
    for i in range(data.__len__()):
        if i in sequence:
            new_data.append(data[i])
    return new_data

def main():
    restart = True
    while True:
        if restart:
            restart = False
            airport_code_list = read_file("database.txt")
            key = get_key()
            mode = gen_mode()
            sorted_airport_list = sort_list(airport_code_list)
        print("========================考试开始==========================")
        result = quiz(sorted_airport_list, key=key, mode=mode)
        print_result(sorted_airport_list, result)
        print("\n")
        next_move = input("继续考试？\n输入1重新考试\n输入2重做错题\n不输入将退出\n>>")
        if next_move == "":
            break
        elif next_move == "1":
            restart = True
        elif next_move == "2":
            sorted_airport_list = list_filter(sorted_airport_list, result)
            if not sorted_airport_list:
                break


if __name__ == "__main__":
    main()
    
