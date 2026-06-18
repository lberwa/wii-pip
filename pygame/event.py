import wiitools
import data as d
print("event")
# Wiimote → pygame Mapping:
#   WPAD_BUTTON_UP    → KEYDOWN/KEYUP  K_UP  + K_w
#   WPAD_BUTTON_DOWN  → KEYDOWN/KEYUP  K_DOWN + K_s
#   WPAD_BUTTON_LEFT  → KEYDOWN/KEYUP  K_LEFT + K_a
#   WPAD_BUTTON_RIGHT → KEYDOWN/KEYUP  K_RIGHT + K_d
#   (alle 4 Kanäle, je zwei Events pro Tastendruck)
#   WPAD_BUTTON_A     → MOUSEBUTTONDOWN/UP  button=BUTTON_LEFT
#   WPAD_BUTTON_B     → MOUSEBUTTONDOWN/UP  button=BUTTON_RIGHT
#   WPAD_BUTTON_HOME  → KEYDOWN/KEYUP  K_ESCAPE
#   Alles andere      → kein Event

def have_keyboard():
    return False


class Event:
    def __init__(self, type, **kwargs):
        self.type = type
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __repr__(self):
        attrs = {k: v for k, v in vars(self).items() if k != 'type'}
        return f"<Event type={self.type} {attrs}>"


# (wpad_attr, arrow_key, wasd_key)
_DPAD_MAP = [
    ('WPAD_BUTTON_UP',    d.K_UP,    d.K_w),
    ('WPAD_BUTTON_DOWN',  d.K_DOWN,  d.K_s),
    ('WPAD_BUTTON_LEFT',  d.K_LEFT,  d.K_a),
    ('WPAD_BUTTON_RIGHT', d.K_RIGHT, d.K_d),
]


def get():
    wiitools.WPAD_ScanPads()
    events = []

    for chan in range(4):
        dn = wiitools.WPAD_ButtonsDown_all(chan)
        up = wiitools.WPAD_ButtonsUp_all(chan)

        for attr, arrow, wasd in _DPAD_MAP:
            if getattr(dn, attr, False):
                events.append(Event(d.KEYDOWN, key=arrow, mod=0, unicode=''))
                events.append(Event(d.KEYDOWN, key=wasd,  mod=0, unicode=''))
            if getattr(up, attr, False):
                events.append(Event(d.KEYUP,   key=arrow, mod=0, unicode=''))
                events.append(Event(d.KEYUP,   key=wasd,  mod=0, unicode=''))

        if getattr(dn, 'WPAD_BUTTON_A', False):
            events.append(Event(d.MOUSEBUTTONDOWN, button=d.BUTTON_LEFT,  pos=(0, 0)))
        if getattr(up, 'WPAD_BUTTON_A', False):
            events.append(Event(d.MOUSEBUTTONUP,   button=d.BUTTON_LEFT,  pos=(0, 0)))

        if getattr(dn, 'WPAD_BUTTON_B', False):
            events.append(Event(d.MOUSEBUTTONDOWN, button=d.BUTTON_RIGHT, pos=(0, 0)))
        if getattr(up, 'WPAD_BUTTON_B', False):
            events.append(Event(d.MOUSEBUTTONUP,   button=d.BUTTON_RIGHT, pos=(0, 0)))

        if getattr(dn, 'WPAD_BUTTON_HOME', False):
            events.append(Event(d.KEYDOWN, key=d.K_ESCAPE, mod=0, unicode='\x1b'))
        if getattr(up, 'WPAD_BUTTON_HOME', False):
            events.append(Event(d.KEYUP,   key=d.K_ESCAPE, mod=0, unicode='\x1b'))

    return events


def pump():
    wiitools.WPAD_ScanPads()
print("event end")