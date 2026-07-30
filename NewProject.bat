@echo off
title Create Project Folders
set /p client=Client Name:
set /p project=Project Name:
set directory=D:\00_Work

md "%directory%\%client%\%project%\Assets\From Client"
md "%directory%\%client%\%project%\Assets\REF"
md "%directory%\%client%\%project%\3D\3D_Anim"
md "%directory%\%client%\%project%\3D\3D_Render"
md "%directory%\%client%\%project%\3D\C4D"
md "%directory%\%client%\%project%\3D\FBX"
md "%directory%\%client%\%project%\3D\CAD"
md "%directory%\%client%\%project%\3D\HOU"
md "%directory%\%client%\%project%\3D\SBS"
md "%directory%\%client%\%project%\Dailies"
md "%directory%\%client%\%project%\Deliverables"
md "%directory%\%client%\%project%\00_Doc"

start "" "%directory%\%client%\%project%"