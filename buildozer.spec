[app]
title = Painel Discord
package.name = paineldiscord
package.domain = org.seunome

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

# Dependencias: kivy para a interface, discord.py + aiohttp para o bot
requirements = python3,kivy,discord.py,aiohttp,certifi,charset-normalizer,idna,multidict,yarl,attrs,frozenlist,aiosignal,pillow

orientation = portrait
fullscreen = 0

# Permissao de internet e necessaria pro bot conectar no Discord
android.permissions = INTERNET

android.api = 33
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
