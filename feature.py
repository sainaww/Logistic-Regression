import argparse
import collections

def parse_command_line():
    parser = argparse.ArgumentParser(description='Read the command line')
    parser.add_argument('train_input')
    parser.add_argument('validation_input')
    parser.add_argument('test_input')
    parser.add_argument('dict_input')
    parser.add_argument('formatted_train_out')
    parser.add_argument('formatted_validation_out')
    parser.add_argument('formatted_test_out')
    parser.add_argument('feature_flag', type=int)
    parser.add_argument('threshold')
    args = parser.parse_args()
    return args


def convert_dicttxt_to_dict(filename):
    dict_of_dict = {}
    with open(filename, 'r') as file:
        for line in file:
            word, index = line.strip().split(" ")
            dict_of_dict[word] = int(index)
    return dict_of_dict


def format_input_file(in_filename, out_filename, dictionary, model, threshold):
    with open(in_filename, 'r') as in_file:
        with open(out_filename, 'w') as out_file:
            lines = in_file.readlines()
            for line in lines:
                list_of_label_and_reviews = line.strip().split("\t")
                list_of_words_in_reviews = list_of_label_and_reviews[1].split(" ")
                if model == 1:
                    dict_of_wordindexes_in_reviews = collections.OrderedDict()
                    formatted_line = [list_of_label_and_reviews[0]]
                    for word in list_of_words_in_reviews:
                        if word in dictionary:
                            if word in dict_of_wordindexes_in_reviews:
                                dict_of_wordindexes_in_reviews[word] += 1
                            else:
                                dict_of_wordindexes_in_reviews[word] = 1
                    for index in dict_of_wordindexes_in_reviews.keys():
                        formatted_line.append(str(dictionary[index])+":1")
                    out_file.write('\t'.join(formatted_line))
                    out_file.write('\n')
                else: #model 2
                    dict_of_wordindexes_in_reviews = collections.OrderedDict()
                    formatted_line = [list_of_label_and_reviews[0]]
                    for word in list_of_words_in_reviews:
                        if word in dictionary:
                            if word in dict_of_wordindexes_in_reviews:
                                dict_of_wordindexes_in_reviews[word] += 1
                            else:
                                dict_of_wordindexes_in_reviews[word] = 1
                    for index, value in dict_of_wordindexes_in_reviews.items():
                        if value < threshold:
                            formatted_line.append(str(dictionary[index])+":1")
                    out_file.write('\t'.join(formatted_line))
                    out_file.write('\n')


def main():
    args = parse_command_line()
    dict_of_dict = convert_dicttxt_to_dict(args.dict_input)
    format_input_file(args.train_input, args.formatted_train_out, dict_of_dict, args.feature_flag, args.threshold)
    format_input_file(args.validation_input, args.formatted_validation_out, dict_of_dict, args.feature_flag, args.threshold)
    format_input_file(args.test_input, args.formatted_test_out, dict_of_dict, args.feature_flag, args.threshold)


if __name__ == '__main__':
    main()
