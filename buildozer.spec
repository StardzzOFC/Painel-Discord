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
#
# IMPORTANTE sobre aiohttp/multidict/yarl/frozenlist/attrs/aiosignal:
# discord.py==2.4.0 so exige "aiohttp>=3.7.4,<4", entao sem fixar o resto da
# cadeia o pip pega o aiohttp mais novo -> que a partir da 3.10 depende do
# pacote "propcache" (extensao em C/Rust sem fallback puro-Python coberto
# pelas flags *_NO_EXTENSIONS do workflow). Isso quebra a compilacao pra
# Android e faz o pip tentar TODAS as versoes do discord.py em busca de uma
# combinacao que funcione, terminando em "ResolutionImpossible".
# Fixando toda a cadeia numa combinacao compativel e anterior ao propcache,
# o pip resolve direto (uma unica versao por pacote, sem precisar procurar).
requirements = python3==3.11.9,hostpython3==3.11.9,kivy==2.3.0,pillow,attrs==23.2.0,aiosignal==1.3.1,frozenlist==1.4.1,multidict==6.0.5,yarl==1.9.4,aiohttp==3.9.5,discord.py==2.4.0

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
