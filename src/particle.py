import math
from constants import G


class Particle:
    """
    Class to represent 2-d particles in newtonian physics
    Particles are represented as points with mass

    ...

    Attributes
    ----------
    mass: float
        mass of body, kg 
    x: float 
        meters from origin in x-direction
    y: float
        meters from origin in y-direction
    vel_x: float
        velocity in x-direction, m/s 
    vel_y: float
        velocity in y-direction, m/s
    
    Methods
    -------
    distance: float
        returns distance between self and another particle, meters
    orbital_speed: float
        returns magnitude of velocity of particle in orbit around more massive particle, m/s  
    orbital_circumference: float
        returns length of 1 orbit around more massive particle, meteres
    orbital_period: float
        returns time to complete 1 orbit of more massive particle, seconds
    gravitational_attraction: float
        returns force of attraction due to gravity between 2 particles, N, kgms^-2
    """

    def __init__(self, mass: float, x: float, y: float, vel_x: float, vel_y: float)-> None:
        self.mass = mass
        self.x = x 
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        
    def x_distance(self, particle: 'Particle') -> float:
        return abs(self.x - particle.x)

    def y_distance(self, particle: 'Particle') -> float:
        return abs(self.y - particle.y)

    def distance(self, particle: 'Particle') -> float:
        return math.sqrt(self.x_distance(particle)**2 + self.y_distance(particle)**2)

    def orbital_speed(self, particle: 'Particle') -> float:
        return math.sqrt(G * particle.mass / self.distance(particle))
    
    def orbital_circumference(self, particle: 'Particle') -> float:
        return 2 * math.pi * self.distance(particle)

    def orbital_period(self, particle: 'Particle') -> float:
        return self.orbital_circumference(particle) / self.orbital_speed(particle) 
    
    def gravitational_attraction(self, particle: 'Particle') -> tuple[float, float]:
        r = self.distance(particle)
        theta = math.atan2(self.y_distance(particle), self.x_distance(particle))
        # this line crashes if there is a collision, ie, if r==0
        force = G * self.mass * particle.mass * r**-2
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return (force_x, force_y)

    def sum_gravitational_forces(self, particles: list['Particle']) -> tuple[float, float]:
        total_fx: float = 0
        total_fy: float = 0
        for particle in particles:
            if self == particle:
                continue
            (fx, fy) = self.gravitational_attraction(particle)
            total_fx += fx
            total_fy += fy 
        return (total_fx, total_fy)

    def sum_forces(self, particles: list['Particle']) -> tuple[float, float]:
        (total_fx, total_fy) = self.sum_gravitational_forces(particles)
        return (total_fx, total_fy)

    def acceleration(self, particles: list['Particle']) -> tuple[float, float]:
        (total_fx, total_fy) = self.sum_forces(particles)
        ax = total_fx / self.mass
        ay = total_fy / self.mass
        return (ax, ay)

    def update_velocity(self, particles: list['Particle'], timestep: float) -> None:
        (ax, ay) = self.acceleration(particles)
        self.vel_x += ax * timestep
        self.vel_y += ay * timestep

    def update_position(self, particles: list['Particle'], timestep: float) -> None:
        self.update_velocity(particles, timestep)
        self.x += self.vel_x * timestep
        self.y += self.vel_y * timestep






