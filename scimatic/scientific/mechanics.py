from math import sqrt, cos

def impulse(
    force: int | float,
    initial_time: int | float,
    final_time: int | float,
    print_result: bool = False,
    return_deltat: bool = False
) -> tuple[int | float, int | float] | int | float:
    if initial_time >= final_time:
        raise ValueError

    delta_t = final_time - initial_time

    J = force * delta_t

    delta = '\u0394'

    if print_result:
        if not return_deltat:
            print(f'Impulse: {J}N•s')
        else:
            print(f'Impulse: {J}N•s, {delta}t: {delta_t}s')

    if return_deltat:
        return J, delta_t
    else:
        return J


class Mechanics:
    def __init__(self, mass: float):
        self.mass = mass

    def momentum(
        self,
        velocity: int | float,
        print_result: bool = False
    ) -> int | float | None:
        p = self.mass * velocity

        if print_result:
            print(f'Momentum: {p}kg•m/s')
        return p

    def kinetic_energy(
            self,
            velocity: int | float,
            print_result: bool = False
    ) -> int | float:
        output = 1 / 2 * self.mass * velocity**2

        if print_result:
            print(f'Kinetic Energy: {output}J')
        return output
    def potential_energy(
            self,
            h: int | float,
            gravity: int | float = 9.80665,
            print_result: bool = False
    ) -> int | float:
        output = self.mass * gravity * h

        if print_result:
            print(f'Potential Energy: {output}J')
        return output

    def force(
            self,
            acceleration: int | float,
            print_result: bool = False
    ) -> int | float:
        output = self.mass * acceleration

        if print_result:
            print(f'Force: {output}N')
        return output

    def mass_energy(
        self,
        print_result: bool = False
    ) -> int | float:

        output = self.mass * 299_792_458**2

        if print_result:
            print(f'Energy: {output}J')
        return output

    def KE_velocity(
            self,
            KE: int | float,
            print_result: bool = False
    ) -> int | float:

        output = sqrt(2 * KE / self.mass)
        if print_result:
            print(f'Velocity: {output}m/s')
        return output

    def weight(
        self,
        gravity: int | float = 9.80665,
        print_result: bool = False
    ) -> int | float:

        output = self.mass * gravity

        if print_result:
            print(f'Weight: {output}N')
        return output

    def grav_force(
        self,
        obj_mass: int | float,
        r: int | float,
        print_result: bool = False
    ) -> int | float:

        G = 6.67430 * 10**-11

        output = G * (self.mass * obj_mass) / r**2
        if print_result:
            print(f'Gravitational Force: {output}N')
        return output

def work(
    force: int | float,
    displacement: int | float,
    angle: int | float = 0.0,
    print_result: bool = False
) -> int | float:
    if angle == 0:
        W = force * displacement
    else:
        W = force * displacement * cos(angle)

    if print_result:
        print(f'Work: {W}J')
    return W