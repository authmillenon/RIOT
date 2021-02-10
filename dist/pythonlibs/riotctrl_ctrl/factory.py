# Copyright (C) 2021 Freie Universität Berlin
#
# This file is subject to the terms and conditions of the GNU Lesser
# General Public License v2.1. See the file LICENSE in the top level
# directory for more details.

import os

import riotctrl.ctrl

from .native import NativeRIOTCtrl


class RIOTCtrlFactory:
    """Abstract factory to create different RIOTCtrl types based on
    the environment variables.

    :param board_cls: A dict that maps a `BOARD` name to a RIOTCtrl class.
    """
    DEFAULT_CLS = riotctrl.ctrl.RIOTCtrl
    BOARD_CLS = {
        'native': NativeRIOTCtrl
    }

    def __init__(self, board_cls=None):
        self.board_cls = {}
        self.board_cls.update(self.BOARD_CLS)
        if board_cls is not None:
            self.board_cls.update(board_cls)

    def get_ctrl(self, application_directory='.', env=None):
        """
        Returns a RIOTCtrl object of a class as specified in `board_cls` on
        initialization.

        :param application_directory: `application_directory` initialization
                                      parameter for the RIOTCtrl object
        :param env:                   `env` initialization parameter for
                                      the RIOTCtrl object. This will also be
                                      used to determine the actual class of
                                      the return value.

        When `BOARD` is set in the environment variables when `env` is provided
        in `env`, that value is used to look-up the RIOTCtrl class in the
        factory's `board_cls` for that specific `BOARD`. The default is
        `riotctrl_ctrl.native.NativeRIOTCtrl` if `BOARD='native'` and
        `riotctrl.ctrl.RIOTCtrl` otherwise.
        """
        the_env = {}
        the_env.update(os.environ)
        if env:
            the_env.update(env)
        if 'BOARD' not in the_env or the_env['BOARD'] not in self.board_cls:
            cls = self.DEFAULT_CLS
        else:
            cls = self.board_cls[the_env['BOARD']]
        # cls does its own fetching of `os.environ` so only provide `env` here
        return cls(application_directory=application_directory, env=env)
