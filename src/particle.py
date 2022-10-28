import math
from ssl import VERIFY_ALLOW_PROXY_CERTS 
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
    """

    def __init__(self, mass: float, x: float, y: float, vel_x: float, vel_y: float) -> None:
        self.mass = mass
        self.x = x 
        self.y = y
        self.vel_x = vel_x 
        self.vel_y = vel_y
        
    def distance(self, particle: 'Particle') -> float:
        x_diff = self.x - particle.x
        y_diff = self.y - particle.y
        return math.sqrt(x_diff**2 + y_diff**2)

    def orbital_speed(self, particle: 'Particle') -> float:
        return math.sqrt(G * particle.mass / self.distance(particle))
    
    def orbital_circumference(self, particle: 'Particle') -> float:
        return 2 * math.pi * self.distance(particle)

    def orbital_period(self, particle: 'Particle') -> float:
        return self.orbital_circumference(particle) / self.orbital_speed(particle) 
    
    def gravitational_force(self, particle: 'Particle') -> float:
        r = self.distance(particle)
        return G * self.mass * particle.mass * math.pow(r, -2) 






