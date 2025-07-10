def remove_long_lines(input_filename, output_filename, max_length):
    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        for line in infile:
            if len(line) == max_length:
                outfile.write(line)

# 示例调用
input_filename = 'words_alpha.txt'  # 输入文件名
output_filename = 'words_alpha-4.txt'  # 输出文件名
max_length = 5  # 设定最大行长度

remove_long_lines(input_filename, output_filename, max_length)
