def num_images(data):
    """
    Count the number of images in the given JSON data.

    Parameters:
    - data (dict): JSON data containing image information.

    Returns:
    - int or None: Number of images if 'images' key exists in the data, None otherwise.
    """
    if "images" in data:
        return len(data["images"])
    return None
def image_size(data):
    """
    Find the largest and smallest image sizes in the given JSON data.

    Parameters:
    - data (dict): JSON data containing image information.

    Returns:
    - tuple or (None, None): Tuple containing the largest and smallest image dictionaries
                             (width, height) if 'images' key exists in the data, (None, None) otherwise.
    """
    if "images" in data:
        images = data["images"]
        dimension = 0
        largest_image_size = 0
        smallest_image_size = float("inf")
        largest_image = None
        smallest_image = None
        for image in images:
            dimension = image["height"] * image["width"]
            if dimension > largest_image_size:
                largest_image_size = dimension
                largest_image = image
            if dimension < smallest_image_size:
                smallest_image_size = dimension
                smallest_image = image
                
        return largest_image, smallest_image
    return None, None


def mean_size(data):
    """
    Find the image closest to the mean size in the given JSON data.

    Parameters:
    - data (dict): JSON data containing image information.

    Returns:
    - dict or None: Dictionary containing information about the image closest to the mean size
                   if 'images' key exists in the data, None otherwise."""
    if "images" in data:
        images=data["images"]      
        mean_heights=(sum(image["height"] for image in images))/len(images)     
        mean_width=(sum(image["width"] for image in images))/len(images)
        closest_image=min(images,key=lambda img:abs(img.get("height")-mean_heights)+abs(img.get("width")-mean_width))
        return closest_image 
    return None