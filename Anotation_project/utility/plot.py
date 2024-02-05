import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
def plot_image_width(data):
    """
    Plot the probability density of image widths.

    Parameters:
    - data (dict): JSON data containing image information.
    """
    images=data["images"]
    width=[image.get("width") for image in images]
    scaling_factor = 2.0
    max_plot_width = 900
    mu, sigma = np.mean(width), np.std(width)
    xmin, xmax = plt.xlim()
    plt.xlim(xmin, max_plot_width )
    x = np.linspace(xmin, max_plot_width, 1000)
    p = scaling_factor*norm.pdf(x, mu, sigma)
    plt.plot(x, p, 'k', linewidth=1)
    plt.xlabel('Width')
    plt.ylabel('Probability Density')

    plt.axvline(mu, color='red', linestyle='--', linewidth=2, label=f'Mean Width: {mu:.2f}')

    title = "Fit results: mu = %.2f,  std = %.2f" % (mu, sigma)
    plt.title(title)
    plt.legend()
    plt.show()    
