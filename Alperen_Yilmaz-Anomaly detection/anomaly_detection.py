import matplotlib.pyplot as plt
import numpy as np
from data_stream_generator import data_stream #import data_stream_sim func from data_stream_generator

# ===========================================================================
#   Developer:
#   Alperen Yilmaz
#   alpican55@gmail.com
#   Date: 12/09/2024
#
#   NOTES:
#       -This program requires Numpy
#       -This program made for application to Cobblestone Energies Graduate Software Engineer role
# ===========================================================================

"""
I will use Z-score and Sliding window for my research project for Cobblestone energy

I choose to use a statistical method instead of a machine learning method like and Isolation Forest

Because I chose Z-score because its more simple, straightforward and fast. It works great against random spikes.
But I'm aware that this algorithm is weak against drift.

I consider Isolation Forest because its more robust and versatile.
Reason why I didn't choose this algorithm is that I had to train it and I think Isolation Forest will be a better choice for bigger data sets.

My steps are:
1. Calculate Mean and Standard Deviation
2. Calculate Z-score using Z=(data point - mean of the dataset)/standard deviation of the dataset

For data analysis and compute the Z-score I will be using Sliding window technique.
"""

"""
I used Numpy because program will be more optimized and efficient with Numpy. 
But I didn't have I could've been use built-in Python libraries like statistics.

I used matplotlib because without this external library it would be very hard to visualize.
"""

def anomaly_detection(data_stream, threshold=1.5, window_size=30):
    """
    Perform anomaly detection using Z-score.
    
    Parameters:
    - data_stream: Generator that yields data points.
    - threshold: Z-score threshold to detect anomalies.
    - window_size: Number of data points in the sliding window for calculations.
    """
    data_points = []  # List to store incoming data points
    anomalies = []  # List to store anomalies detected
    anomaly_count = 0  # Track the number of anomalies detected
    
    try:
        for data_point in data_stream:
            # Validate data_point to ensure it's a number
            if not isinstance(data_point, (int, float)):
                raise ValueError(f"Invalid data point encountered: {data_point}")

            data_points.append(data_point)  # Append the data point to the list

            # Ensure the data window is larger than the window_size
            if len(data_points) > window_size:
                window_data = np.array(data_points[-window_size:])
                mean = np.mean(window_data)
                std_dev = np.std(window_data)

                # Prevent division by zero
                if std_dev > 0:
                    z_score = (data_point - mean) / std_dev  # Z-score formula

                    # Detect anomaly if Z-score exceeds the threshold
                    if np.abs(z_score) > threshold:
                        anomaly_count += 1
                        anomalies.append((len(data_points), data_point, z_score))
                        print(f"Anomaly detected {len(data_points)}: {data_point} (Z-score: {z_score})")

            # Call visualization function every 200 data points to optimize performance
            if len(data_points) % 200 == 0:
                visualize_data(data_points, anomalies, anomaly_count)

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print(f"Anomaly detection completed. Total anomalies: {anomaly_count}")

def visualize_data(data_points, anomalies, anomaly_count):
    """
    Visualize the data stream and detected anomalies.

    Parameters:
    - data_points: List of data points from the data stream.
    - anomalies: List of detected anomalies.
    - anomaly_count: Total count of detected anomalies.
    """
    try:
        plt.figure(figsize=(13, 8))
        plt.plot(data_points, label='Data Stream')

        if anomalies:
            anomaly_indices, anomaly_values, _ = zip(*anomalies)
            plt.scatter(anomaly_indices, anomaly_values, color='#276DD4', label='Anomalies')

        plt.title('Efficient Data Stream Anomaly Detection - Cobblestone Energy Research Project', fontsize=20)
        plt.xlabel('Data Points')
        plt.ylabel('Value')
        plt.legend()
        plt.text(0.95, 0.05, f'Anomalies: {anomaly_count}', transform=plt.gca().transAxes,
                 horizontalalignment='right', verticalalignment='bottom', fontsize=14, color='red')
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"An error occurred during visualization: {e}")

# Example usage
if __name__ == "__main__":
    try:
        stream = data_stream()  # Ensure the data stream function works correctly
        anomaly_detection(stream, threshold=1.5, window_size=30)
    except Exception as e:
        print(f"An error occurred in the main program: {e}")