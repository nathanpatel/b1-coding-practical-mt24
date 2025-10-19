# demo_closedloop.py
# Run from repo root:  python -m uuv_mission.demo_closedloop

from .dynamic import Submarine, ClosedLoop, Mission
from .control import PDController
from pathlib import Path

def main():
    # 1) Load mission
    mission = Mission.from_csv("data/mission.csv")
    print(f"[demo_closedloop] loaded mission with {len(mission.reference)} steps")

    # 2) Plant + controller
    plant = Submarine()
    ctrl = PDController(kp=0.15, kd=0.6)

    # 3) Close the loop and run with some randomness
    sim = ClosedLoop(plant, ctrl)
    traj = sim.simulate_with_random_disturbances(mission, variance=0.5)

    print("[demo_closedloop] simulation finished")

    # 4) Plot result; also save a PNG so CI/headless runs have an artifact
    import matplotlib.pyplot as plt
    traj.plot_completed_mission(mission)
    out_dir = Path("outputs"); out_dir.mkdir(exist_ok=True)
    out_path = out_dir / "closedloop_demo.png"
    plt.savefig(out_path, dpi=150, bbox_inches="tight")
    print(f"[demo_closedloop] saved plot to {out_path}")

if __name__ == "__main__":
    main()
