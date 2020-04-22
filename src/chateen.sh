#!/usr/bin/env bash
# run chateen
# wykys 2018

SCRIPTS_DIR=.scripts

if [ ! -d ".venv" ]; then
    ./venv.sh
fi

#. .venv/bin/activate
export QT_QPA_PLATFORMTHEME=gtk3
pyside2-uic chateen.ui -o template_main_win.py
./mockup.py