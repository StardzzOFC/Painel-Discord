[app]
title = Painel Discord
package.name = paineldiscord
package.domain = org.seunome

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

# python3==3.11.9 fixa a versao do Python usada DENTRO do app Android -
# versoes mais novas (3.13/3.14) ainda tem incompatibilidades com o Kivy.
# hostpython3 precisa ser a MESMA versao (regra do proprio python-for-android)
# Nao fixamos mais aiohttp/multidict/yarl/frozenlist - o discord.py escolhe
# sozinho versoes compativeis (fixar todas juntas estava gerando conflito)
requirements = python3==3.11.9,hostpython3==3.11.9,kivy==2.3.0,discord.py==2.4.0,pillow

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
