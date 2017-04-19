import numpy as np
import matplotlib.pyplot as plt

# Make sure that caffe is on the python path:
caffe_root = '/usr/local/caffe' 
import sys
sys.path.insert(0, caffe_root + 'python')

import caffe

# Set the right path to your model definition file, pretrained model weights,
# and the image you would like to classify.
MODEL_FILE = 'cifar_full.prototxt'
PRETRAINED = 'cifar_full_iter_65000.caffemodel.h5'
IMAGE_FILE = '/home/abaybektursun/IS/source/data/merged/test/ISIC_0012050.jpg'

caffe.set_mode_gpu();
caffe.set_device(0);

net = caffe.Classifier(MODEL_FILE, PRETRAINED,
                       mean=np.load('/home/abaybektursun/projects/GitHub/IndependentStudy/source/data/mean.npy').mean(1).mean(1),
                       channel_swap=(2,1,0),
                       raw_scale=255,
                       image_dims=(128, 128))
input_image = caffe.io.load_image(IMAGE_FILE)
plt.imshow(input_image)

prediction = net.predict([input_image])  # predict takes any number of images, and formats them for the Caffe net automatically
print 'prediction shape:', prediction[0].shape
plt.plot(prediction[0])
print 'predicted class:', prediction[0].argmax()
plt.show()
