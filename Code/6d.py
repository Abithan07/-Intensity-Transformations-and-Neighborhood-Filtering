# Compute the cumulative sum of the histogram
cumsum_hist = np.cumsum(hist)

# Normalize the cumulative sum
cumsum_hist = cumsum_hist * hist.max() / cumsum_hist.max()