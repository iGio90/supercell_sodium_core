######################################################
# Did anyone thought i would left the cat mouse?
# I was just taking a good break! :)
# As usual, this has been done for free and for fun.
#
# This is just the core of the crypto,
# translated from arxan obfuscated ARM assembly.
# Other relevant code of the crypto are still sodium
# (i.e scalarmult, sigma const, etc.)
#
# The logic is not that far from what is known,
# however, owning the crypto core only won't be
# enough to create a client able to send and recv data.
#
# To be really fair, this has been opensourced
# as a poc that I'm still in the game,
# that i spent good times and learnt something new
# as usual. The whole crypto logic instead,
# won't be opensourced but don't get mad!
# you can still push yourself to the limit, break it
# and have some fun too. <3
#
# By cl0wnPwn (iGio90)
######################################################


salsa_const = [0x61707865, 0x6b206574, 0x3320646e, 0x79622D32]


def _ror(val, bits, bit_size):
    return ((val & (2 ** bit_size - 1)) >> bits % bit_size) | \
           (val << (bit_size - (bits % bit_size)) & (2 ** bit_size - 1))


def __ROR4__(a, b):
    return _ror(a, b, 32)


def bic(a, b):
    r = a & ((-1 - b) << 8)
    r = (a & 0x00000ff) | r
    return r


