# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 00:35:49 2018

@author: criow
"""

from py2exeUtils import Compiler

a= Compiler(
    [
        #Python Files
        'Optimizer.py',
        'compile.py',
        'setup.py',
        #Text Files
        'readme.txt'
    ],
    [
        'mdlxconv/MdlxConv_1.04.exe'
    ]
)
a.changeFolderNames('Optimizer')
a.Compile()
print 'Done!'