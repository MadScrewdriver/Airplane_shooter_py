import ctypes
from ctypes import Structure, POINTER, c_long, c_uint

u32 = ctypes.windll.user32

SPI_GETWORKAREA = 0x30

class Rect(Structure):
    _fields_ = [
        ('left', c_long),
        ('top', c_long),
        ('right', c_long),
        ('bottom', c_long)
        ]


SPI = u32.SystemParametersInfoA
SPI.argtypes = [
    c_uint,         # __in      UINT uiAction,
    c_uint,         # __in      UINT uiParam,
    POINTER(Rect),  # __inout   PVOID pvParam,
    c_uint,         # __in      UINT fWinIni
    ]


def get_work_area():
    area = Rect()
    res = SPI(SPI_GETWORKAREA, 0, area, 0)
    if not res:
        return None
    return area.bottom - 23


if __name__ == '__main__':
    print(get_work_area())