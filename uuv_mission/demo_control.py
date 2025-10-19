# demo_control.py
# Run with: python -m YOURPKG.demo_control  (from the repo root)

from .control import PDController

def main():
    
    print("[demo_control] starting…")  # debug

    ctrl = PDController(kp=0.15, kd=0.6)
    ctrl.reset()  # start fresh

    # Try a small sequence of errors to see proportional + derivative effect.
    test_errors = [0.0, 1.0, 0.5, 0.5, -0.5, -0.5, 0.0]
    for e in test_errors:
        u = ctrl.step(e)
        print(f"error={e:6.2f}  ->  control u={u:7.3f}")

if __name__ == "__main__":
    main()