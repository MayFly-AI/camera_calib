import numpy as np
import cv2
from pathlib import Path

from mayfly.sensorcapture import SensorCapture

def record(out_dir):
    cap = SensorCapture(list(range(64)), '')
    frame_idx = -1
    count = 0
    while True:
        capture = cap.read()
        if capture['type'] != 'camera':
            continue
        frame_idx += 1
        frm = capture['frames'][0] # It may have more than 1 frame if sync cameras or ToF. We assume 1 frame
        # arr is RGBA
        arr = np.from_dlpack(frm['image']).copy()
        bgr = cv2.cvtColor(arr[:,:,:3], cv2.COLOR_RGB2BGR)

        cv2.imshow('image',bgr)
        k = cv2.waitKey(1)
        if k == 32: # space
            img_path = out_dir+'/image_%06d.png'%count
            count += 1
            cv2.imwrite(img_path,bgr)
            print('Saved image ',img_path)
            save_image = False

if __name__ == "__main__":
    print('Press Enter to save image')
    out_dir = './outputs'
    Path(out_dir).mkdir(parents=False, exist_ok=True)
    record(out_dir)


