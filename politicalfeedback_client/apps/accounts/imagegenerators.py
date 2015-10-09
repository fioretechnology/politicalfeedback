from imagekit import ImageSpec, register
from imagekit.processors import ResizeToFill,ResizeToFit,SmartResize,ResizeToCover,ResizeCanvas

class Thumbnail300(ImageSpec):
    processors = [ResizeToFit(300,200)]
    format = 'PNG'
    options = {'quality': 90}

register.generator('accounts:thumbnail300', Thumbnail300)

class Thumbnail200(ImageSpec):
	processors = [ResizeToFit(200, 200),ResizeCanvas(200,200)]
	format = 'PNG'
	options = {'quality': 90}

register.generator('accounts:thumbnail200', Thumbnail200)

class Thumbnail50(ImageSpec):
    processors = [ResizeToFit(50, 40),ResizeCanvas(50,40)]
    format = 'PNG'
    options = {'quality': 80}

register.generator('accounts:thumbnail50', Thumbnail50)


class Thumbnail80(ImageSpec):
    processors = [ResizeToFit(80, 65),ResizeCanvas(80,65)]
    format = 'PNG'
    options = {'quality': 90}

register.generator('accounts:thumbnail80', Thumbnail80)

class Thumbnail90(ImageSpec):
    processors = [ResizeToFit(90, 90),ResizeCanvas(90,90)]
    format = 'PNG'
    options = {'quality': 90}

register.generator('accounts:thumbnail90', Thumbnail90)

class Thumbnail450(ImageSpec):
    processors = [ResizeToFit(400, 300),ResizeCanvas(400,300)]
    format = 'PNG'
    options = {'quality': 90}

register.generator('accounts:thumbnail450', Thumbnail450)

class Thumbnail850(ImageSpec):
    processors = [ResizeToFit(850, 300)]
    format = 'PNG'
    options = {'quality': 90}

register.generator('accounts:thumbnail850', Thumbnail850)

class Thumbnail1400(ImageSpec):
    processors = [ResizeToFit(1400, 1400),ResizeCanvas(1400,1400)]
    format = 'JPEG'
    options = {'quality': 100}

register.generator('accounts:thumbnail1400', Thumbnail1400)


class Thome(ImageSpec):
    processors = [ResizeToFit(400, 220)]
    format = 'PNG'
    options = {'quality': 100}

register.generator('accounts:thome', Thome)


class Chome(ImageSpec):
    processors = [ResizeToFit(1200, 440)]
    format = 'PNG'
    options = {'quality': 100}

register.generator('accounts:chome', Chome)