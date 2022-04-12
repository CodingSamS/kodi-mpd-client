#/bin/sh
# do NOT use this script from XBMC addons directory, it is intented for development only
DESTINATION_DIR=~/.kodi/addons/plugin.audio.mpdclient

rm -rf ${DESTINATION_DIR}
mkdir -p ${DESTINATION_DIR}
cp -a * ${DESTINATION_DIR}
