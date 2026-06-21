_active_tweens = []

class TweenRequest:
    def __init__(self, target, property, start, end, duration):
        self.target = target
        self.property = property
        self.start = start
        self.end = end
        self.duration = duration
        self.elapsed = 0.0

def to(**kwargs):
    target = kwargs.pop('target', None)
    property = kwargs.pop('property', None)
    start = getattr(target, property)
    end = kwargs.pop('end', None)
    duration = kwargs.pop('duration', None)

    request = TweenRequest(target, property, start, end, duration)
    _active_tweens.append(request)

def _updateAll(dt):
    global _active_tweens

    for i in range(len(_active_tweens) - 1, -1, -1):
        t = _active_tweens[i]
        
        progress = min(t.elapsed / t.duration, 1.0)
        if progress >= 1.0:
            _active_tweens.pop(i)
            continue

        t.elapsed += dt

        c_val = t.start + (t.end - t.start) * progress
        setattr(t.target, t.property, c_val)
