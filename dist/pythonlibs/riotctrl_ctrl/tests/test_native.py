# Copyright (C) 2021 Freie Universität Berlin
#
# This file is subject to the terms and conditions of the GNU Lesser
# General Public License v2.1. See the file LICENSE in the top level
# directory for more details.

import os.path

import riotctrl_ctrl.native


def test_reset():
    env = {'DEBUG_ADAPTER_ID': '', 'BOARD': 'native'}
    ctrl = riotctrl_ctrl.native.NativeRIOTCtrl(
        application_directory=os.path.normpath(os.path.join(
            os.path.abspath(__file__),
            '..', '..', '..', '..', '..',
            'examples', 'hello-world'
        )),
        env=env,
    )
    print(ctrl.application_directory)
    assert not ctrl.env['DEBUG_ADAPTER_ID']
    ctrl.make_run(['flash'])
    with ctrl.run_term(reset=False):
        # DEBUG_ADAPTER_ID is now a PID
        assert int(ctrl.env['DEBUG_ADAPTER_ID'])
        ctrl.term.expect_exact('Hello World!')
        ctrl.reset()
        ctrl.term.expect_exact('!! REBOOT !!')
        ctrl.term.expect_exact('Hello World!')
