import nidaqmx
import matplotlib.pyplot as plt
import numpy as np

def main() -> None:
    
    with nidaqmx.Task() as task:
        
        # Configure/aquire channel 16
        task.ai_channels.add_ai_voltage_chan("Dev1/ai16", min_val=-5, max_val=5)
        task.ai_channels.add_ai_voltage_chan("Dev1/ai17", min_val=-5, max_val=5)

        # Set sampling rate
        task.timing.cfg_samp_clk_timing(16000)
        
        # Read 100 samples worth of data
        data = np.array(task.read(1600))

        fit, ax = plt.subplots()
        ax.plot(range(0, len(data[0])), data[0])
        ax.plot(range(0, len(data[1])), data[1])
        plt.show()

    # TODO:
    # Assume all points attached to some node
    # Assume/calculate frequency
    # Compute Amplitude + Phase of each channel
    # Compute inverses for correction
    # Repeat across multiple samples

    # End result is sparse scaling identy array / vector of all correction factors

if __name__ == "__main__":
    main()