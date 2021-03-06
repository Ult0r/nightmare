#!/usr/bin/env python
# -*- coding:utf-8 -*-

# ---------- ---------- ---------- ---------- ---------- ---------- ---------- #
# @file pyTestUtils                                                            #
# @author Hanno Sternberg <hanno@almostintelligent.de>                         #
#                                                                              #
# This file contains an asorted collection of utilities:                       #
#     - Terminal coloring                                                      #
#     - A custom logger                                                        #
#                                                                              #
# @license MIT                                                                 #
#                                                                              #
# This software is licensed under the MIT License                              #
#                                                                              #
# Copyright (c) 2012-2015 Hanno Sternberg                                      #
#                                                                              #
# Permission is hereby granted, free of charge, to any person obtaining a copy #
# of this software and associated documentation files (the "Software"), to     #
# deal in the Software without restriction, including without limitation the   #
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or  #
# sell copies of the Software, and to permit persons to whom the Software is   #
# furnished to do so, subject to the following conditions:                     #
#                                                                              #
# The above copyright notice and this permission notice shall be included in   #
# all copies or substantial portions of the Software.                          #
#                                                                              #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR   #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,     #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  #
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER       #
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING      #
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS #
# IN THE SOFTWARE.                                                             #
# ---------- ---------- ---------- ---------- ---------- ---------- ---------- #

import sys
import os
import time


def isLambda(v):
    """
    Test if a given value is a lambda function

    @type        v: Anything (preferable a lambda function)
    @param        v: Some value
    @rtype:     Boolean
    @return:    True, if the value is a lambda function
    """
    return isinstance(v, type(lambda: None)) and v.__name__ == '<lambda>'


class TermColor:
    __slots__ = [
        'Black', 'Red', 'Green', 'Yellow', 'Blue', 'Purple', 'Cyan', 'White',
        'Normal', 'Bold', 'Dim', 'Background', 'Text', 'active']
    """ Print colored text """
    Black = 0
    """Black color code"""
    Red = 1
    """Red color code"""
    Green = 2
    """Green color code"""
    Yellow = 3
    """Yellow color code"""
    Blue = 4
    """Blue color code"""
    Purple = 5
    """Purple color code"""
    Cyan = 6
    """Cyan color code"""
    White = 7
    """White color code"""
    Normal = 0
    """Normal text style"""
    Bold = 1
    """Bold text style"""
    Dim = 2
    """Dim text style"""
    Background = 40
    """Change background color"""
    Text = 30
    """Change text color"""

    active = True
    """activate colourful output"""

    @staticmethod
    def colorText(text, fg=7, bg=0, style=0):
        if TermColor.active and (os.getenv('ANSI_COLORS_DISABLED') is None):
            return u"\033[{:02};{:2};{:2}m{:s}\033[0m".format(style, fg + TermColor.Text, bg + TermColor.Background, text)
        else:
            return text


@staticmethod
def logPrinter(msg):
    print msg


class logger:
    __slots__ = ['_buffer']
    """Logger class"""
    _buffer = []
    """Message buffer"""
    autoflush = False
    """Autoflush logged messages"""
    logListener = logPrinter
    """Listener to redirect output"""
    @staticmethod
    def log(str, showTime=True):
        """
        Writes a log message to the buffer

        @type    str: String
        @param    str: Log message
        """
        if showTime:
            msg = u"{0} {1}".format(TermColor.colorText("[{0}]".format(time.strftime("%H:%M:%S")), TermColor.Blue, style=TermColor.Dim), str.strip("\r\n"))
        else:
            msg = u"           {0}".format(str.strip("\r\n"))
        if logger.autoflush:
            logger.logListener(msg)
        else:
            logger._buffer.append(msg)

    @staticmethod
    def flush(quiet=False):
        """
        flushes the message buffer

        @type    quiet: Boolean
        @param    quiet: Flag if the buffer should be printed or not
        """
        if not quiet:
            for b in logger._buffer:
                logger.logListener(b)
            sys.stdout.flush()
        logger.clear()

    @staticmethod
    def clear():
        """
        Clears the buffer
        """
        logger._buffer = []
