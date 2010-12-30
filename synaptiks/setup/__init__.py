# -*- coding: utf-8 -*-
# Copyright (c) 2010, Sebastian Wiesner <lunaryorn@googlemail.com>
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.


"""
    synaptiks.setup
    ===============

    Extension code for setup.py.  This module is *not* installed!

    .. moduleauthor::  Sebastian Wiesner  <lunaryorn@googlemail.com>
"""

from __future__ import (print_function, division, unicode_literals,
                        absolute_import)

import os
from subprocess import Popen, PIPE
from distutils.cmd import Command
from distutils import spawn


def get_output(command):
    return Popen(command, stdout=PIPE).communicate()[0].strip()


def change_prefix(path, old_prefix, new_prefix):
    old_prefix = os.path.normpath(old_prefix)
    path = os.path.normpath(path)
    unprefixed_path = path[len(old_prefix)+1:]
    return os.path.normpath(os.path.join(new_prefix, unprefixed_path))


class BaseCommand(Command):
    def _find_executable(self, executable, missing_message=''):
        self.announce('Searching {0}...'.format(executable))
        exe_path = spawn.find_executable(executable)
        if exe_path is None:
            raise SystemExit('Could not find {0}. {1}'.format(
                executable, missing_message))
        self.announce(' ...{0} found at {1}'.format(executable, exe_path))
        return exe_path

