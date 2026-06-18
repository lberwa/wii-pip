import wiitools

print("display")

real_width   = 802
real_height  = 640

local_width  = real_width
local_height = real_height

class surface:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def fill(self, rgb):
        wiitools.draw_rect(0, 0, local_width, local_height,
                           (rgb[0], rgb[1], rgb[2], 255),
                           0.0)
        
    def blit(self, tex_id, pos):
        wiitools.blit(tex_id, pos[0], pos[1])


def set_mode(w_h): 
    global local_width, local_height
    local_width = w_h[0]
    local_height = w_h[1]
    wiitools.set_screen_size(w_h[0], w_h[1])
    return surface(w_h[0], w_h[1])


def update():
    wiitools.render_update()
print("display end")