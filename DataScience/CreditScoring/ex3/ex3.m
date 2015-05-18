%% Machine Learning Online Class - Exercise 3 | Part 1: One-vs-all


%% Initialization
clear ; close all; clc

%% Setup the parameters you will use for this part of the exercise
input_layer_size  = 10;  % 20x20 Input Images of Digits
num_labels = 1;          % 10 labels, from 1 to 10
                          % (note that we have mapped "0" to label 10)

%% =========== Part 1: Loading and Visualizing Data =============
%  We start the exercise by first loading and visualizing the dataset.
%  You will be working with a dataset that contains handwritten digits.
%

% Load Training Data
fprintf('Loading and Visualizing Data ...\n')

%XandY = csvread('cs-training_weka_octave.csv');
XandY = csvread('~/Practice_Python/DataScience/CreditScoring/training.csv');
X = XandY(:, 3:12);
y = XandY(:, 2);
size(X)
size(y)
m = size(X, 1);

%Xvalandyval = csvread('~/Practice_Python/DataScience/CreditScoring/crossValidation.csv');
Xvalandyval = csvread('~/Practice_Python/DataScience/CreditScoring/test.csv');

Xval = Xvalandyval(:, 3:12);
yval = Xvalandyval(:, 2);

% feature scaling
for c = 1:size(X, 2)
  X(:, c) = (X(:, c) - mean(X(:, c)))/std(X(:, c));
endfor

for c = 1:size(Xval, 2)
  Xval(:, c) = (Xval(:, c) - mean(Xval(:, c)))/std(Xval(:, c));
endfor



%% ============ Part 2: Vectorize Logistic Regression ============
%  In this part of the exercise, you will reuse your logistic regression
%  code from the last exercise. You task here is to make sure that your
%  regularized logistic regression implementation is vectorized. After
%  that, you will implement one-vs-all classification for the handwritten
%  digit dataset.
%

fprintf('\nTraining One-vs-All Logistic Regression...\n')

lambda = 0.1;
all_theta = oneVsAll([ones(m, 1) X], y, num_labels, lambda); %okay with and without []

fprintf('Program paused. Press enter to continue.\n');
pause;


%% ================ Part 3: Predict for One-Vs-All ================
%  After ...
pred = predictOneVsAll(all_theta, X);

fprintf('\nTraining Set Accuracy: %f\n', mean(double(pred == y)) * 100);



%% ================= learning curve ===============
%  Next, you should implement the learningCurve function.
%
%  Write Up Note: Since the model is underfitting the data, we expect to
%                 see a graph with "high bias" -- slide 8 in ML-advice.pdf
%

lambda = 0;
numExamples = linspace(10000, 90000, 17);
%numExamples = linspace(1, 6001, 100);

p = size(numExamples, 2);
[error_train, error_val] = ...
    learningCurve([ones(m, 1) X], y, ...
                  [ones(size(Xval, 1), 1) Xval], yval, ...
                  lambda, numExamples);

plot(1:p, error_train, 1:p, error_val);
title('Learning curve for linear regression')
legend('Train', 'Cross Validation')
xlabel('Number of training examples')
ylabel('Error')
axis([0 p+1 0 0.3])

fprintf('# Training Examples\tTrain Error\tCross Validation Error\n');
for i = 1:p
    fprintf('  \t%d\t\t%f\t%f\n', i, error_train(i), error_val(i));
end

fprintf('Program paused. Press enter to continue.\n');
pause;
