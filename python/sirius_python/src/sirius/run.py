#!/usr/bin/python
# -*- coding: utf-8 -*-

import ring_v500
import pyring.tracking
import pyring.lattice
import pyring.optics
import matplotlib.pyplot as plt
import numpy
import time
import math

def test_compare_with_AT_linepass(the_ring):
    
    refpts = [0, 1500-1, 1800-1, len(the_ring)]
    posi = numpy.zeros((6,1))
    posi[:,0] = [0.001,0,0,0,0,0]
    posf = pyring.tracking.linepass(line = the_ring, particles = posi, refpts = refpts, engine = 'trackcpp', element_offset=1)
    
    for i in range(posf.shape[0]):
        for j in range(posf.shape[1]):
            print('{:+22.16E} '.format(posf[i,j])),
        print('')
        
def test_compare_with_AT_ringpass(the_ring):
    
    posi = numpy.zeros((6,1))
    posi[:,0] = [0.001,0,0,0,0,0]
    posf = pyring.tracking.ringpass(ring = the_ring, particles = posi, nr_turns = 1000, element_offset = 1)
 
    turns = [0,1,999]
    for i in range(posf.shape[0]):
        for t in turns:
            print('{:+22.16E} '.format(posf[i,t])),
        print('')

def test_linepass(the_ring):
    
    ''' set cavity state '''
    the_ring = pyring.lattice.copy.deepcopy(the_ring)
    the_ring = pyring.lattice.setcavity(the_ring, 'off')
    
    nr_particles = 2
    refpts = range(len(the_ring))
    posi = numpy.zeros((6,nr_particles))
    posi[:,0] = [0.001,0,0,0,0,0]
    posi[:,1] = [0.002,0,0,0,0,0]
    posf = pyring.tracking.linepass(line = the_ring, particles = posi, refpts = refpts, engine = 'trackcpp')
    
    s = pyring.lattice.findspos(lattice = the_ring, indices = range(len(the_ring)))
    p1 = pyring.tracking.select(posf, nr_particles = nr_particles, nr_elements = len(refpts), particle = 0)    
    p2 = pyring.tracking.select(posf, nr_particles = nr_particles, nr_elements = len(refpts), particle = 1)
    plt.plot(s, 1000*p1[0,:])
    plt.plot(s, 1000*p2[0,:])
    plt.xlabel('s [m]'); plt.ylabel('x [mm]')
    plt.show()
    
def test_ringpass(the_ring):
    
    nr_turns = 1000
    
    ''' set cavity state '''
    the_ring = pyring.lattice.copy.deepcopy(the_ring)
    the_ring = pyring.lattice.setcavity(the_ring, 'off')
    
    nr_particles = 3
    posi = numpy.zeros((6,nr_particles))
    posi[:,0] = [0.001,0,0,0,0,0]
    posi[:,1] = [0.002,0,0,0,0,0]
    posi[:,2] = [0.008,0,0,0,0,0]
    posf = pyring.tracking.ringpass(ring = the_ring, particles = posi, nr_turns = nr_turns, engine = 'trackcpp')

    lost = pyring.tracking.lost(posf, nr_particles = nr_particles, nr_turns = nr_turns)
    if lost:
        (turn,element,particle) = lost
        print('particle #' + str(particle) + ' lost at element #' + str(element) + ' in turn #' + str(turn))
        return None
    
    for particle in range(nr_particles):
        p = 1000 * pyring.tracking.select(posf, nr_turns = nr_turns, nr_particles = nr_particles, particle = particle)
        plt.scatter(p[0,:], p[1,:])
    plt.xlabel('rx [mm]'); plt.ylabel('px [mrad]')
    plt.show()   
    
def test_speed(the_ring):
    
    nr_turns       = 1026 * 2
    nr_particles   = 50 
    particles      = numpy.zeros((6,nr_particles))
    particles[:,0] = 0.001
    
    t0 = time.time()
    pyring.tracking.ringpass(ring = the_ring, particles = particles, nr_turns = nr_turns, engine = 'trackcpp')
    t1 = time.time()
    print(str(nr_turns)+ ' turns with ' + str(nr_particles) + ' particles: ' + str(t1-t0) + ' seconds')
    
def test_findm66(the_ring):
    
    t0 = time.time()
    m66,_ = pyring.tracking.findm66(the_ring, closed_orbit = None)
    b1 = pyring.lattice.findcells(the_ring, 'fam_name', 'b1')
    print(m66[b1[0],:,:])
    t1 = time.time()
    print(str(t1-t0))
    
