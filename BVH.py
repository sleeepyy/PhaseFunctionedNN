import numpy as np
from hyperparams import *


class BVH:
    def load(self, filepath):
        with open(filepath) as f:
            lines = f.readlines()
        motion_index = lines.index('MOTION\n')
        motion_str = lines[motion_index+3:]
        self.meta_info = ''.join(lines[:motion_index])
        self.frames = int(lines[motion_index+1].split(':')[1])
        self.frame_time = lines[motion_index+2]
        self.motion = [[float(x) for x in line.split()] for line in motion_str]

    def save(self, filepath, motion=None):
        if motion is None:
            motion = self.motion
        with open(filepath, 'w') as f:
            f.write(self.meta_info)
            f.write('MOTION\n')
            f.write('Frames: {}\n'.format(len(motion)))
            f.write(self.frame_time)
            for m in motion:
                f.write(' '.join(str(x) for x in m)+'\n')

    @property
    def motions(self):
        return np.asarray(self.motion, dtype=np.float32)

    @property
    def motion_angles(self):
        return self.motions[:, abandon_items:]

    @property
    def num_of_angles(self):
        return self.motions.shape[1]-abandon_items

    @property
    def length(self):
        return self.motions.shape[0]
