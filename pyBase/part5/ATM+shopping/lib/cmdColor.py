# -*- coding:utf-8 -*-
# Author:YEAR
class Logger:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def print_header(content):
    print(Logger.HEADER + content + Logger.ENDC)


def print_okblue(content):
    print(Logger.OKBLUE + content + Logger.ENDC)


def print_okgreen(content):
    print(Logger.OKGREEN + content + Logger.ENDC)


def print_warning(content):
    print(Logger.WARNING + content + Logger.ENDC)


def print_fail(content):
    print(Logger.FAIL + content + Logger.ENDC)
