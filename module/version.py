# https://github.com/Senzdetta/Senzdetta

from utils.color import Color

class Version:
    @staticmethod
    def execute(*args):
        name = "Senzdetta"
        version = "v0.1.20261008"
        developer = "Senzdetta"
        homepage = "https://github.com/Senzdetta/Senzdetta"

        print(f"{Color.DG}- {Color.GG}{name} {Color.DG}-{Color.N}")
        print(f"{Color.N}Version: {Color.GG}{version}{Color.N}")
        print(f"{Color.N}Developer: {Color.GG}{developer}{Color.N}")
        print(f"{Color.N}Homepage: {Color.GG}{homepage}{Color.N}")

# Copyright (c) 2026 Senzdetta