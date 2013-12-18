/*
 compile with gcc -o main main.c -framework ApplicationServices


 
 */

#include <ApplicationServices/ApplicationServices.h>

int main(int argc, char **argv)
{
	int xPos = 20;
	int yPos = 20;
	
	CGEventRef m1 = CGEventCreateMouseEvent(NULL, kCGEventMouseMoved,    CGPointMake(xPos, yPos), kCGMouseButtonLeft);
	CGEventPost(kCGHIDEventTap, m1);
	CFRelease(m1);
	usleep(1000);

	CGEventRef c1 = CGEventCreateMouseEvent(NULL, kCGEventLeftMouseDown, CGPointMake(xPos, yPos), kCGMouseButtonLeft);
	CGEventPost(kCGHIDEventTap, c1);
	CFRelease(c1);
	usleep(1000);
	
	CGEventRef c2 = CGEventCreateMouseEvent(NULL, kCGEventLeftMouseUp,   CGPointMake(xPos, yPos), kCGMouseButtonLeft);
	CGEventPost(kCGHIDEventTap, c2);
	CFRelease(c2);
	usleep(1000);
}
