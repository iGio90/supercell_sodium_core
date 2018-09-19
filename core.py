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
    t1 = r0
    r1 = result[0x6]
    r0 = result[0x5]
    r1 = r1 | r2 << 8
    r0 = r0 | r1 << 8
    r1 = result[0x4]
    r2 = result[0xb]
    r0 = r1 | r0 << 8
    r1 = result[0xa]
    r1 = r1 | r2 << 8
    t2 = r0
    r0 = result[0x9]
    r2 = r1 << 8
    t3 = r2
    r0 = r0 | r1 << 8
    r2 = r2 ^ r1 << 8
    r2 = (r2 - r1 << 8) & 0xffffffff
    t4 = r2
    r1 = result[0x8]
    r2 = result[0xf]
    r0 = r1 | r0 << 8
    r1 = result[0xe]
    t5 = r0
    r0 = result[0xd]
    r1 = r1 | r2 << 8
    r0 = r0 | r1 << 8
    t6 = r0
    r1 = t6
    r2 = result[0x13]
    r0 = result[0xc]
    r0 = r0 | r1 << 8
    r1 = result[0x12]
    t7 = r0
    r0 = result[0x11]
    r1 = r1 | r2 << 8
    r0 = r0 | r1 << 8
    t9 = r0
    r1 = result[0x10]
    r0 = r1 | r0 << 8
    r1 = result[0x17]
    t10 = r0
    r0 = result[0x16]
    r1 = r1 << 8
    r0 |= r1
    r6 = result[0x15]
    r2 = result[0x14]
    r0 = r6 | r0 << 8
    r0 = r2 | r0 << 8
    t11 = r0
    r0 = result[0x1b]
    r0 = r0 << 8
    t12 = r0
    r0 = result[0x1a]
    r0 |= t12
    r6 = result[0x19]
    r1 = result[0x18]
    r0 = r6 | r0 << 8
    r0 = r1 | r0 << 8
    t13 = r0
    r0 = result[0x1f]
    r6 = r0 << 8
    r0 = result[0x1e]
    r0 |= r6
    r1 = result[0x1d]
    r2 = result[0x1c]
    r0 = r1 | r0 << 8
    r0 = r2 | r0 << 8
    t14 = r0
    r2 = n[0x13]
    r1 = n[0x12]
    r1 = r1 | r2 << 8
    r1 = r1 << 8
    t15 = r1
    r1 = r0 | r2
    r0 = r0 & r2
    r0 = (r0 - r1) & 0xffffffff
    r0 -= 1
    pd1 = r0
    r2 = n[0x11]
    r1 = n[0x10]
    r0 = t15
    r0 |= r2
    r0 = r1 | r0 << 8
    t16 = r0
    r1 = n[0x17]
    r0 = n[0x16]
    r0 = r0 | r1 << 8
    r0 = r0 << 8
    r1 = n[0x15]
    r0 |= r1
    r2 = n[0x14]
    r0 = r2 | r0 << 8
    t17 = r0

    r0 = t1
    r1 = salsa_const[0]
    r0 = (r0 + r1) & 0xffffffff
    t18 = r0
    r0 = (r0 << 0x10) & 0xffffffff

    h_res = h_core_a([t18, t10, r0, t1, 0, salsa_const[2], t2, t11, salsa_const[3],
                      t5, t16, t13, salsa_const[1], t7, t17, t14, t18])

    rounds = 8
    while rounds > 0:
        h_res = h_core_a([h_res[15], h_res[8], h_res[16], h_res[13],
                          h_res[7], h_res[3], h_res[2], h_res[12], h_res[6],
                          h_res[5], h_res[11], h_res[1], h_res[10], h_res[9],
                          h_res[0], h_res[4], h_res[14]])
        rounds -= 1

    r1 = h_res[17]
    r2 = salsa_const[0]
    r1 = (r1 + r2) & 0xffffffff
    c_1 = r1
    r0 = h_res[3]
    r1 = salsa_const[2]
    r0 = (r0 + r1) & 0xffffffff
    c_2 = r0

    m_stracts = [
        h_stract(salsa_const[3], h_res[6]),
        h_stract(salsa_const[1], h_res[10]),
        h_stract(t1, h_res[13]),
        h_stract(t2, h_res[2]),
        h_stract(t5, h_res[5]),
        h_stract(t7, h_res[9]),
        h_stract(t10, h_res[8]),
        h_stract(t11, h_res[12]),
        h_stract(t13, h_res[1]),
        h_stract(t14, h_res[4]),
        h_stract(0, h_res[18]),
        h_stract(0, h_res[7]),
        h_stract(t16, h_res[11]),
        h_stract(t17, h_res[0])
    ]

    m_spack = [
        h_spack(c_1),
        h_spack(c_2),
        h_spack(m_stracts[0]),
        h_spack(m_stracts[1]),
        h_spack(m_stracts[2]),
        h_spack(m_stracts[3]),
        h_spack(m_stracts[4]),
        h_spack(m_stracts[5]),
        h_spack(m_stracts[6]),
        h_spack(m_stracts[7]),
        h_spack(m_stracts[8]),
        h_spack(m_stracts[9]),
        h_spack(m_stracts[10]),
        h_spack(m_stracts[11]),
        h_spack(m_stracts[12]),
        h_spack(m_stracts[13]),
    ]


