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
# By Cl0wnPwn (iGio90)
######################################################

import math


salsa_const = [0x61707865, 0x6b206574, 0x3320646e, 0x79622D32]
sc_magic = [0x5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0xfc]


def _ror(val, bits, bit_size):
    return ((val & (2 ** bit_size - 1)) >> bits % bit_size) | \
           (val << (bit_size - (bits % bit_size)) & (2 ** bit_size - 1))


def __ROR4__(a, b):
    return _ror(a, b, 32)


def bic(a, b):
    r = a & ((-1 - b) << 8)
    r = (a & 0x00000ff) | r
    return r


def crypto_core(w, n, s, p):
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

    t4 = b
    t7 = l
    t8 = h
    t11 = i
    t12 = salsa_const[1]
    t13 = e
    t14 = j
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

    rounds = 0
    while rounds != 4:
        result.append(r10 & 0x000000ff)
        r10 = r10 >> 8
        rounds += 1
    rounds = 0
    while rounds != 4:
        result.append(r0 & 0x000000ff)
        r0 = r0 >> 8
        rounds += 1
    rounds = 0
    while rounds != 4:
        result.append(r8 & 0x000000ff)
        r8 = r8 >> 8
        rounds += 1
    rounds = 0
    while rounds != 4:
        result.append(t12 & 0x000000ff)
        t12 = t12 >> 8
        rounds += 1
    rounds = 0
    while rounds != 4:
        result.append(lr & 0x000000ff)
        lr = lr >> 8
        rounds += 1
    rounds = 0
    while rounds != 4:
        result.append(r11 & 0x000000ff)
        r11 = r11 >> 8
        rounds += 1
    rounds = 0
    while rounds != 4:
        result.append(t4 & 0x000000ff)
        t4 = t4 >> 8
        rounds += 1
    rounds = 0
    while rounds != 4:
        result.append(r6 & 0x000000ff)
        r6 = r6 >> 8
        rounds += 1
    if len(w) < 1:
        return bytes(result)

    w = bytes([0] * p) + w

    h_prop = h_set(result, n)

    result = []
    h_core_rounds = 0
    h_t_core_rounds = math.ceil(len(w) / 64)

    while h_core_rounds < h_t_core_rounds:
        r0 = h_prop[0]
        r1 = salsa_const[0]
        r0 = (r0 + r1) & 0xffffffff
        t1 = r0
        r0 = (r0 ^ h_core_rounds) & 0xffffffff
        r0 = (r0 << 0x10) & 0xffffffff

        h_res = h_core_a([t1, h_prop[4], r0, h_prop[0], 0, salsa_const[2], h_prop[1], h_prop[5], salsa_const[3],
                          h_prop[2], h_prop[8], h_prop[6], salsa_const[1], h_prop[3], h_prop[9], h_prop[7], t1])
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
        t1 = r1
        r0 = h_res[3]
        r1 = salsa_const[2]
        r0 = (r0 + r1) & 0xffffffff
        t2 = r0

        m_stracts = [
            h_stract(salsa_const[3], h_res[6]),
            h_stract(salsa_const[1], h_res[10]),
            h_stract(h_prop[0], h_res[13]),
            h_stract(h_prop[1], h_res[2]),
            h_stract(h_prop[2], h_res[5]),
            h_stract(h_prop[3], h_res[9]),
            h_stract(h_prop[4], h_res[8]),
            h_stract(h_prop[5], h_res[12]),
            h_stract(h_prop[6], h_res[1]),
            h_stract(h_prop[7], h_res[4]),
            h_stract(h_core_rounds, h_res[18]),
            h_stract(0, h_res[7]),
            h_stract(h_prop[8], h_res[11]),
            h_stract(h_prop[9], h_res[0])
        ]

        m_spack = []
        m_spack += h_spack(t1)
        m_spack += h_spack(t2)

        for x in m_stracts:
            m_spack += h_spack(x)

        rounds = 0
        ulim = 64 * h_core_rounds
        if ulim + 64 > len(w):
            df = (ulim + 64) - len(w)
            if df < 64:
                df = len(w)
            rounds = 0
            while df > 0 and ulim + rounds < len(w):
                s_a = m_spack[rounds]
                w_a = w[ulim + rounds]
                s_a = (w_a ^ s_a) & 0xff
                result.append(s_a)
                df -= 1
                rounds += 1

            s_a_1 = result[:0x10]
            w_a = [
                s_a_1[3] & 0xf,
                s_a_1[4] & 0xfc,
                s_a_1[7] & 0xf,
                s_a_1[8] & 0xfc,
                s_a_1[11] & 0xf,
                s_a_1[12] & 0xfc,
                s_a_1[15] & 0xf,
                ]

            w_le = len(w)
            w_lle_s = 0x20
            smul_values = []

            if len(w) >= 0x30:
                while w_lle_s < w_le:
                    s_a_2 = result[w_lle_s:w_lle_s + 0x10]
                    s_a_2.append(1)

                    if len(s_a_2) < 0x11:
                        while len(s_a_2) != 0x11:
                            s_a_2.append(0)

                    if len(smul_values) > 0:
                        t2 = 0
                        rounds = 0
                        while rounds != 0x11:
                            t1, t2 = h_aaas(smul_values[rounds], s_a_2[rounds], t2)
                            smul_values[rounds] = t1 & 0x000000ff
                            rounds += 1
                    else:
                        smul_values = s_a_2

                    mul_add_rounds = 0
                    mul_add_values = []
                    while mul_add_rounds != 0x11:
                        mul_add_values.append(h_mul_add_core(mul_add_rounds, s_a_1, smul_values, w_a))
                        mul_add_rounds += 1

                    rounds = 0
                    t2 = 0
                    while rounds != 0x10:
                        t1, t2 = h_aas(mul_add_values[rounds], t2)
                        rounds += 1

                    r1 = mul_add_values[0x10]
                    t2 = (t2 + r1) & 0xffffffff
                    r1 = t2 & 3
                    t2 = t2 >> 2
                    smul_values[rounds] = r1
                    t2 = t2 + (t2 << 2)

                    rounds = 0
                    while rounds != 0x10:
                        t1, t2 = h_aaas(smul_values[rounds], s_a_2[rounds], t2)
                        smul_values[rounds] = t1 & 0x000000ff
                        rounds += 1
                    w_lle_s += 0x10
            else:
                smul_values = [00] * 0x11

            t2 = 0
            s_a_1 = []
            rounds = 0
            while rounds != 0x11:
                t1, t2 = h_aaas(smul_values[rounds], sc_magic[rounds], t2)
                s_a_1.append(t1)
                rounds += 1

            rounds = 0
            r1 = 0xffffffff
            while rounds != 0x11:
                r2 = smul_values[rounds]
                r6 = s_a_1[rounds]
                r2 = (r2 ^ r6) & 0xffffffff
                r2 = r2 & r1
                r2 = (r2 ^ r6) & 0xffffffff
                smul_values[rounds] = r2
                rounds += 1

            s_a_2 = result[0x10:0x20]
            s_a_2.append(0)

            t2 = 0
            rounds = 0
            while rounds != 0x11:
                t1, t2 = h_aaas(smul_values[rounds], s_a_2[rounds], t2)
                smul_values[rounds] = t1
                rounds += 1

            r = []
            if p > 0x10:
                r = smul_values[:0x10]
            if len(w) - p >= 0x20:
                r += result[0x20:]
            return bytes(r)
        else:
            while rounds < 64:
                w_a = w[rounds + ulim]
                s_a = m_spack[rounds]
                s_a = (s_a ^ w_a) & 0xff
                result.append(s_a)
                rounds += 1

        h_core_rounds += 1


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
    r0 = (r1 + __ROR4__(r0, 24)) & 0xffffffff
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


