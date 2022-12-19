code/lazy_witness_complex.py
#  itertools
import math
import numpy as np
import plotly.graph_objects as go
# import plotly.express as px
import random
import time


def choose_landmarks(points, num_landmarks):
    """
    Choose landmarks from the data points using sequeential maxmin method.
    Returns a list of landmarks.
    """
    selected, not_selected, min_distance = [], points.copy(), []
    start_idx = random.randint(0, len(points)-1)
    selected.append(not_selected[start_idx])
    not_selected.pop(start_idx)

    for p in not_selected:
        min_distance.append(math.dist(selected[0], p))

    while len(selected) < num_landmarks:
        # get the index of the marimum value in the min_distance list
        added_idx = min_distance.index(max(min_distance))
        selected.append(not_selected[added_idx])
        not_selected.pop(added_idx)
        min_distance.pop(added_idx)
        for i in range(len(min_distance)):
            min_distance[i] = \
                min(min_distance[i], math.dist(not_selected[i], selected[-1]))
    return selected


def nu_distance(p, landmarks, nu):
    """
    Calculate the distance from p to the nu-th closest landmark point.
    """
    if nu > 0:
        nu_min_distance = []
        for q in landmarks:
            nu_min_distance.append(math.dist(p, q))
        nu_min_distance.sort()
        return nu_min_distance[nu-1]
    else:
        return 0


def drawLazyWitness(points, num_landmarks, nu, t):

    landmarks = choose_landmarks(points, num_landmarks)
    edge_matrix = np.zeros([len(landmarks), len(landmarks)])

    for i in range(len(points)):
        m_z = nu_distance(points[i], landmarks, nu)
        for j in range(len(landmarks)-1):
            for k in range(1, len(landmarks)-j):
                max_distance = max(math.dist(points[i], landmarks[j]),
                                   math.dist(points[i], landmarks[j+k]))
                if max_distance <= t + m_z:
                    edge_matrix[j, j+k] = 1

    traces = []

    x, y, z = \
        [p[0] for p in points], [p[1] for p in points], [p[2] for p in points]
    traces.append(go.Scatter3d(x=x, y=y, z=z, mode='markers',
                  marker_color='#B6B1A9', marker_size=7))

    x, y, z = [p[0] for p in landmarks], [p[1] for p in landmarks], [p[2] for p in landmarks]
    traces.append(go.Scatter3d(x=x, y=y, z=z, mode='markers', marker_color='#8B1C62'))

    pairs = [[idx1, idx2] for idx1 in range(len(landmarks)) for idx2 in range(len(landmarks))]
    triples = [[idx1, idx2, idx3] for idx1 in range(len(landmarks)) for idx2 in range(len(landmarks)) for idx3 in range(len(landmarks))]

    for pair in pairs:
        if edge_matrix[pair[0], pair[1]] == 1:
            x = [landmarks[pair[0]][0], landmarks[pair[1]][0]]
            y = [landmarks[pair[0]][1], landmarks[pair[1]][1]]
            z = [landmarks[pair[0]][2], landmarks[pair[1]][2]]
            traces.append(go.Scatter3d(x=x, y=y, z=z, mode='lines', line_width=8, line_color='#5D478B'))

    for triple in triples:
        if edge_matrix[triple[0], triple[1]] == 1 and edge_matrix[triple[0], triple[2]] == 1 and edge_matrix[triple[1], triple[2]] == 1:
            x = [landmarks[triple[0]][0], landmarks[triple[1]][0], landmarks[triple[2]][0]]
            y = [landmarks[triple[0]][1], landmarks[triple[1]][1], landmarks[triple[2]][1]]
            z = [landmarks[triple[0]][2], landmarks[triple[1]][2], landmarks[triple[2]][2]]
            traces.append(go.Mesh3d(x=x, y=y, z=z, color='#8968CD', opacity=0.8, showscale=True))

    layout = go.Layout(title='', showlegend=False,
                       scene=dict(xaxis=dict(backgroundcolor='white',
                                             color='white',
                                             gridcolor='white'),
                                  yaxis=dict(backgroundcolor='white',
                                             color='white',
                                             gridcolor='white'),
                                  zaxis=dict(backgroundcolor='white',
                                             color='white',
                                             gridcolor='white')
                                  ))

    fig = go.Figure(data=traces, layout=layout)

    fig.show()


def genG5Surface(num, noise):

    points = []

    while len(points) < num:
        x = 2*(2*np.random.uniform(0, 1)-1)
        y = 2*(2*np.random.uniform(0, 1)-1)
        z = 2*(2*np.random.uniform(0, 1)-1)
        if abs(4.5+10*(x**4+y**4+z**4)-10*(x**2+y**2+z**2)) < noise:
            points.append([x, y, z])

    return points


points = genG5Surface(3000, 0.01)
t0 = time.time()
drawLazyWitness(points, 150, 1, 0.05)
t1 = time.time()
print(t1-t0)