def test_calcm66(the_ring):
    
    ''' set cavity state '''
    the_ring = pyring.lattice.copy.deepcopy(the_ring)
    the_ring = pyring.lattice.setcavity(the_ring, 'on')
    
    t0 = time.clock()
    m66_list,_ = pyring.tracking.findm66(the_ring, closed_orbit = None)
    t1 = time.clock()
    print('findm66: {:f} s'.format(t1-t0))
    t0 = time.clock()
    tm,_,_ = pyring.optics.calcm66(line = the_ring, m66_list = m66_list)
    t1 = time.clock()
    print('calcm66: {:f} s'.format(t1-t0))
    for i in range(tm.shape[0]):
        for j in range(tm.shape[1]):
            print('{:+22.16E} '.format(tm[i,j])),
        print('')

def test_twiss(the_ring):
    
    fractunes,m66,m66_list,closed_orbit = pyring.optics.fractunes(the_ring)
    twiss,_,_,_ = pyring.optics.twiss(line = the_ring, m66 = m66, m66_list = m66_list, closed_orbit = closed_orbit)
    
    s = pyring.lattice.findspos(the_ring)
    betax = pyring.lattice.getcellstruct(twiss, 'betax')
    betay = pyring.lattice.getcellstruct(twiss, 'betay')
    etax  = pyring.lattice.getcellstruct(twiss, 'etax')
    mux = pyring.lattice.getcellstruct(twiss, 'mux')
    tunex = numpy.array(mux) / math.pi / 2
    muy = pyring.lattice.getcellstruct(twiss, 'muy')
    tuney = numpy.array(muy) / math.pi / 2
    print((tunex[-1],tuney[-1]))
    
    plt.plot(s, 1000*numpy.array(etax))
    plt.xlabel('pos [m]'); plt.ylabel('etax  [mm]')
    plt.show()
    
    plt.plot(s, betax)
    plt.plot(s, betay)
    plt.xlabel('pos [m]'); plt.ylabel('betax,betay [m]')
    plt.show()
    
    plt.plot(s, tunex)
    plt.plot(s, tuney)
    plt.xlabel('pos [m]'); plt.ylabel('tunex,tuney')
    plt.show()
    
    print(fractunes)
    print(twiss)
            
def test_findorbit4(the_ring):
    
    ''' set cavity state '''
    the_ring = pyring.lattice.copy.deepcopy(the_ring)
    the_ring = pyring.lattice.setcavity(the_ring, 'off')
    
    ''' introduces an horizontal kick '''
    hcms = pyring.lattice.findcells(the_ring, 'fam_name', 'hcm')
    the_ring[hcms[0]].kick_angle[0] = 0.0003;
    
    t0 = time.time()
    orb = pyring.optics.findorbit4(ring = the_ring, de = 0, refpts = range(len(the_ring)))
    t1 = time.time()
    print('time[s]: ' + str(t1-t0))
    print('4D Closed orbit at beginning of model:')
    print('x  [mm]  : {0:+22.16E}'.format(orb[0,0]))
    print('xl [mrad]: {0:+22.16E}'.format(orb[1,0]))
    print('y  [mm]  : {0:+22.16E}'.format(orb[2,0]))
    print('yl [mrad]: {0:+22.16E}'.format(orb[3,0]))
    
    s = pyring.lattice.findspos(lattice = the_ring, indices = range(len(the_ring)))
    plt.scatter(s, 1000*orb[0,:])
    plt.show()
    
    print('ok')
    
def create_the_ring_sirius():
    
    the_ring = ring_v500.create_lattice(mode = 'AC10_6', energy = 3e9)
    the_ring = the_ring[::] # option to select subset of elements
    pyring.lattice.setcavity(the_ring, 'off')
    return the_ring

def create_the_ring_test():
    
    dipole = pyring.elements.rbend(fam_name = 'bend', length = 0.614131, angle = 0.035809880194256, angle_in = 0.035809880194256, angle_out = 0.0, nr_steps = 18, polynom_b = [0,-0.78]) 
    the_ring = [dipole]
    return the_ring

def run_tests():
          
    ''' load lattice model
        ------------------ '''
    the_ring = create_the_ring_sirius()
    #the_ring = create_the_ring_test()
    #pyring.lattice.printlattice(the_ring)
    
    ''' compares tracking with AT results '''
    #test_compare_with_AT_linepass(the_ring)
    #test_compare_with_AT_ringpass(the_ring)
    
    ''' tests linepass use '''
    #test_linepass(the_ring)
    
    ''' tests ringpass use '''
    #test_ringpass(the_ring)
    
    ''' tests speed of tracking code '''
    #test_speed(the_ring)
    
    ''' tests findorbit4 '''
    #test_findorbit4(the_ring)
    
    ''' tests findorbit6 '''
    #test_findorbit6(the_ring)
    
    ''' tests findm66 '''
    #test_findm66(the_ring)
      
    ''' tests calcm66 '''
    #test_calcm66(the_ring)
    
    ''' tests twiss '''
    test_twiss(the_ring)
    
''' TEST Suite for PyRing and TrackC++ '''
    
run_tests()
