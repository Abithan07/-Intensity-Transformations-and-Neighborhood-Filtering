def histogram_equalization(image):
    """Apply histogram equalization to a grayscale image."""
    hist, _ = np.histogram(image.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_normalized = np.ma.masked_equal(cdf, 0)
    cdf_normalized = (cdf_normalized - cdf_normalized.min()) * 255 / (cdf_normalized.max() - cdf_normalized.min())
    return np.ma.filled(cdf_normalized, 0).astype('uint8')[image]


original_img = cv2.imread("a1images/shells.tif", cv2.IMREAD_GRAYSCALE)
equalized_img = histogram_equalization(original_img)