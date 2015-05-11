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

XandY = csvread('cs-training_weka_octave.csv');
X = XandY(:, 1:10);
y = XandY(:, 11);
size(X)
size(y)
m = size(X, 1);

% feature scaling
for c = 1:size(X, 2)
  X(:, c) = (X(:, c) - mean(X(:, c)))/std(X(:, c));
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
all_theta = oneVsAll(X, y, num_labels, lambda); %okay with and without []

fprintf('Program paused. Press enter to continue.\n');
pause;


%% ================ Part 3: Predict for One-Vs-All ================
%  After ...
pred = predictOneVsAll(all_theta, X);

fprintf('\nTraining Set Accuracy: %f\n', mean(double(pred == y)) * 100);
