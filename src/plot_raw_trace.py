import matplotlib.pyplot as plt
import spikeinterface.extractors as se

local_path = "data/raw/mearec_test_10s.h5"
recording, sorting_true = se.read_mearec(local_path)

# Grab 1 second of data from the first channel
fs = recording.get_sampling_frequency()
trace = recording.get_traces(start_frame=0, end_frame=int(fs * 1), channel_ids=[recording.channel_ids[0]])

plt.figure(figsize=(12, 4))
plt.plot(trace)
plt.title("Raw extracellular trace — Channel 0 (first 1 second)")
plt.xlabel("Sample")
plt.ylabel("Voltage (uV)")
plt.tight_layout()
plt.savefig("figures/raw_trace_channel0.png")
print("Saved plot to figures/raw_trace_channel0.png")
