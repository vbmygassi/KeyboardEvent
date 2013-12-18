#!/usr/bin/python
#coding=utf-8

'''
http://stackoverflow.com/questions/1817628/clicking-the-mouse-down-to-drag-objects-on-mac
http://stackoverflow.com/questions/18027342/how-can-i-call-cgeventkeyboardsetunicodestring-from-python
'''

import sys, time
from Quartz.CoreGraphics import *

def postMClickDownE(x, y):
	e = CGEventCreateMouseEvent(None, kCGEventLeftMouseDown, (x, y), kCGMouseButtonLeft);
	CGEventPost(kCGHIDEventTap, e);

def postMClickUpE(x, y):
	e = CGEventCreateMouseEvent(None, kCGEventLeftMouseUp, (x, y), kCGMouseButtonLeft);
	CGEventPost(kCGHIDEventTap, e);

def postMDragggedE(x, y):
	e = CGEventCreateMouseEvent(None, kCGEventLeftMouseDragged, (x, y), kCGMouseButtonLeft);
	CGEventPost(kCGHIDEventTap, e);

def postMMoved(x, y):
	e = CGEventCreateMouseEvent(None, kCGEventMouseMoved, (x, y), kCGMouseButtonLeft);
	CGEventPost(kCGHIDEventTap, e);
 	
def postKeyE(key):
	e = CGEventCreateKeyboardEvent(None, 0, True);
	CGEventKeyboardSetUnicodeString(e, len(key), map(ord, key));
	# CGEventSetFlags(e, kCGEventFlagMaskShift);
	CGEventPost(kCGHIDEventTap, e);

def postKeycodeE(code):
	e = CGEventCreateKeyboardEvent(None, code, True);	
	CGEventPost(kCGHIDEventTap, e);
	e = CGEventCreateKeyboardEvent(None, code, False);	
	CGEventPost(kCGHIDEventTap, e);

def postSearchSCE():
	e = CGEventCreateKeyboardEvent(None, 49, True);
	CGEventSetFlags(e, kCGEventFlagMaskCommand);
	CGEventPost(kCGHIDEventTap, e);
	e = CGEventCreateKeyboardEvent(None, 49, False);
	CGEventPost(kCGHIDEventTap, e);

# stores mouse position	
e = CGEventCreate(None);
pos = CGEventGetLocation(e);

# wild wild click
postMClickDownE(10, 10);
postMDragggedE(20, 20);
postMClickUpE(10, 10);

# resets mouse position
postMMoved(int(pos.x), int(pos.y));
time.sleep(1);
postMClickDownE(int(pos.x), int(pos.y));
time.sleep(1);

# opens spotlight
postSearchSCE();

# easy
time.sleep(1);

# types
postKeyE(u'ü');
time.sleep(1);
postKeyE(u'l');
time.sleep(1);
postKeyE(u'f');
time.sleep(1);
postKeyE(u'e');
time.sleep(1);
postKeyE(u'!');
time.sleep(3);

# enters
postKeycodeE(52);

