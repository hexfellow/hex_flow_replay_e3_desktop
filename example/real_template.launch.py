#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################
# Copyright 2026 Dong Zhaorui. All rights reserved.
# Author: Dong Zhaorui 847235539@qq.com
# Date  : 2026-04-28
################################################################

from hex_flow_core import LaunchConfig
from hex_flow_node_robot import default_robot_archer_y6_node
from hex_flow_node_teleop import default_teleop_keyboard_node
from hex_flow_node_camera import default_cam_berxel_node, default_cam_usb_node
from hex_flow_template_e3_desktop import default_template_e3_desktop_node

config = LaunchConfig(
    local_only=True,
    enable_tui=True,
    log_to_file=True,
    save_path="/tmp/real_template.yml",
)

nodes = {
    "left_archer_y6":
    default_robot_archer_y6_node(
        name="left_archer_y6",
        # host="172.18.23.197",
        # port=8439,
        host="172.18.27.26",
        port=8439,
        ctrl_rate=500,
        state_buffer_size=200,
        sens_ts=True,
        grip_type="gp80",
        pose_end_in_flange="0.187,0.0,0.0,1.0,0.0,0.0,0.0",
        required=True,
        hidden=True,
        remap_dict={
            "arm_state": "left_archer_y6/arm_state",
            "grip_state": "left_archer_y6/grip_state",
            "arm_ctrl": "left_archer_y6/arm_ctrl",
            "grip_ctrl": "left_archer_y6/grip_ctrl",
        },
    ),
    "right_archer_y6":
    default_robot_archer_y6_node(
        name="right_archer_y6",
        # host="172.18.23.197",
        # port=9439,
        host="172.18.27.26",
        port=9439,
        ctrl_rate=500,
        state_buffer_size=200,
        sens_ts=True,
        grip_type="gp80",
        pose_end_in_flange="0.187,0.0,0.0,1.0,0.0,0.0,0.0",
        required=True,
        hidden=True,
        remap_dict={
            "arm_state": "right_archer_y6/arm_state",
            "grip_state": "right_archer_y6/grip_state",
            "arm_ctrl": "right_archer_y6/arm_ctrl",
            "grip_ctrl": "right_archer_y6/grip_ctrl",
        },
    ),
    "teleop_keyboard":
    default_teleop_keyboard_node(
        name="teleop_keyboard",
        device_path="",
        rate_hz=100.0,
        required=True,
        hidden=True,
        remap_dict={"teleop_keyboard": "teleop_keyboard/teleop_keyboard"},
    ),
    "template_e3_desktop":
    default_template_e3_desktop_node(
        name="template_e3_desktop",
        rate_hz=500.0,
        arm_stable_pos="0.0,-1.5,3.0,0.07,0.0,0.0",
        grip_stable_pos="0.5",
        arrive_threshold=0.06,
        arm_err_threshold=0.02,
        grip_err_threshold=0.02,
        required=True,
        hidden=False,
        remap_dict={
            "left_arm_state": "left_archer_y6/arm_state",
            "right_arm_state": "right_archer_y6/arm_state",
            "left_grip_state": "left_archer_y6/grip_state",
            "right_grip_state": "right_archer_y6/grip_state",
            "left_arm_ctrl": "left_archer_y6/arm_ctrl",
            "right_arm_ctrl": "right_archer_y6/arm_ctrl",
            "left_grip_ctrl": "left_archer_y6/grip_ctrl",
            "right_grip_ctrl": "right_archer_y6/grip_ctrl",
            "keys": "teleop_keyboard/teleop_keyboard",
        },
    ),
}

config.set_nodes(nodes)
print(config.export())
