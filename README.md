# Analyzing the 'Shape' of Data - Persistent Homology
**Mentor:** Dr. Zhixu Su  
**TA:** Chengyuan Ma  
**Undergraduate students:** Caroline Ding, Zongze Li

Topological data analysis uses techniques from topology to understand the ‘shape’ of data set, which can be high dimensional and noisy. Given a point cloud data set, one can construct a nested sequence of complexes thickening the data set at different scales. Persistent homology detects topological features of the complexes that persist over a range of scales, it computes the numbers of connected components, 1-dimensional holes (loops), 2-dimensional holes (voids), etc, and keeps track of the birth and death scale of the features.

In this project, we learned various methods of building filtered simplicial complexes and understand the standard algorithm for computing persistent homology. In the end of the project, we applied one of the methods of buildinng filtered simplicial complexes - **Lazy Witness Complex** to visiualize the shape of genus 5 surface equation in Python.


## Genus 5 Surface
Genus 5 surface should look like:  
<img width="190" alt="genus 5 surface" src="https://user-images.githubusercontent.com/120891991/208362844-7eaaea3f-4828-45a8-b5a6-2949aff2f860.png">  
The implicit surface equation of genus 5 surface is:
$$3 + 8 (x^4 + y^4 + z^4) = 8 (x^2 + y^2 + z^2)$$
You can find more information [here](https://mathworld.wolfram.com/ChmutovSurface.html).

The output from our code will have a similar shape as the one above.


## Libraries used
- `math`
- `numpy`
- `plotly.graph_objects`
- `matplotlib.pyplot`
- `random`
- `time`

## Project Structure
- `code`: Contains the Python code we wrote to find the landmarks using Sequential MaxMin and draw the genus 5 surface.
- `plot`: Stores the html page for the interactive plot and the landmarks graph.
- `slide`: The PowerPoint we used in our presntation which contains more detailed information and elegant graphs.
- `README.md`: You are here.
- `index.html`: Detailed information on analyzing the 'shape' of genus 5 surface equation using Lazy Witness Complex.
