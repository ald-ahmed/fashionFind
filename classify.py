import tensorflow as tf
import sys
import os

# Disable tensorflow compilation warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf



image_path = sys.argv[1]

def run(image_path):
    # Read the image_data
    image_data = tf.gfile.FastGFile(image_path, 'rb').read()

    # Loads label file, strips off carriage return
    label_lines = [line.rstrip() for line
                   in tf.gfile.GFile("/Users/ahmed.al.dulaimy@ibm.com/PycharmProjects/fashionFind/tf_files/retrained_labels.txt")]

    # Unpersists graph from file
    with tf.gfile.FastGFile("/Users/ahmed.al.dulaimy@ibm.com/PycharmProjects/fashionFind/tf_files/retrained_graph.pb", 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

    string = ""

    with tf.Session() as sess:
        # Feed the image_data as input to the graph and get first prediction
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')

        predictions = sess.run(softmax_tensor, \
                               {'DecodeJpeg/contents:0': image_data})

        # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]

        links = dict()
        links["converse"] = "https://www.amazon.com/Converse-Mens-Original-Chuck-Sneakers/dp/B00QSSORYS/"
        links["whitevans"] = "https://www.amazon.com/Vans-Authentic-Unisex-Skate-Trainers/dp/B00ML10XTO/"
        links["addidas"] = "https://www.amazon.com/adidas-Originals-Superstar-Fashion-Sneaker/dp/B00LLS5EVK/"

        count = 0
        for node_id in top_k:
            count += 1
            human_string = label_lines[node_id]
            score = predictions[0][node_id]
            if count == 1:
                string += links[str(human_string).lower()]
            # string += "<br>"+str(human_string)+": " + str(score*100.0)
            print('%s (score = %.5f)' % (human_string, score))

    return string