#!/usr/bin/env python
# -*- coding: utf-8 -*-

# test_irkcmd.py

import irkcmd as irkcmd
import pytest

def test_irkMain():
    ret = irkcmd.irkMain()
    assert ret is True

def test_showCmds():
    ret = irkcmd.showCmds()
    assert ret is True

def test_execCmdSend():
    ret = irkcmd.execCmdSend('test')
    assert ret is False

@pytest.mark.parametrize("test_input", [
    "irkconfig.sample.json"
])
def test_loadConfig(test_input):
    ret = irkcmd.loadConfig(test_input)
    assert ret != ''
