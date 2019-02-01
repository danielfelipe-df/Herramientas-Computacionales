import cython

def suma(n):
	ni,nj = n.shape
	s=0
	for i in range(ni):
		for j in range(nj):
			s=s+n[i,j]
	
	return s


def suma_opt(long[:,:] n):
	cdef int ni,nj
	ni=n.shape[0] # maximo 8 dimensiones
	nj=n.shape[1]
	cdef int s=0
	for i in range(ni):
		for j in range(nj):
			s=s+n[i,j]
	return s

@cython.boundscheck(False) 
@cython.wraparound(False)
def suma_ropt(long[:,:] n):
	cdef int ni,nj,i,j
	ni=n.shape[0] # maximo 8 dimensiones
	nj=n.shape[1]
	cdef int s=0
	for i in range(ni):
		for j in range(nj):
			s=s+n[i,j]
	
	return s

@cython.boundscheck(False) 
@cython.wraparound(False)
def suma_r1opt(long[:,:] n):
	cdef int ni,nj,i,j
	ni=n.shape[0] # maximo 8 dimensiones
	nj=n.shape[1]
	cdef int s=0
	for j in range(nj):
		for i in range(ni):
			s=s+n[i,j]
	
	return s