def h_set(r, n):
    h_prop = []
    r2 = r[0x3]
    r1 = r[0x2]
    r1 = r1 | r2 << 8
    r1 = r1 << 8
    r0 = r[0x1]
    r1 = r1
    r0 = r0 + r1
    r1 = r[0]
    r2 = r[0x7]
    r0 = r1 | r0 << 8
    h_prop.append(r0)
    r1 = r[0x6]
    r0 = r[0x5]
    r1 = r1 | r2 << 8
    r0 = r0 | r1 << 8
    r1 = r[0x4]
    r2 = r[0xb]
    r0 = r1 | r0 << 8
    r1 = r[0xa]
    r1 = r1 | r2 << 8
    h_prop.append(r0)
    r0 = r[0x9]
    r0 = r0 | r1 << 8
    r1 = r[0x8]
    r2 = r[0xf]
    r0 = r1 | r0 << 8
    r1 = r[0xe]
    h_prop.append(r0)
    r0 = r[0xd]
    r1 = r1 | r2 << 8
    r0 = r0 | r1 << 8
    t1 = r0
    r1 = t1
    r2 = r[0x13]
    r0 = r[0xc]
    r0 = r0 | r1 << 8
    r1 = r[0x12]
    h_prop.append(r0)
    r0 = r[0x11]
    r1 = r1 | r2 << 8
    r0 = r0 | r1 << 8
    r1 = r[0x10]
    r0 = r1 | r0 << 8
    r1 = r[0x17]
    h_prop.append(r0)
    r0 = r[0x16]
    r1 = r1 << 8
    r0 |= r1
    r6 = r[0x15]
    r2 = r[0x14]
    r0 = r6 | r0 << 8
    r0 = r2 | r0 << 8
    h_prop.append(r0)
    r0 = r[0x1b]
    r0 = r0 << 8
    t1 = r0
    r0 = r[0x1a]
    r0 |= t1
    r6 = r[0x19]
    r1 = r[0x18]
    r0 = r6 | r0 << 8
    r0 = r1 | r0 << 8
    h_prop.append(r0)
    r0 = r[0x1f]
    r6 = r0 << 8
    r0 = r[0x1e]
    r0 |= r6
    r1 = r[0x1d]
    r2 = r[0x1c]
    r0 = r1 | r0 << 8
    r0 = r2 | r0 << 8
    h_prop.append(r0)
    r2 = n[0x13]
    r1 = n[0x12]
    r1 = r1 | r2 << 8
    r1 = r1 << 8
    t1 = r1
    r1 = r0 | r2
    r0 = r0 & r2
    r0 = (r0 - r1) & 0xffffffff
    r0 -= 1
    r2 = n[0x11]
    r1 = n[0x10]
    r0 = t1
    r0 |= r2
    r0 = r1 | r0 << 8
    h_prop.append(r0)
    r1 = n[0x17]
    r0 = n[0x16]
    r0 = r0 | r1 << 8
    r0 = r0 << 8
    r1 = n[0x15]
    r0 |= r1
    r2 = n[0x14]
    r0 = r2 | r0 << 8
    h_prop.append(r0)
    return h_prop


