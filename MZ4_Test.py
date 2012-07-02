'''
Created on Jun 25, 2012

@author: Saber
'''

if __name__ == '__main__':
    from MarshalZ4 import dumps
    import time
    car = {'BMW':'bavaria dutch cars factory',
           'Mercedes':'dutch cars factory',
           'Ferrari':'super fast itailien taste cars factory',
           'Buggati':'1001 horse power to unleach your speed limits.'}
    st = time.time()
    for _ in range(1000000):dumps(car)
    print '1 Round - Dictionnary:',time.time() - st,'(s)'
    pc = ['IBM','DELL','Sony','Gigabyte','hp','LG']
    st = time.time()
    for _ in range(1000000):dumps(pc)
    print '2 Round - List',time.time() - st,'(s)'
    
    st = time.time()
    __ = 1
    for _ in range(1000000):dumps(__)
    print '3 Round - Int Flawless',time.time() - st,'(s)'