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
	CGEventPost(kCGHIDEventTap, e);

# stores mouse position	
e = CGEventCreate(None);
pos = CGEventGetLocation(e);

postMClickDownE(10, 10);
postMDragggedE(20, 20);
postMClickUpE(10, 10);

# resets mouse position
postMMoved(int(pos.x), int(pos.y));
postMClickDownE(int(pos.x), int(pos.y));

# key massakcer
postKeyE(u'ü');
postKeyE(u'l');
postKeyE(u'f');
postKeyE(u'e');
postKeyE(u'!');

## ? key shiftär??
