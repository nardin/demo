init -20 python:
    from random import uniform
    import math
    class ParticleGenerator(renpy.Displayable):
        def __init__(self, image, y, count=128, max_age=5.0, **kwargs):
            super(ParticleGenerator, self).__init__(**kwargs)
            self.st         = 0
            self.y          = y
            self.image      = image
            self.count      = count
            self.max_age    = max_age
            self.particles  = []
            self.reset_particles()
        def reset_particles(self):
            self.particles = []
            for i in xrange(0,self.count):
                self.particles.append(self.create_particle())
        def create_particle(self, st=0):
            return {
                    "x": config.screen_width/2,
                    "y": self.y,
                    "st": st,
                    "birth": uniform(0.0,self.max_age),
                    "age": uniform(self.max_age/2, self.max_age),
                    "scale": uniform(0.25,1.0),
                    "vx": uniform(-0.50,0.50),
                    "vy": uniform(-1.00,-0.25),
                }
        def render(self, width, height, st, at):
            render = renpy.Render(0,0)
            if st > self.st:
                self.st = st
            else:
                for p in self.particles:
                    p['st'] -= self.st
                self.st = st
            for k, p in enumerate(self.particles):
                if st < p['birth'] and p['birth']:
                    continue
                elif st > p['birth'] and p['birth']:
                    p['birth'] = None
                    p['st'] = st
                t = (st - p['st'])/p['age']
                if t >= 1.0 or t < 0:
                    self.particles[k] = self.create_particle(st)
                    continue
                p['x'] += p['vx']
                p['y'] += p['vy']
                z = 1.0 - t
                a = 0.7
                t = Transform(child=self.image, subpixel=True, zoom=z, alpha=a, xanchor=0.5, yanchor=0.5)
                r = renpy.render(t,0,0,st,at)
                render.blit(r,(p['x'],p['y']))
            renpy.redraw(self,0)
            return render
        def visit(self):
            return [self.image]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
