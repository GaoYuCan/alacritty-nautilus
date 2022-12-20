# Alacritty Nautilus Extension
#
# Place me in ~/.local/share/nautilus-python/extensions/,
# ensure you have python-nautilus package, restart Nautilus, and enjoy :)
#
# This script is released to the public domain.

from gi.repository import Nautilus, GObject
from subprocess import call

# path to alacritty
ALACRITTY = 'alacritty'

# what name do you want to see in the context menu?
ALACRITTYNAME = 'Alacritty'


class AlacrittyExtension(GObject.GObject, Nautilus.MenuProvider):

    def launch_alacritty(self, menu, file):
        safepaths = '"' + file.get_location().get_path() + '" '
        call(ALACRITTY + ' --working-directory ' + safepaths + '&', shell=True)

    def get_background_items(self, *args):
        cfile_ = args[-1]
        item = Nautilus.MenuItem(
            name='AlacrittyOpenBackground',
            label='Open in ' + ALACRITTYNAME,
            tip='Opens the current directory in Alacritty')
        item.connect('activate', self.launch_alacritty, cfile_)

        return [item]
