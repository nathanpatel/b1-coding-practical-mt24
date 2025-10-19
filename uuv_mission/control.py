# control.py
# Simple PD controller used by the cave mission simulation.
# PD = Proportional + Derivative. We store the previous error to estimate the derivative term.

class PDController:
    def __init__(self, kp: float = 0.15, kd: float = 0.6):
        
        """
        Args:
            kp: Proportional gain (how strongly we react to current error)
            kd: Derivative gain (how strongly we react to change in error)
        """
        self.kp = kp
        self.kd = kd
        
        # Store previous error e[t-1] so we can compute the derivative term.
        self.prev_e = 0.0 

    # Clear controller memory (previous error). Call before a new run.
    def reset(self):
        self.prev_e = 0.0

    def step(self, e_t: float) -> float:
        """
        Compute the control action for the current error.

        Discrete PD law (unit sample time):
            u[t] = Kp * e[t] + Kd * (e[t] - e[t-1])

        Args:
            e_t: current error (reference - measured)
        Returns:
            Control action u_t (float)
        """

        # Estimate the derivative by error difference (Δe = e[t] - e[t-1]).
        de = e_t - self.prev_e

        # PD control output
        u_t = self.kp * e_t + self.kd * de

        # Update memory for next call
        self.prev_e = e_t
        
        return u_t