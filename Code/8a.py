def nearest_neighbor_zoom(image, scale_factor):
    # Use cv2 to perform nearest neighbor interpolation
    height, width = image.shape[:2]
    new_dimensions = (int(width * scale_factor), int(height * scale_factor))
    
    # Resizing with INTER_NEAREST for nearest-neighbor interpolation
    resized_image = cv2.resize(image, new_dimensions, interpolation=cv2.INTER_NEAREST)
    
    return resized_image