def h_stract(a, b):
    return ((a - 1) - ((-1 - b) & 0xffffffff)) & 0xffffffff


def h_spack(a):
    return [
        a & 0xff,
        a >> 8 & 0xff,
        a >> 16 & 0xff,
        a >> 24 & 0xff
    ]


def h_mul_add_core(r, s1, s2, w1):
    mul_a = h_mul_add_fields(r, s1, w1)
    mul_add = 0
    rounds = 0
    r_a = 0

    while rounds != 0x11:
        mul_add = h_mul_add(s2[rounds],
                            mul_a[rounds],
                            mul_add,
                            r_a)
        if mul_a[rounds] == 0 and r < 0x10:
            r_a = 1
        rounds += 1

    return mul_add


def h_mul_add(a, b, m, r):
    if r > 0:
        b = (((b + (b << 2)) & 0xfffffff) << 6) & 0xffffffff
    return (b * a + m) & 0xffffffff


def h_mul_add_fields(r, s1, w1):
    fields = [w1[6], s1[0xe], s1[0xd], w1[5], w1[4], s1[0xa],
              s1[9], w1[3], w1[2], s1[6], s1[5], w1[1], w1[0],
              s1[2], s1[1], s1[0]]
    f_s = []
    if r < 0x10:
        while r >= 0:
            a = fields.pop()
            f_s_a = [a]
            f_s = f_s_a + f_s
            r -= 1
    f_s.append(0)
    return f_s + fields


def h_aaas(a, b, c):
    b = (((c + a) & 0xffffffff + b) & 0xffffffff) & 0x000000ff
    c = c >> 8
    return b, c
