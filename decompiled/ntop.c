// address: 0x23934
__size32 inet_ntop4(unsigned int param1) {
    unsigned int o0; 		// r8

    memset();
    o0 = __GI_strlen();
    __GI___errno_location();
    *(__size32*)o0_1 = 28;
    return 0;
}

// address: 0x23648
__size32 inet_pton4() {
    __size32 *fp; 		// r30
    __size32 *fp_1; 		// r30{204}
    unsigned int g1; 		// r1
    unsigned int g2; 		// r2
    unsigned int g3; 		// r3
    unsigned char *g4; 		// r4
    unsigned char *g4_1; 		// r4{40}
    __size32 g5; 		// r5
    __size32 g6; 		// r6
    __size32 i0; 		// r24
    char *i0_1; 		// r24{96}
    char *i0_2; 		// r24{26}
    __size32 i0_3; 		// r24{198}
    char *i0_4; 		// r24{170}
    __size32 i3; 		// r27
    __size32 i4; 		// r28
    __size32 i5; 		// r29
    __size32 i7; 		// r31
    __size32 l2; 		// r18
    __size32 l5; 		// r21
    unsigned char *local1; 		// g4_1{167}
    int local2; 		// o4_1{168}
    int local3; 		// o5_1{169}
    char *local4; 		// i0_4{170}
    unsigned char *local5; 		// g4{179}
    unsigned char *local6; 		// g4_1{213}
    char *o0; 		// r8
    int o4; 		// r12
    int o4_1; 		// r12{35}
    int o5; 		// r13
    int o5_1; 		// r13{38}
    __size32 *o6; 		// r14

    i0_2 = o0;
    fp = o6;
    o4_1 = 0;
    o5_1 = 0;
    g4_1 = (o6 - 12);
    local1 = g4_1;
    local2 = o4_1;
    local3 = o5_1;
    local4 = i0_2;
L13:
    g4_1 = local1;
    o4_1 = local2;
    o5_1 = local3;
    i0_4 = local4;
    g3 = (int) *i0_4;
    i0_1 = i0_4 + 1;
    local1 = g4_1;
    local1 = g4_1;
    local2 = o4_1;
    local3 = o5_1;
    local3 = o5_1;
    local4 = i0_1;
    local4 = i0_1;
    local4 = i0_1;
    local6 = g4_1;
    local6 = g4_1;
    local6 = g4_1;
    while (g3 != 0) {
        g1 = g3 - 48;
        if ((unsigned int)(g3 - 48) <= 9) {
            g1 = *(unsigned char*)g4_1;
            g2 = g1 * 8;
            g1 = g1 * 10 + g3 - 48;
            if (g1 > 255) {
L1:
                g4_1 = local6;
                local5 = g4_1;
                goto L0;
            } else {
                *(unsigned char*)g4_1 = (char) g1;
                if (o4_1 != 0) {
                    goto L13;
                }
                o5 = o5_1 + 1;
                o4_1 = 1;
                local2 = o4_1;
                local3 = o5;
                if (o5_1 + 1 <= 4) {
                    goto L13;
                }
                goto L1;
            }
            goto L0;
        }
        g4 = g4_1 + 1;
        local1 = g4;
        local6 = g4;
        local6 = g4;
        local6 = g4;
        if (g3 != 46) {
            goto L1;
        }
        o4 = 0;
        local2 = o4;
        if (o4_1 == 0 || o5_1 == 4) {
            goto L1;
        }
        *(__size8*)(g4_1 + 1) = 0;
L13:
        g4_1 = local1;
        o4_1 = local2;
        o5_1 = local3;
        i0_4 = local4;
        g3 = (int) *i0_4;
        i0_1 = i0_4 + 1;
        local1 = g4_1;
        local1 = g4_1;
        local2 = o4_1;
        local3 = o5_1;
        local3 = o5_1;
        local4 = i0_1;
        local4 = i0_1;
        local4 = i0_1;
        local6 = g4_1;
        local6 = g4_1;
        local6 = g4_1;
    }
    if (o5_1 <= 3) {
        goto L1;
    } else {
        i0 = 1;
        g1 = __GI_memcpy(); /* Warning: also results in g2, g3, g4, g5, g6 */
        local5 = g4;
    }
L0:
    g4 = local5;
    i0_3 = i0;
    fp_1 = fp;
    l2 = *(fp_1 + 8);
    l5 = *(fp_1 + 20);
    i0 = *(fp_1 + 32);
    i3 = *(fp_1 + 44);
    i4 = *(fp_1 + 48);
    i5 = *(fp_1 + 52);
    fp = *(fp_1 + 56);
    i7 = *(fp_1 + 60);
    return i0_3; /* WARNING: Also returning: g1 := g1, g2 := g2, g3 := g3, g4 := g4, g5 := g5, g6 := g6, l2 := l2, l5 := l5, i0 := i0, i3 := i3, i4 := i4, i5 := i5, fp := fp, i7 := i7 */
}

