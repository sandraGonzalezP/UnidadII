def gravitational_force(G: float, M: float, m: float, r: float) -> float:
    force = G * (M * m / (r * r))
    return force


"""This function calculate gravitational force"""
