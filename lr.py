import argparse
import math

def parse_command_line_lr():
    parser = argparse.ArgumentParser(description='Read the command line')
    parser.add_argument('formatted_train_out')
    parser.add_argument('formatted_validation_out')
    parser.add_argument('formatted_test_out')
    parser.add_argument('dict_input')
    parser.add_argument('train_out')
    parser.add_argument('test_out')
    parser.add_argument('metrics_out')
    parser.add_argument('num_epoch', type=int)
    args = parser.parse_args()
    return args


def convert_formatted_file_to_dict(filename):
    with open(filename, 'r') as in_file:
        labels = []
        list_of_dictionaries = []
        lines = in_file.readlines()
        for line in lines:
            list_of_indexes = line.strip().split("\t")
            labels.append(int(list_of_indexes[0]))
            review_words = {-1:1}
            for index in list_of_indexes[1:]:
                review_words[int(index[:-2])] = 1
            list_of_dictionaries.append(review_words)
        # print list_of_dictionaries
        return list_of_dictionaries, labels



def carry_out_SGD(list_of_dictionaries, labels, num_epoch):
    theta = {}
    for epoch in xrange(num_epoch):
        #for every example
        for i, review_words in enumerate(list_of_dictionaries):
            dot_product = 0.0
            #for every word in example
            for j in review_words.keys():
                dot_product += theta.get(j, 0)
            for j in review_words.keys():
                if j in theta:
                    theta[j] = theta[j] + 0.1* 1.0 * (labels[i] - sigmoid(dot_product))
                else:
                    theta[j] = 0.1* 1.0 * (labels[i] - sigmoid(dot_product))
    return theta


def sigmoid(dot_product):
    return math.exp(dot_product) / (1 + math.exp(dot_product))


def predict_labels(list_of_dictionaries, theta):
    list_of_predicted_labels =[]
    for dictionary in list_of_dictionaries:
        dot_product = 0.0
        for key in dictionary.keys():
                dot_product += theta.get(key, 0)
        if dot_product > 0:
            list_of_predicted_labels.append(1)
        else:
            list_of_predicted_labels.append(0)
    return list_of_predicted_labels


def write_to_labels_file(list, file_name):
    file = '{}.labels'.format(file_name)
    with open(file_name, 'w') as file:
        for label in list:
            file.write("%d\n" %label)


def output_metrics(labels_train, predicted_list_train, labels_test, predicted_list_test, file_name):
    count_train = 0.0
    total_train = len(labels_train)
    count_test = 0.0
    total_test = len(labels_test)
    for i in xrange(total_train):
        if labels_train[i] != predicted_list_train[i]:
            count_train +=1.0
    for i in xrange(total_test):
        if labels_test[i] != predicted_list_test[i]:
            count_test +=1.0
    error_train = count_train/total_train
    error_test = count_test/total_test
    with open(file_name, 'w') as file:
        file.write("error(train) : {}\nerror(test) : {}".format(error_train, error_test))


def main():
    args = parse_command_line_lr()
    list_of_dictionaries_train, labels_train = convert_formatted_file_to_dict(args.formatted_train_out)
    theta_train = carry_out_SGD(list_of_dictionaries_train, labels_train, args.num_epoch)
    predicted_list_train = predict_labels(list_of_dictionaries_train, theta_train)
    list_of_dictionaries_valid, labels_valid = convert_formatted_file_to_dict(args.formatted_validation_out)
    # predicted_list_valid = predict_labels(list_of_dictionaries_valid, theta_valid)
    list_of_dictionaries_test, labels_test = convert_formatted_file_to_dict(args.formatted_test_out)
    predicted_list_test = predict_labels(list_of_dictionaries_test, theta_train)
    write_to_labels_file(predicted_list_train, args.train_out)
    write_to_labels_file(predicted_list_test, args.test_out)
    output_metrics(labels_train, predicted_list_train, labels_test, predicted_list_test, args.metrics_out)


if __name__=='__main__':
    main()
