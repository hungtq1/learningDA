import tensorflow as tf
from tensorflow import keras #Keras: Framework để xác định mạng neural như là một chuỗi các layers.
import numpy as np 
#Keras: Framework để xác định mạng neural như là một chuỗi các layers.

#loss: dùng để đo độ chính xác của phương trình dự đoán (ví dụ y = 4x + 1).
#optimizer: đưa ra phương trình dự đoán, dựa trên giá trị mà function loss đưa ra, function optimizer sẽ đưa ra câu trả lời sao cho giá trị của function loss nhỏ nhất.
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

#loss: dùng để đo độ chính xác của phương trình dự đoán (ví dụ y = 2x).
#optimizer: đưa ra phương trình dự đoán, dựa trên giá trị mà function loss đưa ra, function optimizer sẽ đưa ra câu trả lời sao cho giá trị của function loss nhỏ nhất.


model.compile(optimizer='sgd', loss='mean_squared_error')
xs = np.array([-3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0], dtype=float)
ys = np.array([-9.0, -6.0, -3.0, 0.0, 3.0, 6.0, 9.0], dtype=float)
model.fit(xs, ys, epochs=50)
print(model.predict([8.0]))

#
# Tóm tắt
# Có những khái niệm cơ bản cần nắm khi tìm hiểu về Machine learning.
# Data: dữ liệu đầu vào.
# Label: đầu ra (hay còn gọi là nhãn).
# Model: được tạo ra từ data và label, sử dụng model để dự đoán những data khác.
# Thư viện numpy: một thư viện toán học phổ biến và mạnh mẽ của Python.
# Thư viện tensorflow: thư viện mã nguồn mở hỗ trợ cho việc tính toán số học dựa trên biểu đồ mô tả sự thay đổi của dữ liệu.
# Loss: hàm đánh giá độ chính xác của giá trị dự đoán.
# Optimizer: hàm đưa ra giá trị dự đoán sao cho giá trị của hàm loss là nhỏ nhất.
# Epochs: Số lần lặp khi train model.
# Neural network: là một hệ thống tính toán lấy cảm hứng từ sự hoạt động của các neuron trong hệ thần kinh.
# Trên đây là những khái niệm cơ bản về Machine learning, hy vọng sẽ giúp ích cho những bạn mới tìm hiểu về lĩnh vực này.
