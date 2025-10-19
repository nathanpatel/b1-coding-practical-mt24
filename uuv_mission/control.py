# control.py

# PD controller per task (defaults: Kp = 0.15, Kd = 0.6)
class PDController:
    def __init__(self, kp: float = 0.15, kd: float = 0.6):
        self.kp = kp
        self.kd = kd
        self.prev_e = 0.0  # remember e[t-1]

    # to clear previous error
    def reset(self):
        self.prev_e = 0.0