import AES

class AEStest:
    def __init__(self):
        pass


    def runTest(self):

        d = AES()
        state =[[0x19,0xa0,0x9a,0xe9],
    			[0x3d,0xf4,0xc6,0xf8],
    			[0xe3,0xe2,0x8d,0x48],
    			[0xbe,0x2b,0x2a,0x08]]

                
    	print("\nffAdd")
    	print(str(hex(d.ffAdd(0x57,0x83)) == hex(0xd4)))

    	print("\nxtime")
    	print(str(hex(d.xtime(0x57)) == hex(0xae)))
    	print(str(hex(d.xtime(0xae)) == hex(0x47)))
    	print(str(hex(d.xtime(0x47)) == hex(0x8e)))
    	print(str(hex(d.xtime(0x8e)) == hex(0x07)))

    	print("\nffMultiply")
    	print(str(hex(d.ffMultiply(0x57,0x13)) == hex(0xfe)))

    	print("\nsubWord")
    	print(str( hex(d.subWord(0x00102030)) == hex(0x63cab704) ))
    	print(str(hex(d.subWord(0x40506070)) == hex(0x0953d051) ))
    	print(str(hex(d.subWord(0x8090a0b0)) == hex(0xcd60e0e7) ))
    	print(str(hex(d.subWord(0xc0d0e0f0)) == hex(0xba70e18c) ))

    	print("\nrotWord")
    	print(str(hex(d.rotWord(0x09cf4f3c)) == hex(0xcf4f3c09)))
    	print(str(hex(d.rotWord(0x2a6c7605)) == hex(0x6c76052a)))

    	print("\nKeyExpansion")
    	key = [ 0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7,0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c ]
    	expanded = [ 0x2b7e1516, 0x28aed2a6, 0xabf71588, 0x09cf4f3c, 0xa0fafe17,
    	0x88542cb1, 0x23a33939, 0x2a6c7605, 0xf2c295f2, 0x7a96b943,
    	0x5935807a, 0x7359f67f, 0x3d80477d, 0x4716fe3e, 0x1e237e44,
    	0x6d7a883b, 0xef44a541, 0xa8525b7f, 0xb671253b, 0xdb0bad00,
    	0xd4d1c6f8, 0x7c839d87, 0xcaf2b8bc, 0x11f915bc, 0x6d88a37a,
    	0x110b3efd, 0xdbf98641, 0xca0093fd, 0x4e54f70e, 0x5f5fc9f3,
    	0x84a64fb2, 0x4ea6dc4f, 0xead27321, 0xb58dbad2, 0x312bf560,
    	0x7f8d292f, 0xac7766f3, 0x19fadc21, 0x28d12941, 0x575c006e,
    	0xd014f9a8, 0xc9ee2589, 0xe13f0cc8, 0xb6630ca6 ]

    	# print(str(expanded))
    	# print(str(type(expanded)))
    	#
    	#
    	# w = d.keyExpansion( key, 16, 44 )
