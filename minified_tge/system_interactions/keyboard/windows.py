import ctypes
from ctypes import wintypes
from.import virtual_keys as keys
user32=ctypes.WinDLL('user32')
user32.GetAsyncKeyState.restype=wintypes.SHORT
def is_key_pressed(key_code):A=user32.GetAsyncKeyState(key_code);return A&32768!=0
KEYEVENTF_KEYDOWN=0
KEYEVENTF_KEYUP=2
def press_key(key_code):A=key_code;user32.keybd_event(A,0,KEYEVENTF_KEYDOWN,0);user32.keybd_event(A,0,KEYEVENTF_KEYUP,0)
def hold_key(key_code):user32.keybd_event(key_code,0,KEYEVENTF_KEYDOWN,0)
def release_key(key_code):user32.keybd_event(key_code,0,KEYEVENTF_KEYUP,0)