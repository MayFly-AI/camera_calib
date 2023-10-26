# Simple OpenCV camera calibration with chess pattern

Stream data from sensorleap sensor and record images for calibration (using the space key):
```bash
python record.py
```

This creates a folder ./outputs which contains PNG images.

To estimate intrinsic camera parameters, run
```bash
python calib.py --folder ./outputs
```



