import subprocess

def run(cmd):
    """Executa um comando em segundo plano"""
    subprocess.Popen(cmd, shell=True)

def autostart():
    """Lista os programas"""
    run("xrandr --output HDMI-1 --primary --mode 1920x1080 --pos 0x0 --output LVDS-1 --off")  # Configuração dos monitores
    run("picom")  # Compositor para transparências e suavização
    run("nitrogen --restore")  # Restaurar papel de parede

