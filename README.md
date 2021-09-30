# soulstorm
Asset Decoder for Warhammer: Dawn of War - Soulstorm (requires .whm to .x converter first)

![screenshot1](https://github.com/TheMindVirus/soulstorm/blob/main/screenshot1.png)

# Explanation
The Asset files for Soulstorm are illegible to both humans and machines. \
EBP files are non-existent in the Steam distribution of Soulstorm. \
The .ebp gets compiled to .whe and the .sgm gets compiled to .whm - this has the geometry data. \
Other data includes stats and animation which can be extracted using DoW ModTools v1. \
This is all compressed inside a .sga archive which is like a .jar file \
that 7-zip doesn't know how to open.

![screenshot2](https://github.com/TheMindVirus/soulstorm/blob/main/screenshot2.png)

My scripts need to be used with DoW_Modtools_setup_v1 \
and mudflaps-whm-to-x-converter from Mudflaps_whm_and_whe_Tools_2008_III \
to extract it from the .sga archive in the first place, so: \
ModStudio.exe -> DoW:SS Mod -> DXP2.module (English) \
-> Data/art/ebps/races/dark_eldar/structures/kabal_fortress.whm \
-> Right Click, Extract File \
.whm -> mudflaps-whm-to-x-converter -> .x \
.x -> x2obj.py -> .obj \
Windows, Blender and Unity can then start to recognise the assets straight away \
so you can include the assets in e.g. Tabletop Simulator. \
The assets are now also human readable which makes it easier to port \
in newer versions of the omniverse.

![screenshot3](https://github.com/TheMindVirus/soulstorm/blob/main/screenshot3.png)
