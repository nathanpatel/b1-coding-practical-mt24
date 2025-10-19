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