def h_core_a(a):
    r = [0] * 19
    s = [0] * 31

    r1 = a[0] >> 16
    r3 = a[1]
    r0 = r1 | a[2]
    r6 = a[3]
    r1 = (r0 + r3) & 0xffffffff
    r2 = a[16]
    r3 = r1 ^ r6
    r2 = (r2 + __ROR4__(r3, 20)) & 0xffffffff
    s[0] = r2
    r0 ^= r2
    r2 = r0 >> 0x18
    r2 = (-1 - r2) & 0xffffffff
    r0 = bic(r2, r0)
    r2 = a[4]
    r0 = (-1 - r0) & 0xffffffff
    s[1] = r0
    r0 = (r0 + r1) & 0xffffffff
    s[2] = r0
    r0 = (r0 ^ __ROR4__(r3, 20)) & 0xffffffff
    r1 = a[5]
    r0 = __ROR4__(r0, 0x19)
    s[7] = r0
    r0 = a[6]
    r3 = (r0 + r1) & 0xffffffff
    r6 = r3 ^ r2
    r5 = (r6 << 0x10) & 0xffffffff

    r0 = a[7]
    r2 = (r5 | __ROR4__(r6, 16)) & 0xffffffff
    r1 = a[6]
    r0 = (r0 + r2) & 0xffffffff
    r1 = (r1 ^ r0) & 0xffffffff
    r3 = (r3 + __ROR4__(r1, 20)) & 0xffffffff
    s[3] = r3
    r2 = (r2 ^ r3) & 0xffffffff
    r0 = (r0 + __ROR4__(r2, 24)) & 0xffffffff
    s[4] = r0
    r0 = (r0 ^ __ROR4__(r1, 20)) & 0xffffffff
    r1 = a[8]
    r3 = __ROR4__(r2, 0x18)
    r0 = __ROR4__(r0, 0x19)
    s[9] = r3
    s[10] = r0
    r0 = a[9]
    r0 = (r0 + r1) & 0xffffffff
    r1 = a[10]
    s[5] = r0
    r0 = r0 ^ r1
    s[6] = r0
    r0 = (r0 << 0x10) & 0xffffffff

    r1 = s[6] >> 16
    r3 = a[11]
    r0 |= r1
    r6 = a[9]
    r1 = (r0 + r3) & 0xffffffff
    r2 = s[5]
    r3 = (r1 ^ r6) & 0xffffffff
    r2 = (r2 + __ROR4__(r3, 20)) & 0xffffffff
    s[8] = r2
    r0 = (r0 ^ r2) & 0xffffffff
    r2 = __ROR4__(r0, 0x18)
    r0 = (r1 + __ROR4__(r0, 24)) & 0xffffffff
    s[11] = r0
    r0 = (r0 ^ __ROR4__(r3, 20)) & 0xffffffff
    r1 = a[12]
    r0 = __ROR4__(r0, 0x19)
    s[12] = r2
    s[13] = r0
    r0 = a[13]
    r0 = (r0 + r1) & 0xffffffff
    r1 = a[14]
    s[14] = r0
    r0 = (r0 ^ r1) & 0xffffffff
    s[15] = r0
    r0 = (r0 << 0x10) & 0xffffffff

    r2 = r0
    r1 = s[15] >> 16
    r6 = a[15]
    r5 = a[13]
    r1 = (r1 | r2) & 0xffffffff
    r2 = (r1 + r6) & 0xffffffff
    r3 = (r2 ^ r5) & 0xffffffff
    r0 = s[14]
    r3 = __ROR4__(r3, 0x14)

    r0 = (r0 + r3) & 0xffffffff
    s[16] = r0
    r0 = (r0 ^ r1) & 0xffffffff
    r1 = (r2 + __ROR4__(r0, 24)) & 0xffffffff
    s[17] = r1
    r1 = (r1 ^ r3) & 0xffffffff
    r2 = s[10]
    r1 = __ROR4__(r1, 0x19)
    s[18] = r1
    r1 = s[0]
    r1 = (r1 + r2) & 0xffffffff
    s[19] = r1
    r0 = (r1 ^ __ROR4__(r0, 24)) & 0xffffffff
    r0 = __ROR4__(r0, 0x10)
    s[20] = r0

    r0 = s[11]
    r1 = s[20]
    r0 = (r0 + r1) & 0xffffffff
    s[21] = r0
    r0 = s[10]
    r1 = s[21]
    r0 = (r0 ^ r1) & 0xffffffff
    r1 = __ROR4__(r0, 0x14)
    s[22] = r1
    r1 = s[19]
    r0 = (r1 + __ROR4__(r0, 20)) & 0xffffffff
    r1 = s[20]
    s[23] = r0
    r0 = (r0 ^ r1) & 0xffffffff
    r0 = __ROR4__(r0, 0x18)
    r[0] = r0

    r1 = s[21]
    r0 = (r0 + r1) & 0xffffffff
    r1 = s[22]
    r[1] = r0
    r0 = (r0 ^ r1) & 0xffffffff
    r0 = __ROR4__(r0, 0x19)
    r[2] = r0

    r0 = s[13]
    r1 = s[3]
    r3 = s[1]
    r0 = (r0 + r1) & 0xffffffff
    r1 = s[17]
    r6 = (r3 + r0) & 0xffffffff
    r3 = r3 | r0
    r2 = s[13]
    r6 = -(r6 - (r3 << 1))
    r3 = (r1 + __ROR4__(r6, 16)) & 0xffffffff
    r5 = __ROR4__(r6, 0x10)
    r1 = (r3 ^ r2) & 0xffffffff
    r0 = (r0 + __ROR4__(r1, 20)) & 0xffffffff
    r[3] = r0
    r6 = __ROR4__(r1, 0x14)

    r0 = (r0 ^ r5) & 0xffffffff
    r1 = __ROR4__(r0, 0x18)
    r0 = (r3 + __ROR4__(r0, 24)) & 0xffffffff
    r[4] = r0
    r0 = (r0 ^ r6) & 0xffffffff
    s[24] = r1
    r0 = __ROR4__(r0, 0x19)
    r[5] = r0
    r0 = s[8]
    r1 = s[18]
    r2 = s[9]
    r0 = (r0 + r1) & 0xffffffff
    r1 = (r2 ^ r0) & 0xffffffff
    r2 = __ROR4__(r1, 0x10)
    s[25] = r2
    r2 = s[2]
    r1 = (r2 + __ROR4__(r1, 16)) & 0xffffffff
    s[26] = r1
    r1 = s[18]
    r2 = s[26]
    r1 = (r1 ^ r2) & 0xffffffff
    r2 = __ROR4__(r1, 0x14)
    r0 = (r0 + __ROR4__(r1, 20)) & 0xffffffff
    s[27] = r2
    r[6] = r0

    r1 = s[25]
    r0 = (r0 ^ r1) & 0xffffffff
    r1 = __ROR4__(r0, 0x18)
    r[7] = r1
    r1 = s[26]
    r0 = (r1 +__ROR4__(r0, 24)) & 0xffffffff
    r1 = s[27]
    r[8] = r0
    r0 = (r0 ^ r1) & 0xffffffff
    r0 = __ROR4__(r0, 0x19)
    r[9] = r0

    r0 = s[16]
    r1 = s[7]
    r2 = s[4]
    r0 = (r0 + r1) & 0xffffffff
    s[28] = r0
    r0 = s[12]
    r1 = s[28]
    r0 = (r0 ^ r1) & 0xffffffff
    r1 = __ROR4__(r0, 0x10)
    r0 = (r2 + __ROR4__(r0, 16)) & 0xffffffff
    s[29] = r0
    r0 = s[7]
    s[30] = r1
    r1 = s[29]
    r0 = (r0 ^ r1) & 0xffffffff

    r1 = r0
    r2 = s[28]
    r1 = r1 >> 0x14
    r0 = (r1 | r0 << 12) & 0xffffffff
    r1 = (r0 + r2) & 0xffffffff
    r2 = s[30]
    r[10] = r1

    r1 = (r1 ^ r2) & 0xffffffff
    r2 = r1 >> 0x18
    r2 = bic(r2, r1)
    r1 = (r2 + (r1 << 8)) & 0xffffffff
    r2 = s[29]
    r[11] = r1
    r1 = (r1 + r2) & 0xffffffff
    r0 = (r0 ^ r1) & 0xffffffff
    r[12] = r1
    r0 = __ROR4__(r0, 0x19)
    r[13] = r0

    r1 = s[23]
    r0 = (r0 + r1) & 0xffffffff
    r[14] = r0
    r1 = s[24]
    r0 = (r0 ^ r1) & 0xffffffff
    r[15] = r0
    r[16] = (r0 << 0x10) & 0xffffffff
    r[17] = s[23]
    r[18] = s[24]
    return r


def h_stract(a, b):
    r2 = b
    r3 = a
    r2 = (-1 - r2) & 0xffffffff
    r3 -= 1
    r2 = r3 - r2
    return r2 & 0xffffffff


def h_spack(a):
    return [
        a & 0xff,
        a >> 8 & 0xff,
        a >> 16 & 0xff,
        a >> 24 & 0xff
    ]
