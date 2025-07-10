from spellwise import Levenshtein

def read_file_and_process(filename):
    result = []
    with open(filename, 'r') as file:
        for line in file:
            # 去除从.开始的部分
            line = line.split('.')[0]  # 如果只想去掉.及之后的字符
            result.append(line.strip())  # 去掉每行的多余空白字符
    return result


# Initialise the algorithm
levenshtein = Levenshtein()
# Index the words from a dictionary
levenshtein.add_from_path("./words_alpha-4.txt")


filename = 'success.txt'  # 替换为实际文件名
lines = read_file_and_process(filename)
for line in lines:
    suggestions = levenshtein.get_suggestions(line)
    #print("=================")
    #for suggestion in suggestions[0:3]:
    #    print("{} {} \t {}".format(line, suggestion.get("word"), suggestion.get("distance")))
    if len(suggestions) > 0 and suggestions[0].get("distance") == 0:
        print(f"{line}")
        #print("{} {} \t {}".format(line, suggestions[0].get("word"), suggestions[0].get("distance")))


