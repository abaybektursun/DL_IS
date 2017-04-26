import os
import sys
import subprocess
import pandas as pd

import matplotlib
matplotlib.use('Agg')
import matplotlib.pylab as plt

plt.style.use('ggplot')


CAFFE_PATH = '/usr/local/caffe/'
print('Assuming Caffe is located here:'+CAFFE_PATH)
try:
    LOG_MODEL_PATH = sys.argv[1]
    IMAGE_SAVE_PATH = sys.argv[2]
except:
    print('Usage: python plot.py [Path to the model log] [Path where to store the image]')
    sys.exit()

#Get directory where the model logs is saved, and move to it
DIR_LOG_MODEL_PATH = os.path.dirname(LOG_MODEL_PATH)
os.chdir(DIR_LOG_MODEL_PATH)


# Test, train log generation

#Parsing training/validation logs
command = CAFFE_PATH + '/tools/extra/parse_log.sh ' + LOG_MODEL_PATH
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
process.wait()
#Read training and test logs
train_log_path = LOG_MODEL_PATH + '.train'
test_log_path = LOG_MODEL_PATH + '.test'
train_log = pd.read_csv(train_log_path, delim_whitespace=True)
test_log = pd.read_csv(test_log_path, delim_whitespace=True)



#Making learning curve

fig, ax1 = plt.subplots()

#Plotting training and test losses
train_loss, = ax1.plot(train_log['#Iters'], train_log['TrainingLoss'], color='red',  alpha=.5)
test_loss, = ax1.plot(test_log['#Iters'], test_log['TestLoss'], linewidth=2, color='green')
ax1.set_ylim(ymin=0, ymax=1)
ax1.set_xlabel('Iterations', fontsize=15)
ax1.set_ylabel('Loss', fontsize=15)
ax1.tick_params(labelsize=15)
#Plotting test accuracy
ax2 = ax1.twinx()
test_accuracy, = ax2.plot(test_log['#Iters'], test_log['TestAccuracy'], linewidth=2, color='blue')
ax2.set_ylim(ymin=0, ymax=1)
ax2.set_ylabel('Accuracy', fontsize=15)
ax2.tick_params(labelsize=15)
#Adding legend
plt.legend([train_loss, test_loss, test_accuracy], ['Training Loss', 'Test Loss', 'Test Accuracy'],  bbox_to_anchor=(1, 0.8))
plt.title('Training Curve', fontsize=18)
#Saving learning curve
plt.savefig(IMAGE_SAVE_PATH)


# Dele the training and test logs

command = 'rm ' + train_log_path
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
process.wait()

command = command = 'rm ' + test_log_path
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
process.wait()

