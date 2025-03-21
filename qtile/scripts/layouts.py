from libqtile import layout

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

layouts = [
    layout.MonadTall(
        border_focus=colors["yellow"],
        border_normal=colors["bg"],
        border_width=4,
        margin=6,
    ),
    
    layout.MonadWide(
        border_focus=colors["orange"],
        border_normal=colors["bg"],
        border_width=4,
        margin=6,
    ),
    layout.Max(),
]

floating_layout = layout.Floating(
    border_focus="#fabd2f",  # Cor para a borda de foco (no estilo Gruvbox)
    border_normal="#282828",  # Cor para a borda normal
    border_width=2,  # Espessura da borda
)

