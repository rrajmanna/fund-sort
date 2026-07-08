import pooch
import spikeinterface.extractors as se

# Download a small (10 second) simulated recording with known ground truth
# directly, bypassing datalad
url = "https://gin.g-node.org/NeuralEnsemble/ephy_testing_data/raw/master/mearec/mearec_test_10s.h5"
local_path = pooch.retrieve(url=url, known_hash=None, fname="mearec_test_10s.h5", path="data/raw")

# Load it as a recording (the raw traces) and a "sorting" (the true spike times)
recording, sorting_true = se.read_mearec(local_path)

print("Recording info:")
print(recording)
print()
print("Ground truth sorting info:")
print(sorting_true)
print()
print(f"Downloaded to: {local_path}")
