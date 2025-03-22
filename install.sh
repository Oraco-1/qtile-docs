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
    # Adicione mais programas aqui
)

# Atualiza o sistema e instala os pacotes
paru -Syu --needed --noconfirm "${packages[@]}"
