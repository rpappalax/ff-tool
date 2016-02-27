#!/usr/bin/env python

import os
import sys
from firefox_env_handler import IniHandler
from fabric.api import local


env = IniHandler()
env.load_os_config('configs')


def install(channel):
    if channel == 'ALL':
        install_all()
        return

    filename = env.get(channel, 'DOWNLOAD_FILENAME')
    install_dir = env.get(channel, 'PATH_FIREFOX_APP')

    if IniHandler.is_linux():
        local('tar -jxf {0} && mv firefox {1}'.format(installer, install_dir))  # NOQA

    elif IniHandler.is_windows():
        local('{0} -ms'.format(installer))

        if channel == 'beta':
            # Since Beta and General Release channels install
            # to the same directory, install Beta first then
            # rename the directory.
            gr_install_dir = self.config.get('gr', 'PATH_FIREFOX_APP')
            local('mv "{0}" "{1}"'.format(gr_install_dir, install_dir))

    elif IniHandler.is_mac():
        from hdiutil import extract_dmg

        app_filename = env.get(channel, "APP_FILENAME")
        dmg_filename = env.get(channel, "DOWNLOAD_FILENAME")
        dmg_dirname = os.path.join('_temp', 'browsers', dmg_filename)

        extract_dmg(dmg_dirname, app_filename, channel)


def install_all():
    for channel in env.sections():
        install(channel)


def main():
    install_all()


if __name__ == '__main__':
    main()



"""
    def install_channel(self, channel):


        #was_cached = self.cache.config.getboolean('cached', channel)
        filename = self.config.get(channel, 'DOWNLOAD_FILENAME')
        install_dir = self.config.get(channel, 'PATH_FIREFOX_APP')
        installer = os.path.join('.', self.out_dir, filename)

        print(('Installing {0}'.format(channel)))

        if IniHandler.is_linux():
            

        elif IniHandler.is_windows():


        elif IniHandler.is_mac():
            from hdiutil import extract_dmg

            print(install_dir)
            print(installer)

            extract_dmg("_temp/browsers/FirefoxBeta.dmg")


        cmd = self.config.get(channel, 'PATH_FIREFOX_BIN_ENV')
        # local('"{0}" --version # {1}'.format(self.config.get(channel,
        #    'PATH_FIREFOX_BIN_ENV'), channel))
        local('"{0}" --version # {1}'.format(cmd, channel))
"""
