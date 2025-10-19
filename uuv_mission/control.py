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
        PD update with explicit variable names for clarity.
        - proportional_term reacts to *how wrong we are right now*
        - derivative_term reacts to *how fast the error is changing*

        Discrete PD law (unit sample time):
            u[t] = Kp * e[t] + Kd * (e[t] - e[t-1])

        Args:
            e_t: current error (reference - measured)
        Returns:
            Control action u_t (float)
        """

        previous_error = self.prev_e          # e[t-1]
        current_error  = e_t                  # e[t]

        change_in_error = current_error - previous_error  # Δe
        proportional_term = self.kp * current_error
        derivative_term   = self.kd * change_in_error

        u_t = proportional_term + derivative_term

        # Remember current error for the next call
        self.prev_e = current_error
        return u_t