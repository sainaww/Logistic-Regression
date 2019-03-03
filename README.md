# Logistic-Regression
This program  implements a working Natural Language Processing (NLP) system, i.e., a sentiment polarity analyzer, using binary logistic regression. The algorithm is used to determine whether a review is positive or negative using movie reviews as data.
## Getting Started

Download feature.py and lr.py

### Prerequisites

The aim was to not use any fancy packages. So there are no prerequisites. This program only uses packages included in Python 2.7's standard library. All you need is the dataset in the form of a tsv file. The program takes as input a tsv file where the labels are in the first column, and the second column is the moview reviews.

### Running the program

feature.py takes in 9 command line arguments. The purpose of feature.py is to do feature engineering and get rid of the features it finds impertinent.

1. <train input>: path to the training input .tsv file
2. <validation input>: path to the validation input .tsv file
3. <test input>: path to the test input .tsv file
4. <dict input>: path to the dictionary input .txt file
5. <formatted train out>: path to output .tsv file to which the feature extractions on the training data should be written
6. <formatted validation out>: path to output .tsv file to which the feature extractions on the validation data should be written
7. <formatted test out>: path to output .tsv file to which the feature extractions on the test data should be written
8. <feature flag>: integer taking value 1 or 2 that specifies whether to construct the Model 1 feature set or the Model 2 feature set- that is, if feature_flag==1 use Model 1 features; if feature_flag==2 use Model 2 features
9. <threshold>: integer taking any value that specifies the maximum number of times a word can appear in the movie review and still be considered pertinent
  
For example:

```
$ python feature.py train_data.tsv valid_data.tsv test_data.tsv dict.txt formatted_train.tsv formatted_valid.tsv formatted_test.tsv 1 4
```

lr.py takes in 8 command-line arguments: <formatted train input> <formatted validation input> <formatted test input> <dict input> <train out> <test out> <metrics out> <num epoch>.

1. <formatted train input>: path to the formatted training input .tsv file 
2. <formatted validation input>: path to the formatted validation input .tsv file 
3. <formatted test input>: path to the formatted test input .tsv file 
4. <dict input>: path to the dictionary input .txt file 
5. <train out>: path to output .labels file to which the prediction on the training data should be written 
6. <test out>: path to output .labels file to which the prediction on the test data should be written 
7. <metrics out>: path of the output .txt file to which metrics such as train and test error should be written 
8. <num epoch>: integer specifying the number of times Stochastic Gradient Descent loops through all of the training data
  
For example:

```
 $ python lr.py formatted_train.tsv formatted_valid.tsv formatted_test.tsv dict.txt train_out.labels test_out.labels metrics_out.txt 60
```
