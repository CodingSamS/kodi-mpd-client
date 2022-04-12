from pathlib import Path


import xbmc
import xbmcaddon


import resources.musicpd


class KodiAddon:

    def __init__(self):
        self.xbmc_addon = xbmcaddon.Addon(id="plugin.audio.mpdclient")
        self.addon_path = Path(self.xbmc_addon.getAddonInfo("path"))    # not needed yet, maybe remove later
        self.cli = resources.musicpd.MPDClient()

    def do_mpd_stuff(self):
        self.cli.connect(
            host=self.xbmc_addon.getSetting("mpd_host"),
            port=self.xbmc_addon.getSetting("mpd_port")
        )
        xbmc.log(str(self.cli.stats()["songs"]), level=1)
        self.cli.disconnect()


if __name__ == '__main__':
    kodi_addon = KodiAddon()
    kodi_addon.do_mpd_stuff()
