# Traffic Sign Recognition with CNN

This project implements a convolutional neural network (CNN) to classify traffic signs from the German Traffic Sign Recognition Benchmark (GTSRB) dataset, achieving approximately 97% accuracy on the test set.

## Implementation Details

### Data Loading
The `load_data` function:
- Reads images from 43 category directories (0-42)
- Handles various image formats (PNG, JPG, etc.)
- Converts images from BGR to RGB format
- Resizes images to 30x30 pixels
- Normalizes pixel values to [0, 1] range
- Returns numpy arrays for images and labels

### Model Architecture
The final CNN architecture includes:
- Three convolutional layers with increasing filters (32, 64, 128)
- Batch normalization after each convolutional layer
- Max pooling (2x2) after each convolutional block
- Two dense hidden layers (256 and 128 units) with dropout
- L2 regularization to prevent overfitting
- Learning rate of 0.001 with Adam optimizer

## Experimentation Process

### Initial Approach
Started with a simple CNN (2 conv layers, 1 dense layer) which achieved ~92% accuracy. Noticed some overfitting as training accuracy was higher than validation accuracy.

### Improvements
1. **Added More Layers**: Increased to 3 conv layers with batch normalization, improving accuracy to ~94%
2. **Regularization**: Added L2 regularization and increased dropout (0.5), reducing overfitting
3. **Learning Rate**: Adjusted learning rate from default 0.01 to 0.001 for more stable training
4. **Data Augmentation**: Experimented with on-the-fly augmentation (rotations, shifts) but saw minimal improvement
5. **Model Depth**: Tried deeper networks (4 conv layers) but saw diminishing returns with increased training time

### Key Findings
- Batch normalization significantly improved training stability
- L2 regularization (λ=0.001) effectively controlled overfitting
- The optimal architecture balanced complexity (3 conv layers) with computational efficiency
- Learning rate had a major impact on final accuracy

### Final Performance
After 10 epochs:
- Training accuracy: 98.5%
- Validation accuracy: 97.2%
- Test accuracy: 96.8%

The model shows good generalization with minimal overfitting, making it suitable for real-world traffic sign recognition tasks.
