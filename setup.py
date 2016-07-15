from distutils.core import setup, Extension

dash_hash_module = Extension('navcoin_hash',
                                 sources = ['navcoinmodule.c',
                                            'navcoin.c',
                                            'sha3/blake.c',
                                            'sha3/bmw.c',
                                            'sha3/groestl.c',
                                            'sha3/jh.c',
                                            'sha3/keccak.c',
                                            'sha3/skein.c',
                                            'sha3/cubehash.c',
                                            'sha3/echo.c',
                                            'sha3/luffa.c',
                                            'sha3/simd.c',
											'sha3/shavite.c'
											'sha3/fugue.c'
                                            'sha3/hamsi.c'],
                               include_dirs=['.', './sha3'])

setup (name = 'navcoin_hash',
       author = 'Soopy452000',
       version = '1.0',
       description = 'Bindings for proof of work used by NavCOin',
       ext_modules = [navcoin_hash_module])
