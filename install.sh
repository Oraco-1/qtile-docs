#!/bin/bash

# Lista de programas para instalar
packages=(
    firefox
    neovim
    zsh
    alacritty
    nerd-fonts
    ttf-hack
    nitrogen
    steam
    discord
    ncspot
)

# Atualiza o sistema e instala os pacotes
paru -Syu --needed --noconfirm "${packages[@]}"
