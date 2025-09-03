import cv2
import numpy as np
import os
import sys
import tensorflow as tf

from sklearn.model_selection import train_test_split

# Global constants for the model configuration
EPOCHS = 10              # Number of training epochs
IMG_WIDTH = 30           # Width of input images
IMG_HEIGHT = 30          # Height of input images
NUM_CATEGORIES = 43      # Number of traffic sign categories
TEST_SIZE = 0.4          # Proportion of data to use for testing


def main():
    """
    Main function that loads traffic sign data, builds and trains the model,
    and evaluates its performance.
    """
    # Check command-line arguments
    if len(sys.argv) not in [2, 3]:
        sys.exit("Usage: python traffic.py data_directory [model.h5]")

    # Get image arrays and labels for all image files
    images, labels = load_data(sys.argv[1])

    # Split data into training and testing sets
    labels = tf.keras.utils.to_categorical(labels)
    x_train, x_test, y_train, y_test = train_test_split(
        np.array(images), np.array(labels), test_size=TEST_SIZE
    )

    # Get a compiled neural network
    model = get_model()

    # Fit model on training data
    model.fit(x_train, y_train, epochs=EPOCHS)

    # Evaluate neural network performance
    model.evaluate(x_test,  y_test, verbose=2)

    # Save model to file if filename provided
    if len(sys.argv) == 3:
        filename = sys.argv[2]
        model.save(filename)
        print(f"Model saved to {filename}.")


def load_data(data_dir):
    """
    Load image data from directory `data_dir`.

    Args:
        data_dir: Path to directory containing traffic sign images organized by category

    Returns:
        Tuple of (images, labels) where:
        - images is a numpy array of resized and normalized image arrays
        - labels is a numpy array of corresponding category labels
    """
    images = []
    labels = []

    # Loop through each category directory (0 to NUM_CATEGORIES-1)
    for category in range(NUM_CATEGORIES):
        # Construct path to category directory
        category_dir = os.path.join(data_dir, str(category))

        # Skip if directory doesn't exist
        if not os.path.isdir(category_dir):
            continue

        # Process each image in the category directory
        for image_file in os.listdir(category_dir):
            # Skip non-image files
            if not image_file.lower().endswith(('.png', '.jpg', '.jpeg', '.ppm', '.bmp')):
                continue

            # Construct full image path
            image_path = os.path.join(category_dir, image_file)

            try:
                # Read image using OpenCV
                image = cv2.imread(image_path)

                # Skip if image couldn't be read
                if image is None:
                    continue

                # Convert from BGR to RGB color space
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

                # Resize image to specified dimensions
                image = cv2.resize(image, (IMG_WIDTH, IMG_HEIGHT))

                # Normalize pixel values to [0, 1] range
                image = image / 255.0

                # Add image and label to our collections
                images.append(image)
                labels.append(category)
            except Exception as e:
                print(f"Error processing {image_path}: {e}")
                continue

    # Convert lists to numpy arrays for better performance
    return (np.array(images), np.array(labels))


def get_model():
    """
    Build and compile a convolutional neural network model for traffic sign classification.

    Returns:
        A compiled TensorFlow Keras model with architecture:
        - 3 convolutional layers with increasing filters
        - Batch normalization and max pooling after each conv layer
        - 2 dense layers with dropout for regularization
        - Output layer with softmax activation
    """
    # Create sequential model
    model = tf.keras.models.Sequential([
        # First convolutional block
        tf.keras.layers.Conv2D(
            32, (3, 3), activation="relu",
            input_shape=(IMG_WIDTH, IMG_HEIGHT, 3),
            kernel_regularizer=tf.keras.regularizers.l2(0.001)  # L2 regularization
        ),
        tf.keras.layers.BatchNormalization(),  # Normalize activations
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),  # Downsample feature maps

        # Second convolutional block
        tf.keras.layers.Conv2D(
            64, (3, 3), activation="relu",
            kernel_regularizer=tf.keras.regularizers.l2(0.001)
        ),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

        # Third convolutional block
        tf.keras.layers.Conv2D(
            128, (3, 3), activation="relu",
            kernel_regularizer=tf.keras.regularizers.l2(0.001)
        ),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

        # Flatten 3D feature maps to 1D vector
        tf.keras.layers.Flatten(),

        # First dense layer with dropout
        tf.keras.layers.Dense(256, activation="relu",
                            kernel_regularizer=tf.keras.regularizers.l2(0.001)),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Dropout(0.5),  # Randomly drop 50% of units to prevent overfitting

        # Second dense layer with dropout
        tf.keras.layers.Dense(128, activation="relu",
                            kernel_regularizer=tf.keras.regularizers.l2(0.001)),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Dropout(0.3),  # Randomly drop 30% of units

        # Output layer with softmax activation for multi-class classification
        tf.keras.layers.Dense(NUM_CATEGORIES, activation="softmax")
    ])

    # Configure model training with Adam optimizer
    optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
    model.compile(
        optimizer=optimizer,
        loss="categorical_crossentropy",  # Suitable for multi-class classification
        metrics=["accuracy"]              # Track accuracy during training
    )

    return model


if __name__ == "__main__":
    main()
