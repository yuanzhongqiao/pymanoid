#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015-2016 Stephane Caron <stephane.caron@normalesup.org>
#
# This file is part of pymanoid.
#
# pymanoid is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# pymanoid is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# pymanoid. If not, see <http://www.gnu.org/licenses/>.


import numpy
import openravepy


__env__ = None


__gravity__ = numpy.array([0, 0, -9.80665])  # ISO 80000-3


def get_env():
    return __env__


def get_gravity():
    return __gravity__


def get_viewer():
    return __env__.GetViewer()


def init(env_file=None, env_xml=None):
    env = openravepy.Environment()
    if env_file:
        env.Load(env_file)
    elif env_xml:
        env.LoadData(env_xml)
    env.GetPhysicsEngine().SetGravity(__gravity__)
    env.SetViewer('qtcoin')
    register_env(env)
    set_default_background_color()
    set_default_camera()


def register_env(env):
    global __env__
    __env__ = env


def set_camera_back(x=-3, y=0, z=0.7):
    get_viewer().SetCamera([
        [0,  0, 1, x],
        [-1, 0, 0, y],
        [0, -1, 0, z],
        [0,  0, 0, 1.]])


def set_camera_bottom(x=0, y=0, z=-2):
    get_viewer().SetCamera([
        [0, -1, 0, x],
        [1,  0, 0, y],
        [0,  0, 1, z],
        [0,  0, 0, 1]])


def set_camera_front(x=+3, y=0, z=0.7):
    get_viewer().SetCamera([
        [0,  0, -1, x],
        [1,  0,  0, y],
        [0, -1,  0, z],
        [0,  0,  0, 1.]])


def set_camera_left(x=0, y=+3, z=0.7):
    get_viewer().SetCamera([
        [-1, 0,  0, x],
        [0,  0, -1, y],
        [0, -1,  0, z],
        [0,  0,  0, 1.]])


def set_camera_right(x=0, y=-3, z=0.7):
    get_viewer().SetCamera([
        [1,  0,  0, x],
        [0,  0, 1, y],
        [0, -1, 0, z],
        [0,  0, 0, 1.]])


def set_camera_top(x=0, y=0, z=3):
    get_viewer().SetCamera([
        [0, -1,  0, x],
        [-1, 0,  0, y],
        [0,  0, -1, z],
        [0,  0,  0, 1.]])


def set_default_background_color():
    get_viewer().SetBkgndColor([.6, .6, .8])


def set_default_camera():
    get_viewer().SetCamera([  # default view from behind
        [0.,  0., 1., -3.],
        [-1., 0., 0.,  0.],
        [0., -1., 0.,  0.7],
        [0.,  0., 0.,  1.]])
