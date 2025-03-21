from libqtile import bar, widget
from libqtile.config import Screen

# 🎨 Cores Gruvbox
colors = {
    "bg": "#282828",  # Fundo
    "fg": "#ebdbb2",  # Texto principal
    "yellow": "#fabd2f",
    "orange": "#fe8019",
    "red": "#fb4934",
    "green": "#b8bb26",
    "blue": "#83a598"
}

def my_bar():
    return bar.Bar(
        [
            widget.GroupBox(
                fontsize = 12,
                font = "Hack",
                highlight_method="block",
                this_current_screen_border=colors["yellow"],
                inactive=colors["fg"],
                rounded=False,
                padding=4,
            ),
            widget.Prompt(),
            widget.Spacer(),
            widget.Systray(icon_size = 16),
            widget.Clock(
                fontsize = 14,
                font = "Hack",
                format=" %H:%M",
                foreground=colors["orange"],
            ),
                
        ],
        32,  # Altura da barra
        background=colors["bg"],
        opacity=0.95,
    )

screens = [Screen(top=my_bar())]

