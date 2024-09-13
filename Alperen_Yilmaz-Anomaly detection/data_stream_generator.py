import time
import numpy as np

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
This program generates a stream of data with seasonal patterns using sinusoidal functions, random noise, and anomalies.

The anomaly rate is %5
"""

def data_stream():
    """
    Simulate a continuous data stream with seasonality, noise, and anomalies.

    Yields:
        float: Simulated data point from the stream.
    """
    try:
        t = 0
        while True:
            # Seasonal component (sinusoidal pattern)
            seasonality = 10 * np.sin(0.2 * t)

            # Noise (random uniform distribution)
            noise = np.random.uniform(-2, 2)

            # Anomalies introduced randomly
            anomaly = 0
            if np.random.rand() < 0.05:  # 5% chance of generating an anomaly
                anomaly = np.random.uniform(20, 30)

            # Combine seasonality, noise, and potential anomaly
            data_point = seasonality + noise + anomaly
            yield data_point

            t += 1  # Increment time
            time.sleep(0.05) #To simulate real life situation a delay for every data to generate
            print(f"{t}.Data: {data_point}")
    except Exception as e:
        print(f"An error occurred in the data stream generation: {e}")

# Example usage
if __name__ == "__main__":
    try:
        stream = data_stream()#example
        print(next(stream))#test
    except Exception as e:
        print(f"An error occurred in the main program: {e}")