#! /bin/bash

in=`pwd`/Inputs/`cut -d. -f1 ${WCC_SCRIPTS_PATH}/share/sourcename`
echo ${in}
vim  ${in}
