import wiitools
print("font")

_TEMP_SURF = "font_surf_temp"

class ft:
    def __init__(self, s, data):
        self.size = s
        self.font = data

    def render(self, text: str, antialias: bool, color):
        wiitools.surface_new(_TEMP_SURF,
                             wiitools.text_length(text, self.size),
                             self.size * 8)
        wiitools.surface_set_target(_TEMP_SURF)
        wiitools.render_text(0, 0, text, self.size, 0,
                             (color[0], color[1], color[2], 255), 0.0)
        wiitools.surface_clear_target()
        return _TEMP_SURF

def Font(font, size: int):
    return ft(size, font)

print("font end")
