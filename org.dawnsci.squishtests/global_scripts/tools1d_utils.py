import socket

def gethostname():
	return socket.gethostname()

def mouseDragRegion(plottingSystem, snoozet=5):
	c = waitForObject(plottingSystem.getPlotComposite())
	b = c.bounds

	test.log("Image at (%d, %d) is %d x %d" % (b.x,b.y, b.width, b.height))
	snooze(snoozet)
	mouseDrag(c, b.x+b.width/2.35, b.y+b.height/4., int(b.width/7.5),0, 0, Button.Button1)
	snooze(snoozet)
