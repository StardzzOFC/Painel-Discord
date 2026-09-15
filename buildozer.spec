[app]
title = Painel Discord
package.name = paineldiscord
package.domain = org.seunome

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

# Dependencias: kivy para a interface, discord.py + aiohttp para o bot
# (versoes fixadas - combinacao testada, evita pegar versao mais nova
# que pode ter incompatibilidade com o ambiente de compilacao do Android)
# python3==3.11 fixa a versao do Python usada DENTRO do app Android -
# versoes mais novas (3.13/3.14) ainda tem incompatibilidades com o Kivy
requirements = python3==3.11,kivy==2.3.0,discord.py==2.4.0,aiohttp==3.10.10,certifi,charset-normalizer,idna,multidict==6.1.0,yarl==1.15.2,attrs,frozenlist==1.4.1,aiosignal,pillow

orientation = portrait
fullscreen = 0

# Permissao de internet e necessaria pro bot conectar no Discord
android.permissions = INTERNET

android.api = 33
android.minapi = 24
android.ndk = 25b
# So arm64-v8a (cobre praticamente todo celular Android de 2018 pra ca) -
# compilar pra menos arquiteturas = build mais rapido e com menos chance de erro
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
