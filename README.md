# Analyzing-the-Shape-of-Data--Persistent-Homology
**Mentor:** Dr. Zhixu Su  
**TA:** Chengyuan Ma  
**Undergraduate students:** Caroline Ding, Zongze Li

This is a project from UW WXML Autumn 2022. We used techniques from topology to understand the 'shape' of data set. Persistent homology detects topological features of the complexes that persist over a range of scales, it computes the numbers of connected components, 1-dimensional holes (loops), 2-dimensional holes (voids), etc, and keeps track of the birth and death scale of the features.

In this project, we computed the persistent homology of genus 5 surface by applying the lazy witness complex.

## What is the Lazy Witness Complex?
Given a finite set of point $S$ in $\mathbb{R}^d$,
