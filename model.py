from keras.layers import (Conv2D, Flatten, MaxPooling2D, Input, 
                                            BatchNormalization, Dropout, Dense, 
                                            Reshape, Permute, Lambda, DepthwiseConv2D, GlobalAveragePooling2D)
from keras.models import Model
import tensorflow as tf

def create_model(input_shape = (48,48,1),num_classes=7, num_heads=8):

    input = Input(shape=input_shape)
    x = Conv2D(filters=256,kernel_size=(3,3),activation='relu',padding='same')(input)

    x = Conv2D(filters=512,kernel_size=(3,3),activation='relu',padding='same')(x)
    x = BatchNormalization()(x)

    x = MaxPooling2D(pool_size=(2,2))(x)
    x = Dropout(0.4)(x)

    x = Conv2D(filters=384,kernel_size=(3,3),activation='relu',padding='same')(x)
    x = BatchNormalization()(x)

    x = MaxPooling2D(pool_size=(2,2))(x)
    x = Dropout(0.4)(x)

    x = Conv2D(filters=192,kernel_size=(3,3),activation='relu',padding='same')(x)
    x = BatchNormalization()(x)

    x = MaxPooling2D(pool_size=(2,2))(x)
    x = Dropout(0.4)(x)


    x = Conv2D(filters=384,kernel_size=(3,3),activation='relu',padding='same')(x)
    x = BatchNormalization()(x)

    x = MaxPooling2D(pool_size=(2,2))(x)
    x = Dropout(0.4)(x)

    # # Multi-head self-attention
    # def multi_head_self_attention(x):
    #     num_channels = tf.shape(x)[-1]
    #     num_heads = num_channels // num_heads
    #     queries = Dense(num_heads * num_channels)(x)
    #     keys = Dense(num_heads * num_channels)(x)
    #     values = Dense(num_heads * num_channels)(x)

    #     queries = Reshape((-1, num_heads, num_channels // num_heads))(queries)
    #     keys = Reshape((-1, num_heads, num_channels // num_heads))(keys)
    #     values = Reshape((-1, num_heads, num_channels // num_heads))(values)

    #     queries = Permute((2, 1, 3))(queries)
    #     keys = Permute((2, 3, 1))(keys)
    #     values = Permute((2, 1, 3))(values)

    #     attention_scores = Lambda(lambda a: tf.matmul(a[0], a[1]) / tf.math.sqrt(tf.cast(num_channels // num_heads, tf.float32)))([queries, keys])
    #     attention_weights = Lambda(lambda a: tf.nn.softmax(a, axis=-1))(attention_scores)

    #     output = Lambda(lambda a: tf.matmul(a[0], a[1]))([attention_weights, values])
    #     output = Permute((2, 1, 3))(output)
    #     output = Reshape((-1, num_channels))(output)

    #     return output

    # x = multi_head_self_attention(x)

    x = Flatten()(x)

    x = Dense(256,activation='relu')(x)
    x = BatchNormalization()(x)

    x = Dropout(0.3)(x)
    x = Dense(num_classes,activation='softmax')(x)

    return Model(input,x,name='fer_model')

# multi-branch attention cnn
# def create_model(input_shape=(48, 48, 1), num_classes=7):
#     input = Input(shape=input_shape)
    
#     x = Conv2D(filters=64, kernel_size=(3,3), strides=1, activation='relu', padding='same')(input)

#     x = Conv2D(filters=64, kernel_size=(3,3), strides=1, activation='relu', padding='same')(x)

#     x = Conv2D(filters=128, kernel_size=(3,3), activation='relu', padding='same')(x)

#     x = Conv2D(filters=128, kernel_size=(3,3), strides=2, activation='relu', padding='same')(x)

#     x = Conv2D(filters=512, kernel_size=(3,3), strides=2, activation='relu', padding='same')(x)

#     x = Conv2D(filters=256, kernel_size=(3,3), activation='relu', padding='same')(x)

#     x = Conv2D(filters=512, kernel_size=(1,1), strides=2, activation='relu', padding='same')(x)

#     x = Conv2D(filters=512, kernel_size=(3,3), activation='relu', padding='same')(x)

#     x = DepthwiseConv2D(kernel_size=(3, 3), padding='same', activation='relu')(x)
#     x = Conv2D(filters=1024, kernel_size=(1, 1), activation='relu', padding='same')(x)

#     x = DepthwiseConv2D(kernel_size=(3, 3), padding='same', activation='relu')(x)
#     x = Conv2D(filters=1024, kernel_size=(1, 1), activation='relu', padding='same')(x)

#     x = GlobalAveragePooling2D()(x)

#     x = Dense(1024, activation='relu')(x)

#     output = Dense(num_classes, activation='softmax')(x)

#     return Model(input, output, name='fer2013')

if __name__=='__main__':
    model = create_model()
    model.summary()
