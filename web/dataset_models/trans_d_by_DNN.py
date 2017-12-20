from base import register, get_model_path

MODEL_NAME = 'DNN'

register(MODEL_NAME)

import tensorflow as tf
import numpy as np
from dataset_preproces.pp_trans_d import *

path = get_model_path(MODEL_NAME)

feature_columns = [tf.feature_column.numeric_column("x", shape=[15])]

# Build 3 layer DNN with 10, 20, 10 units respectively.
classifier = tf.estimator.DNNClassifier(feature_columns=feature_columns,
                                        hidden_units=[20, 30, 20, 10, 10],
                                        n_classes=22,
                                        model_dir=path,
                                        )

# Define the training inputs
train_input_fn = tf.estimator.inputs.numpy_input_fn(
    x={"x": train_X},
    y=train_Y,
    num_epochs=None,
    shuffle=True)

# Train model.
classifier.train(input_fn=train_input_fn, steps=20000)

# Define the test inputs
valid_input_fn = tf.estimator.inputs.numpy_input_fn(
    x={"x": valid_X},
    y=valid_Y,
    num_epochs=1,
    shuffle=True)

# Evaluate accuracy.
accuracy_score = classifier.evaluate(input_fn=valid_input_fn)["accuracy"]

print("\nTest Accuracy: {0:f}\n".format(accuracy_score))

new_samples = test_X[:100]

predict_input_fn = tf.estimator.inputs.numpy_input_fn(
    x={"x": new_samples},
    num_epochs=1,
    shuffle=False)

predictions = list(classifier.predict(input_fn=predict_input_fn))
predicted_classes = [p["classes"] for p in predictions]

print(
    "New Samples, Class Predictions:    {}\n"
        .format(predicted_classes))

print(test_Y[:5])

#
#
#
#
#
_X = test_X[:1000]
_Y = test_Y[:1000]
test_input_fn = tf.estimator.inputs.numpy_input_fn(
    x={"x": _X},
    y=_Y,
    num_epochs=1,
    shuffle=True)
#
#
#
#
# 计算召回率  和 F1Score
preds = list(classifier.predict(input_fn=test_input_fn))
p_classes = [p["classes"] for p in preds]
y_pred = np.asarray(p_classes).astype('int')
y_pred = y_pred.reshape(y_pred.shape[0])
y_true = _Y

print('===>')
print(y_pred.shape)
print(y_true.shape)

print(y_true)
# print(y_pred * y_true)
#
TP = np.count_nonzero(y_pred * y_true)
print("TP", TP)
TN = np.count_nonzero((y_pred - 1) * (y_true - 1))
print("TN", TN)
FP = np.count_nonzero(y_pred * (y_true - 1))
print("FP", FP)
FN = np.count_nonzero((y_pred - 1) * y_true)
print("FN", FN)

precision = TP / (TP + FP)
recall = TP / (TP + FN)

print("precision -------->")
print(precision)
print("recall -------->")
print(recall)
f1 = 2 * precision * recall / (precision + recall)
print("F1 ------->")
print(f1)
