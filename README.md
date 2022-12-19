# Analyzing-the-Shape-of-Data--Persistent-Homology
**Mentor:** Dr. Zhixu Su  
**TA:** Chengyuan Ma  
**Undergraduate students:** Caroline Ding, Zongze Li

This is a project from UW WXML Autumn 2022. We used techniques from topology to understand the 'shape' of data set. Persistent homology detects topological features of the complexes that persist over a range of scales, it computes the numbers of connected components, 1-dimensional holes (loops), 2-dimensional holes (voids), etc, and keeps track of the birth and death scale of the features.

In this project, we computed the persistent homology of genus 5 surface by applying the lazy witness complex.

## What is the Lazy Witness Complex?
Given a finite set of point $S$ in $\mathbb{R}^d$ with the landmark subset $L$. At each filtration value $t$, two landmarks $\ell_i$ and $\ell_j$ are connected by 1-simplex if there exists a witness point $w$ such that:
$$\max \left{ d(\ell_i, w), d(\ell_j, w) \right} \leq t + \nu(w)$$
Where $\nu(w)$ is the distance between $w$ and its nearest landmark point. Three landmarks are connected by 2-simplex if every pair has been connected.
