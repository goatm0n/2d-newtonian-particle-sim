from typing import Generator
from numpy._typing import NDArray

from particle import Particle
from constants import JUPITER_MASS, SUN_MASS, G, EARTH_MASS, AU, TICK

import numpy as np
import matplotlib.pyplot as plt
import math


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

def velocities(particles: list[Particle]) -> tuple[NDArray[np.float64], NDArray[np.float64]]:
    n = len(particles)
    x_vel = np.zeros(n)
    y_vel = np.zeros(n)
    for i in range(n):
        particle = particles[i]
        x_vel[i] = particle.x
        y_vel[i] = particle.y
    return (x_vel, y_vel)
        
def live_plot_particle_sim(simulation: Generator[tuple[list[Particle], float], None, None]) -> None:    
    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    (particles, time) = next(simulation)
    plt.title(f'time: {time} secs')
    ax.set_xlim([-7*AU, 7*AU])
    ax.set_ylim([-7*AU, 7*AU])
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

def circular_orbit_speed(distance, mass) -> float:
    return math.sqrt(G*mass/distance)

def main() -> None:
    sun = Particle(SUN_MASS, 0, 0, 0, 0)
    earth_initial_speed = circular_orbit_speed(AU, SUN_MASS)
    earth = Particle(EARTH_MASS, 0, AU, earth_initial_speed, 0)
    jupiter_initial_speed = circular_orbit_speed(5.2*AU, SUN_MASS)
    jupiter = Particle(JUPITER_MASS, 0, 5.2*AU, jupiter_initial_speed, 0)
    particles: list[Particle] = [sun, earth, jupiter]
            
    tick = TICK

    simulation = simulate(particles, tick)

    live_plot_particle_sim(simulation)


if __name__ == "__main__":
    main()
