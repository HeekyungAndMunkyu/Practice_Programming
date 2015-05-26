clear
clc
close all

% addpath to the libsvm toolbox
addpath('~/Downloads/libsvm-3.20');
% addpath('/home/hyun/octave/statistics-1.2.4');
% addpath to the data
dirData = '~/Practice_Python/DataScience/CreditScoring';
addpath(dirData);

train = csvread('~/Practice_Python/DataScience/CreditScoring/training.csv');
train_label = train(:,2);
train_inst = train(:,3:end);
train_N = size(train_label);

cross = csvread('~/Practice_Python/DataScience/CreditScoring/crossValidation.csv');
cross_label = cross(:,2);
cross_inst = cross(:,3:end);
cross_N = size(cross_label);

test = csvread('~/Practice_Python/DataScience/CreditScoring/test.csv');
test_label = test(:,2);
test_inst = test(:,3:end);
test_N = size(test_label);

% test = csvread('/home/hyun/Desktop/libsvm-3.20/train_zero.csv');
% test_label = test(:,2);
% test_inst = test(:,3:end);
% test_N = size(test_label);

% Determine the train and test index
trainIndex = zeros(train_N,1);
trainIndex(1:500,1) = 1;
crossIndex = zeros(cross_N,1);
crossIndex(1:300,1) = 1;
testIndex = zeros(test_N,1);
testIndex(1:200,1) = 1;

trainData = train_inst(trainIndex==1,:);
trainLabel = train_label(trainIndex==1,:);
crossData = cross_inst(crossIndex==1,:);
crossLabel = cross_label(crossIndex==1,:);
testData = test_inst(testIndex==1,:);
testLabel = test_label(testIndex==1,:);

% Train the SVM
train_model = svmtrain(trainLabel, trainData, '-c 1 -g 0.07 -b 1');
cross_model = svmtrain(crossLabel, crossData, '-c 1 -g 0.07 -b 1');

%model = svmtrain(trainLabel, trainData, '-t 0');
% Use the SVM model to classify the data

[predict_train_label, train_accuracy, train_prob_values] = svmpredict(testLabel, testData, train_model, '-b 1'); % run the SVM model on the test data
 [predict_cross_label, cross_accuracy, cross_prob_values] = svmpredict(testLabel, testData, cross_model, '-b 1');
