from typing import Generator
from numpy._typing import NDArray

from particle import Particle
from constants import SUN_MASS, EARTH_MASS, AU, TICK

import numpy as np
import matplotlib.pyplot as plt


def simulate(particles: list[Particle], timestep: float) -> Generator[tuple[list[Particle], float], None, None]: 
    time: float = 0
    while True:
        for particle in particles:
            particle.update_position(particles, timestep)
        yield (particles, time)
        time += timestep

def coords(particles: list[Particle]) -> tuple[NDArray[np.float64], NDArray[np.float64]]:
    n = len(particles)
    x = np.zeros(n)
    y =  np.zeros(n)
    for i in range(n):
        particle = particles[i]
        x[i] = particle.x
        y[i] = particle.y
    return (x, y)
        
def live_plot_particle_sim(simulation: Generator[tuple[list[Particle], float], None, None]) -> None:    
    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    (particles, time) = next(simulation)
    plt.title(f'time: {time} secs')
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    (x, y) = coords(particles)
    points, = ax.plot(x, y, 'o')

    while True:
        try:
            (particles, time) = next(simulation)
        except StopIteration:
            break
        else:
            (x, y) = coords(particles)
            points.set_xdata(x)
            points.set_ydata(y)
            fig.canvas.draw()
            fig.canvas.flush_events()
            plt.title(f'time: {time} secs')
            plt.pause(1)

def main() -> None:
    sun = Particle(SUN_MASS, 0, 0, 0, 0)
    earth = Particle(EARTH_MASS, 2, 2, 1, 1)
    particles: list[Particle] = [sun, earth]
        
    tick = TICK

    simulation = simulate(particles, tick)

    live_plot_particle_sim(simulation)


if __name__ == "__main__":
    main()
