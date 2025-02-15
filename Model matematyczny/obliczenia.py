import sympy
phi, xa, ya, r, alpha1, alpha2, beta1, beta2, rhok1, rhok2, l1, l2 = sympy.symbols("\u03c6, xa, ya, r, \u03b11, \u03b12, \u03b21, \u03b22, \u03c1k1, \u03c1k2, l1, l2")
#kąty w radianach
t0a = sympy.Matrix([
    [sympy.cos(phi), -1*sympy.sin(phi), 0, xa],
    [sympy.sin(phi), sympy.cos(phi), 0, ya],
    [0, 0, 1, r],
    [0, 0, 0, 1]
])

tab = sympy.Matrix([
    [sympy.sin(alpha1), sympy.cos(alpha1), 0, 0],
    [0, 0, 1, l1],
    [sympy.cos(alpha1), -1*sympy.sin(alpha1), 0, 0],
    [0, 0, 0, 1]
])

tac = sympy.Matrix([
    [sympy.sin(alpha2),sympy.cos(alpha2),0,0],
    [0,0,1,-1*l1],
    [sympy.cos(alpha2),-1*(sympy.sin(alpha2)),0,0],
    [0,0,0,1]
])

tad = sympy.Matrix([
    [sympy.cos(beta1),-1*(sympy.sin(beta1)),0,-1*l2],
    [sympy.sin(beta1),sympy.cos(beta1),0,l1],
    [0,0,1,0],
    [0,0,0,1]
])

tae = sympy.Matrix([
    [sympy.cos(beta2),-1*(sympy.sin(beta2)),0,-1*l2],
    [sympy.sin(beta2),sympy.cos(beta2),0,-1*l1],
    [0,0,1,0],
    [0,0,0,1]
])

t0b = t0a*tab
t0c = t0a*tac
t0d = t0a*tad
t0e = t0a*tae

rhok1 = sympy.Matrix([
    [-1*r*sympy.cos(alpha1)],
    [r*sympy.sin(alpha1)],
    [0],
    [1]
])

rhok2 = sympy.Matrix([
    [-1*r*sympy.cos(alpha2)],
    [r*sympy.sin(alpha2)],
    [0],
    [1]
])

#jak obliczyć pochodną po czasie z macierzy, jeżeli nie zależy ona od czasu??
#względem czego mam obliczyć pochodną z macierzy t0a, t0b, t0c, t0d, t0e??