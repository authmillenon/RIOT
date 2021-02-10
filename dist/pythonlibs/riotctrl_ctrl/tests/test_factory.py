# Copyright (C) 2021 Freie Universität Berlin
#
# This file is subject to the terms and conditions of the GNU Lesser
# General Public License v2.1. See the file LICENSE in the top level
# directory for more details.

import riotctrl.ctrl

import riotctrl_ctrl.factory
import riotctrl_ctrl.native


def test_wo_board():
    factory = riotctrl_ctrl.factory.RIOTCtrlFactory()
    assert factory.DEFAULT_CLS is riotctrl.ctrl.RIOTCtrl
    ctrl = factory.get_ctrl()
    # pylint: disable=unidiomatic-typecheck
    # in this case we want to know the exact type
    assert type(ctrl) is riotctrl.ctrl.RIOTCtrl


def test_w_board_in_default_board_cls():
    env = {'BOARD': 'native'}
    factory = riotctrl_ctrl.factory.RIOTCtrlFactory()
    assert 'native' in factory.board_cls
    ctrl = factory.get_ctrl(env=env)
    # pylint: disable=unidiomatic-typecheck
    # in this case we want to know the exact type
    assert type(ctrl) is riotctrl_ctrl.native.NativeRIOTCtrl


def test_w_board_in_not_default_board_cls():
    env = {'BOARD': 'foobar-test'}
    factory = riotctrl_ctrl.factory.RIOTCtrlFactory()
    assert 'foobar-test' not in factory.board_cls
    ctrl = factory.get_ctrl(env=env)
    # pylint: disable=unidiomatic-typecheck
    # in this case we want to know the exact type
    assert type(ctrl) is riotctrl.ctrl.RIOTCtrl


def test_w_board_custom_board_cls():
    env = {'BOARD': 'native'}
    factory = riotctrl_ctrl.factory.RIOTCtrlFactory(
        board_cls={'native': riotctrl.ctrl.RIOTCtrl}
    )
    assert 'native' in factory.board_cls
    ctrl = factory.get_ctrl(env=env)
    # pylint: disable=unidiomatic-typecheck
    # in this case we want to know the exact type
    assert type(ctrl) is riotctrl.ctrl.RIOTCtrl
