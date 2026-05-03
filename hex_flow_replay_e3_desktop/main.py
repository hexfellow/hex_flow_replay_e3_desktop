#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################
# Copyright 2026 Dong Zhaorui. All rights reserved.
# Author: Dong Zhaorui 847235539@qq.com
# Date  : 2026-04-28
################################################################

from .replay_e3_desktop import HexFlowReplayE3Desktop


def main():
    replay = HexFlowReplayE3Desktop()
    replay.start()
    replay.run()


if __name__ == "__main__":
    main()