def crypto_core(w, n, s, p=False, debug=False):
    a = n[0xc] | (n[0xd] | (n[0xe] | n[0xf] << 8) << 8) << 8
    b = n[0x8] | (n[0x9] | (n[0xa] | n[0xb] << 8) << 8) << 8
    c = n[0x4] | (n[0x5] | (n[0x6] | n[0x7] << 8) << 8) << 8
    d = n[0x0] | (n[0x1] | (n[0x2] | n[0x3] << 8) << 8) << 8

    e = s[0x1c] | (s[0x1d] | (s[0x1e] | s[0x1f] << 8) << 8) << 8
    f = s[0x18] | (s[0x19] | (s[0x1a] | s[0x1b] << 8) << 8) << 8
    g = s[0x14] | (s[0x15] | (s[0x16] | s[0x17] << 8) << 8) << 8
    h = s[0x10] | (s[0x11] | (s[0x12] | s[0x13] << 8) << 8) << 8
    i = s[0xc] | (s[0xd] | (s[0xe] | s[0xf] << 8) << 8) << 8
    j = s[0x8] | (s[0x9] | (s[0xa] | s[0xb] << 8) << 8) << 8
    k = s[0x4] | (s[0x5] | (s[0x6] | s[0x7] << 8) << 8) << 8
    l = s[0x0] | (s[0x1] | (s[0x2] | s[0x3] << 8) << 8) << 8

    t1 = 0  # 0x1c
    t2 = 0  # 0x18
    t3 = 0  # 0x8
    t4 = b  # 0x3c
    t5 = 0  # 0xc
    t6 = 0  # 0x14
    t7 = l  # 0x2c
    t8 = h  # 0x30
    t9 = 0  # 0x4
    t10 = 0  # 0x10
    t11 = i  # 0x34
    t12 = salsa_const[1]  # 0x38
    t13 = e  # 0x24
    t14 = j  # 0x28
    result = []

    r0 = salsa_const[2]
    r5 = k
    r6 = a
    r8 = salsa_const[3]
    r9 = f
    r10 = salsa_const[0]
    r11 = c
    r12 = g
    lr = d
    rounds = 11

    while rounds > 0:
        r0 = (r0 + r5) & 0xffffffff
        r1 = (r0 ^ r11) & 0xffffffff
        r2 = (r12 + __ROR4__(r1, 16)) & 0xffffffff
        r3 = (r2 ^ r5) & 0xffffffff
        t1 = r3
        r0 = (r0 + __ROR4__(r3, 20)) & 0xffffffff
        t2 = r0
        r0 = (r0 ^ __ROR4__(r1, 16)) & 0xffffffff
        r3 = t14
        t3 = r0
        r4 = (r2 + __ROR4__(r0, 24)) & 0xffffffff
        r0 = t4
        r1 = (r3 + r8) & 0xffffffff
        r2 = r1 ^ r0
        t5 = r4
        r0 = (r9 + __ROR4__(r2, 16)) & 0xffffffff
        t6 = r0
        r0 = r0 ^ r3
        t14 = r0
        r9 = (r1 + __ROR4__(r0, 20)) & 0xffffffff
        r1 = t7
        r12 = (r9 ^ __ROR4__(r2, 16)) & 0xffffffff
        r0 = t8
        r2 = (r10 + r1) & 0xffffffff
        t9 = r12
        r3 = r2 ^ lr
        lr = (r0 + __ROR4__(r3, 16)) & 0xffffffff
        r0 = (lr ^ r1) & 0xffffffff
        r1 = (r2 + __ROR4__(r0, 20)) & 0xffffffff
        t10 = r1
        r10 = (r1 ^ __ROR4__(r3, 16)) & 0xffffffff
        lr = (lr + __ROR4__(r10, 24)) & 0xffffffff
        r2 = (lr ^ __ROR4__(r0, 20)) & 0xffffffff
        r0 = t11
        r1 = t12
        r3 = (r0 + r1) & 0xffffffff
        r1 = t13
        r8 = (r3 ^ r6) & 0xffffffff
        r11 = (r1 + __ROR4__(r8, 16)) & 0xffffffff
        r5 = (r11 ^ r0) & 0xffffffff
        r3 = (r3 + __ROR4__(r5, 20)) & 0xffffffff
        r6 = (r3 + __ROR4__(r2, 25)) & 0xffffffff
        r0 = (r6 ^ __ROR4__(r12, 24)) & 0xffffffff
        r1 = (r4 + __ROR4__(r0, 16)) & 0xffffffff
        r4 = t3
        r2 = (r1 ^ __ROR4__(r2, 25)) & 0xffffffff
        r6 = (r6 + __ROR4__(r2, 20)) & 0xffffffff
        t12 = r6
        r0 = (r6 ^ __ROR4__(r0, 16)) & 0xffffffff
        r12 = (r1 + __ROR4__(r0, 24)) & 0xffffffff
        r6 = __ROR4__(r0, 24) & 0xffffffff
        r0 = (r12 ^ __ROR4__(r2, 20)) & 0xffffffff
        r1 = (r3 ^ __ROR4__(r8, 16)) & 0xffffffff
        t4 = r6
        r0 = __ROR4__(r0, 25) & 0xffffffff
        t7 = r0
        r0 = (r11 + __ROR4__(r1, 24)) & 0xffffffff
        r2 = (r0 ^ __ROR4__(r5, 20)) & 0xffffffff
        r3 = (r9 + __ROR4__(r2, 25)) & 0xffffffff
        r5 = (r3 ^ __ROR4__(r4, 24)) & 0xffffffff
        r6 = (lr + __ROR4__(r5, 16)) & 0xffffffff
        r2 = (r6 ^ __ROR4__(r2, 25)) & 0xffffffff
        r8 = (r3 + __ROR4__(r2, 20)) & 0xffffffff
        r5 = (r8 ^ __ROR4__(r5, 16)) & 0xffffffff
        r3 = (r6 + __ROR4__(r5, 24)) & 0xffffffff
        t8 = r3
        r2 = (r3 ^ __ROR4__(r2, 20)) & 0xffffffff
        r3 = t9
        r11 = __ROR4__(r5, 24) & 0xffffffff
        r2 = __ROR4__(r2, 25) & 0xffffffff
        t11 = r2
        r2 = t6
        r2 = (r2 + __ROR4__(r3, 24)) & 0xffffffff
        r3 = t14
        r6 = (r2 ^ __ROR4__(r3, 20)) & 0xffffffff
        r3 = t2
        r5 = (r3 + __ROR4__(r6, 25)) & 0xffffffff
        r3 = (r5 ^ __ROR4__(r10, 24)) & 0xffffffff
        r4 = (r0 + __ROR4__(r3, 16)) & 0xffffffff
        r6 = (r4 ^ __ROR4__(r6, 25)) & 0xffffffff
        r0 = (r5 + __ROR4__(r6, 20)) & 0xffffffff
        r3 = (r0 ^ __ROR4__(r3, 16)) & 0xffffffff
        lr = __ROR4__(r3, 24) & 0xffffffff
        r3 = (r4 + __ROR4__(r3, 24)) & 0xffffffff
        t13 = r3
        r3 = (r3 ^ __ROR4__(r6, 20)) & 0xffffffff
        r4 = t5
        r3 = __ROR4__(r3, 25) & 0xffffffff
        t14 = r3
        r3 = t1
        r3 = (r4 ^ __ROR4__(r3, 20)) & 0xffffffff
        r4 = t10
        r4 = (r4 + __ROR4__(r3, 25)) & 0xffffffff
        r1 = (r4 ^ __ROR4__(r1, 24)) & 0xffffffff
        r2 = (r2 + __ROR4__(r1, 16)) & 0xffffffff
        r3 = (r2 ^ __ROR4__(r3, 25)) & 0xffffffff
        r10 = (r4 + __ROR4__(r3, 20)) & 0xffffffff
        r1 = (r10 ^ __ROR4__(r1, 16)) & 0xffffffff
        r9 = (r2 + __ROR4__(r1, 24)) & 0xffffffff
        r6 = __ROR4__(r1, 24) & 0xffffffff
        r1 = (r9 ^ __ROR4__(r3, 20)) & 0xffffffff
        r5 = __ROR4__(r1, 25) & 0xffffffff
        rounds -= 1

    r4 = t12
    r5 = t4
    r1 = 0
    while r1 != 4:
        result.append(r10 & 0x000000ff)
        r10 = r10 >> 8
        r1 += 1
    r2 = 0
    while r2 != 4:
        result.append(r0 & 0x000000ff)
        r0 = r0 >> 8
        r2 += 1
    r1 = 0
    while r1 != 4:
        result.append(r8 & 0x000000ff)
        r8 = r8 >> 8
        r1 += 1
    r1 = 0
    r2 = r5
    while r1 != 4:
        result.append(r4 & 0x000000ff)
        r4 = r4 >> 8
        r1 += 1
    r1 = 0
    while r1 != 4:
        result.append(lr & 0x000000ff)
        lr = lr >> 8
        r1 += 1
    r1 = 0
    while r1 != 4:
        result.append(r11 & 0x000000ff)
        r11 = r11 >> 8
        r1 += 1
    r1 = 0
    while r1 != 4:
        result.append(r2 & 0x000000ff)
        r2 = r2 >> 8
        r1 += 1
    r1 = 0
    while r1 != 4:
        result.append(r6 & 0x000000ff)
        r6 = r6 >> 8
        r1 += 1
    if not p:
        return bytes(result)

    print(bytes(result).hex())

    rrounds = 0

    # obfuscation will kill me. im gonna clean this up later as the first part
    r2 = result[0x3]
    r1 = result[0x2]
    r1 = r1 | r2 << 8
    r1 = r1 << 8
    r0 = result[0x1]
    r1 = r1
    r0 = r0 + r1
    r1 = result[0]
    r2 = result[0x7]
    r0 = r1 | r0 << 8
    t1 = r0  # 0x99b98288
    r1 = result[0x6]
    r0 = result[0x5]
    r1 = r1 | r2 << 8
    r0 = r0 | r1 << 8
    r1 = result[0x4]
    r2 = result[0xb]
    r0 = r1 | r0 << 8
    r1 = result[0xa]
    r1 = r1 | r2 << 8
    t2 = r0  # 0x93a6b858
    r0 = result[0x9]
    r2 = r1 << 8
    t3 = r2  # 0xa19700
    r0 = r0 | r1 << 8
    r2 = r2 ^ r1 << 8
    r2 = (r2 - r1 << 8) & 0xffffffff
    t4 = r2  # 0xff5e6900
    r1 = result[0x8]
    r2 = result[0xf]
    r0 = r1 | r0 << 8
    r1 = result[0xe]
    t5 = r0  # 0xa197ab2d
    r0 = result[0xd]
    r1 = r1 | r2 << 8
    r0 = r0 | r1 << 8
    t6 = r0  # 0x354a37
    r1 = t6
    r2 = result[0x13]
    r0 = result[0xc]
    r0 = r0 | r1 << 8
    r1 = result[0x12]
    t7 = r0  # 0x354a37e0
    r0 = result[0x11]
    r1 = r1 | r2 << 8
    r0 = r0 | r1 << 8
    t9 = r0  # 0xe324ce
    r1 = result[0x10]
    r0 = r1 | r0 << 8
    r1 = result[0x17]
    t10 = r0  # 0xe324ce5a
    r0 = result[0x16]
    r1 = r1 << 8
    r0 |= r1
    r6 = result[0x15]
    r2 = result[0x14]
    r0 = r6 | r0 << 8
    r0 = r2 | r0 << 8
    t11 = r0  # 0xdf7ec5a4
    r0 = result[0x1b]
    r0 = r0 << 8
    t12 = r0  # 0x6000
    r0 = result[0x1a]
    r0 |= t12
    r6 = result[0x19]
    r1 = result[0x18]
    r0 = r6 | r0 << 8
    r0 = r1 | r0 << 8
    t13 = r0  # 0x60f0b806
    r0 = result[0x1f]
    r6 = r0 << 8
    r0 = result[0x1e]
    r0 |= r6
    r1 = result[0x1d]
    r2 = result[0x1c]
    r0 = r1 | r0 << 8
    r0 = r2 | r0 << 8
    t14 = r0  # 0x4db81a0e
    r2 = n[0x13]
    r1 = n[0x12]
    r1 = r1 | r2 << 8
    r1 = r1 << 8
    t15 = r1  # 0xd0a200
    r1 = r0 | r2
    r0 = r0 & r2
    r0 = (r0 - r1) & 0xffffffff
    r0 -= 1
    pd1 = r0   # 0xb247e521
    r2 = n[0x11]
    r1 = n[0x10]
    r0 = t15
    r0 |= r2
    r0 = r1 | r0 << 8
    t16 = r0  # 0xd0a268df
    r1 = n[0x17]
    r0 = n[0x16]
    r0 = r0 | r1 << 8
    r0 = r0 << 8
    r1 = n[0x15]
    r0 |= r1
    r2 = n[0x14]
    r0 = r2 | r0 << 8
    t17 = r0  # 0x537f99ea

    r0 = t1
    r1 = salsa_const[0]
    r0 = (r0 + r1) & 0xffffffff
    t18 = r0  # 0xfb29faed
    r0 = (r0 << 0x10) & 0xffffffff
    r1 = t18 >> 16
    r3 = t10
    r0 = r1 | r0
    r6 = t1
    r1 = (r0 + r3) & 0xffffffff
    r2 = t18
    r3 = r1 ^ r6
    r2 = (r2 + __ROR4__(r3, 20)) & 0xffffffff
    t19 = r2  # 0xafdaaf67
    r0 ^= r2
    r2 = r0 >> 0x18
    t20 = r2  # 0x55
    r2 = (r0 << 8) & 0xffffffff
    t21 = r2  # 0x37544e00
    r2 = t20
    r2 = (-1 - r2) & 0xffffffff
    r0 = bic(r2, r0)
    r2 = rrounds
    r0 = (-1 - r0) & 0xffffffff
    t22 = r0  # 0x37544e55
    r0 = (r0 + r1) & 0xffffffff
    t23 = r0  # 0x156717d8
    r0 = (r0 ^ __ROR4__(r3, 20)) & 0xffffffff
    r1 = salsa_const[2]
    r0 = __ROR4__(r0, 0x19)
    t24 = r0  # 0xebd1d150
    r0 = t2
    r3 = (r0 + r1) & 0xffffffff
    r6 = r3 ^ r2
    r5 = (r6 << 0x10) & 0xffffffff

    r0 = t11
    r2 = (r5 | __ROR4__(r6, 16)) & 0xffffffff
    r1 = t2
    r0 = (r0 + r2) & 0xffffffff
    r1 = (r1 ^ r0) & 0xffffffff
    r3 = (r3 + __ROR4__(r1, 20)) & 0xffffffff
    t25 = r3  # 0xfa0a53c4
    r2 = (r2 ^ r3) & 0xffffffff
    r0 = (r0 + __ROR4__(r2, 24)) & 0xffffffff
    t26 = r0  # 0xc8da9051
    r0 = (r0 ^ __ROR4__(r1, 20)) & 0xffffffff
    r1 = salsa_const[3]
    r3 = __ROR4__(r2, 0x18)
    r0 = __ROR4__(r0, 0x19)
    t27 = r3  # 0xcc9503e6
    t28 = r0  # 0xccd357fd
    r0 = t5
    r0 = (r0 + r1) & 0xffffffff
    r1 = t16
    t29 = r0  # 0x1af9d85f
    r0 = r0 ^ r1
    t30 = r0  # 0xca5bb080
    r0 = (r0 << 0x10) & 0xffffffff

    r1 = t30 >> 16
    r3 = t13
    r0 |= r1
    r6 = t5
    r1 = (r0 + r3) & 0xffffffff
    r2 = t29
    r3 = (r1 ^ r6) & 0xffffffff
    r2 = (r2 + __ROR4__(r3, 20)) & 0xffffffff
    t31 = r2  # 0x7d8ea36d
    r0 = (r0 ^ r2) & 0xffffffff
    r2 = __ROR4__(r0, 0x18)
    r0 = (r1 + __ROR4__(r0, 24)) & 0xffffffff
    t32 = r0  # 0x1fdab92e
    r0 = (r0 ^ __ROR4__(r3, 20)) & 0xffffffff
    r1 = salsa_const[1]
    r0 = __ROR4__(r0, 0x19)
    t33 = r2  # 0xe6936cd
    t34 = r0  # 0xa739103e
    r0 = t7
    r0 = (r0 + r1) & 0xffffffff
    r1 = t17
    t35 = r0  # 0xa06a9d54
    r0 = (r0 ^ r1) & 0xffffffff
    t36 = r0  # 0xf31504be
    r0 = (r0 << 0x10) & 0xffffffff
    t37 = r0  # 0x4be0000

    r2 = t37
    r1 = t36 >> 16
    r6 = t14
    r5 = t7
    r1 = (r1 | r2) & 0xffffffff
    r2 = (r1 + r6) & 0xffffffff
    r3 = (r2 ^ r5) & 0xffffffff
    r0 = t35
    r3 = __ROR4__(r3, 0x14)

    r0 = (r0 + r3) & 0xffffffff
    t38 = r0  # 0x7416d3c7
    r0 = (r0 ^ r1) & 0xffffffff
    r1 = (r2 + __ROR4__(r0, 24)) & 0xffffffff
    t39 = r1  # 0xfa97df93
    r1 = (r1 ^ r3) & 0xffffffff
    r2 = t28
    r1 = __ROR4__(r1, 0x19)
    t40 = r1  # 0x9df4f014
    r1 = t19
    r1 = (r1 + r2) & 0xffffffff
    t41 = r1  # 0x7cae0764
    r0 = (r1 ^ __ROR4__(r0, 24)) & 0xffffffff
    r0 = __ROR4__(r0, 0x10)
    t42 = r0  # 0xd514d48e

    r0 = t32
    r1 = t42
    r0 = (r0 + r1) & 0xffffffff
    t43 = r0  # 0xf4ef8dbc
    r0 = t28
    r1 = t43
    r0 = (r0 ^ r1) & 0xffffffff
    r1 = __ROR4__(r0, 0x14)
    t44 = r1  # 0xcda41383
    r1 = t41
    r0 = (r1 + __ROR4__(r0, 20)) & 0xffffffff
    r1 = t42
    t45 = r0  # 0x4a521ae7
    r0 = (r0 ^ r1) & 0xffffffff
    r0 = __ROR4__(r0, 0x18)
    t46 = r0  # 0x46ce699f

    r1 = t43
    r0 = (r0 + r1) & 0xffffffff
    r1 = t44
    t47 = r0  # 0x3bbdf75b
    r0 = (r0 ^ r1) & 0xffffffff
    r0 = __ROR4__(r0, 0x19)
    t48 = r0  # 0xcf26c7b

    r0 = t34
    r2 = t22
    r1 = t25
    r3 = t22
    r0 = (r0 + r1) & 0xffffffff
    r1 = t39
    r6 = (r3 + r0) & 0xffffffff
    r3 = r3 | r0
    r2 = t34
    r6 = -(r6 - (r3 << 1))
    t49 = r0  # 0xa1436402
    r3 = (r1 + __ROR4__(r6, 16)) & 0xffffffff
    r5 = __ROR4__(r6, 0x10)
    r1 = (r3 ^ r2) & 0xffffffff
    r0 = (r0 + __ROR4__(r1, 20)) & 0xffffffff
    t49_a = r0  # 0x79cac3f
    r6 = __ROR4__(r1, 0x14)

    r0 = (r0 ^ r5) & 0xffffffff
    r1 = __ROR4__(r0, 0x18)
    r0 = (r3 + __ROR4__(r0, 24)) & 0xffffffff
    t50 = r0  # 0xf0299dd7
    r0 = (r0 ^ r6) & 0xffffffff
    t51 = r1  # 0xcb3a282d
    r0 = __ROR4__(r0, 0x19)
    t52 = r0  # 0x386af54b
    r0 = t31
    r1 = t40
    r2 = t27
    r0 = (r0 + r1) & 0xffffffff
    r1 = (r2 ^ r0) & 0xffffffff
    r2 = __ROR4__(r1, 0x10)
    t53 = r2  # 0x9067d716
    r2 = t23
    r1 = (r2 + __ROR4__(r1, 16)) & 0xffffffff
    t54 = r1  # 0xa5ceeeee
    r1 = t40
    r2 = t54
    r1 = (r1 ^ r2) & 0xffffffff
    r2 = __ROR4__(r1, 0x14)
    r0 = (r0 + __ROR4__(r1, 20)) & 0xffffffff
    t55 = r2  # 0xa1efa383
    t56 = r0  # 0xbd733704

    r1 = t53
    r0 = (r0 ^ r1) & 0xffffffff
    r1 = __ROR4__(r0, 0x18)
    t57 = r1  # 0x14e0122d
    r1 = t54
    r0 = (r1 +__ROR4__(r0, 24)) & 0xffffffff
    r1 = t55
    t58 = r0  # 0xbaaf011b
    r0 = (r0 ^ r1) & 0xffffffff
    r0 = __ROR4__(r0, 0x19)
    t59 = r0  # 0xa0514c0d

    r0 = t38
    r1 = t24
    r2 = t26
    r0 = (r0 + r1) & 0xffffffff
    t60 = r0  # 0x5fe8a517
    r0 = t33
    r1 = t60
    r0 = (r0 ^ r1) & 0xffffffff
    r1 = __ROR4__(r0, 0x10)
    r0 = (r2 + __ROR4__(r0, 16)) & 0xffffffff
    t61 = r0  # 0x5cb4e1d2
    r0 = t24
    t62 = r1  # 0x93da5181
    r1 = t61
    r0 = (r0 ^ r1) & 0xffffffff
    t63 = r0  # 0xb7653082

    r1 = t63
    r2 = t60
    r1 = r1 >> 0x14
    r0 = (r1 | r0 << 12) & 0xffffffff
    r1 = (r0 + r2) & 0xffffffff
    r2 = t62
    t64 = r1  # 0xb2f0d08d

    r1 = (r1 ^ r2) & 0xffffffff
    r2 = r1 >> 0x18
    t65 = r2  # 0x21
    r2 = r1 << 8 & 0xffffffff
    t66 = r2  # 0x2a810c00
    r2 = t65
    r2 = bic(r2, r1)
    r1 = (r2 + (r1 << 8)) & 0xffffffff
    r2 = t61
    t67 = r1  # 0x2a810c21
    r1 = (r1 + r2) & 0xffffffff
    r0 = (r0 ^ r1) & 0xffffffff
    t68 = r1  # 0x8735edf3
    r0 = __ROR4__(r0, 0x19)
    t69 = r0  # 0x1ee342ea

    r1 = t45
    r0 = (r0 + r1) & 0xffffffff
    t70 = r0  # 0x69355dd1
    r1 = t51
    r0 = (r0 ^ r1) & 0xffffffff
    t71 = r0  # 0xa20f75fc
    r0 = (r0 << 0x10) & 0xffffffff


    r1 = t71 >> 16
    r3 = t58
    r0 |= r1
    r6 = t69
    r1 = (r0 + r3) & 0xffffffff
    r2 = t70
    r3 = r1 ^ r6
    r2 = (r2 + __ROR4__(r3, 20)) & 0xffffffff
    t73 = r2  # 0xf75160b5
    r0 ^= r2
    r2 = r0 >> 0x18
    t74 = r2  # 0x82
    r2 = (r0 << 8) & 0xffffffff
    t75 = r2  # 0xadc2ba00
    r2 = t74
    r2 = (-1 - r2) & 0xffffffff
    r0 = bic(r2, r0)
    r2 = t57
    r0 = (-1 - r0) & 0xffffffff
    t76 = r0  # 0xadc2ba82
    r0 = (r0 + r1) & 0xffffffff
    t77 = r0  # 0xde6e5dac
    r0 = (r0 ^ __ROR4__(r3, 20)) & 0xffffffff
    r1 = t49_a
    r0 = __ROR4__(r0, 0x19)
    t78 = r0  # 0x392fa428
    r0 = t48
    r3 = (r0 + r1) & 0xffffffff
    r6 = r3 ^ r2
    r5 = (r6 << 0x10) & 0xffffffff

    r0 = t68
    r2 = (r5 | __ROR4__(r6, 16)) & 0xffffffff
    r1 = t48
    r0 = (r0 + r2) & 0xffffffff
    r1 = (r1 ^ r0) & 0xffffffff
    r3 = (r3 + __ROR4__(r1, 20)) & 0xffffffff
    t79 = r3  # 0xfcb0b28d
    r2 = (r2 ^ r3) & 0xffffffff
    r0 = (r0 + __ROR4__(r2, 24)) & 0xffffffff
    t80 = r0  # 0xb97fd158
    r0 = (r0 ^ __ROR4__(r1, 20)) & 0xffffffff
    r1 = t56
    r3 = __ROR4__(r2, 0x18)
    r0 = __ROR4__(r0, 0x19)
    t81 = r3  # 0x27b2e2f6
    t82 = r0  # 0xaf2445a8
    r0 = t52
    r0 = (r0 + r1) & 0xffffffff
    r1 = t67
    t83 = r0  # 0xf5de2c4f
    r0 = r0 ^ r1
    t84 = r0  # 0xdf5f206e
    r0 = (r0 << 0x10) & 0xffffffff

    r1 = t84 >> 16
    r3 = t47
    r0 |= r1
    r6 = t52
    r1 = (r0 + r3) & 0xffffffff
    r2 = t83
    r3 = (r1 ^ r6) & 0xffffffff
    r2 = (r2 + __ROR4__(r3, 20)) & 0xffffffff
    t85 = r2  # 0x581d4293
    r0 = (r0 ^ r2) & 0xffffffff
    r2 = __ROR4__(r0, 0x18)
    r0 = (r1 + __ROR4__(r0, 24)) & 0xffffffff
    t86 = r0  # 0xcfcaa332
    r0 = (r0 ^ __ROR4__(r3, 20)) & 0xffffffff
    r1 = t64
    r0 = __ROR4__(r0, 0x19)
    t87 = r2  # 0x739dcc78
    t88 = r0  # 0xfadabb56
    r0 = t59
    r0 = (r0 + r1) & 0xffffffff
    r1 = t46
    t89 = r0  # 0x53421c9a
    r0 = (r0 ^ r1) & 0xffffffff
    t90 = r0  # 0x158c7505
    r0 = (r0 << 0x10) & 0xffffffff
    t91 = r0  # 0x75050000

    r2 = t91
    r1 = t90 >> 16
    r6 = t50
    r5 = t59
    r1 = (r1 | r2) & 0xffffffff
    r2 = (r1 + r6) & 0xffffffff
    r3 = (r2 ^ r5) & 0xffffffff
    r0 = t89
    r3 = __ROR4__(r3, 0x14)

    r0 = (r0 + r3) & 0xffffffff
    t92 = r0  # 0x533908f1
    r0 = (r0 ^ r1) & 0xffffffff
    r1 = (r2 + __ROR4__(r0, 24)) & 0xffffffff
    t93 = r1  # 0xa14c3089
    r1 = (r1 ^ r3) & 0xffffffff
    r2 = t82
    r1 = __ROR4__(r1, 0x19)
    t94 = r1  # 0x5d6e6f2f
    r1 = t73
    r1 = (r1 + r2) & 0xffffffff
    t95 = r1  # 0xa675a65d
    r0 = (r1 ^ __ROR4__(r0, 24)) & 0xffffffff
    r0 = __ROR4__(r0, 0x10)
    t96 = r0  # 0xdb7b9a68

    r0 = t86
    r1 = t96
    r0 = (r0 + r1) & 0xffffffff
    t97 = r0  # 0xab463d9a
    r0 = t82
    r1 = t97
    r0 = (r0 ^ r1) & 0xffffffff
    r1 = __ROR4__(r0, 0x14)
    t98 = r1  # 0x27832046
    r1 = t95
    r0 = (r1 + __ROR4__(r0, 20)) & 0xffffffff
    r1 = t96
    t99 = r0  # 0xcdf8c6a3
    r0 = (r0 ^ r1) & 0xffffffff
    r0 = __ROR4__(r0, 0x18)
    t100 = r0  # 0x835ccb16