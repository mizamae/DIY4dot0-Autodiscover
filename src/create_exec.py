'''
Created on 4 nov. 2019

@author: Zabaleta-De Carlos
'''

import PyInstaller.__main__
import os

package_name='mainmodule.pyw'

PyInstaller.__main__.run([
    '--name=Autodiscover',
    '--onefile',
    '--nowindowed',
    '--icon=%s' % os.path.join('.','dist', 'media', 'favicon.ico'),
    package_name,
])