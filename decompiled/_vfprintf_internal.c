// address: 0x1ecdc
int _charpad(unsigned int param1, __size32 param2, __size32 param3, __size32 param4, __size32 param6, __size32 param7, __size32 param8, __size32 param9, __size32 param10, __size32 param10) {
    __size32 *fp; 		// r30
    __size32 *fp_1; 		// r30{101}
    __size32 i0; 		// r24
    unsigned int i1; 		// r25
    unsigned int i2; 		// r26
    unsigned int i2_1; 		// r26{97}
    __size32 i3; 		// r27
    __size32 i3_1; 		// r27{98}
    __size32 i4; 		// r28
    __size32 i4_1; 		// r28{99}
    __size32 i5; 		// r29
    __size32 i5_1; 		// r29{100}
    __size32 i7; 		// r31
    __size32 i7_1; 		// r31{102}
    __size32 l0; 		// r16
    __size32 l1; 		// r17
    __size32 l2; 		// r18
    __size32 l3; 		// r19
    __size32 l4; 		// r20
    __size32 l5; 		// r21
    __size32 l6; 		// r22
    __size32 l7; 		// r23
    int o0; 		// r8
    __size32 *o6; 		// r14

    i2 = param1;
    i3 = param2;
    i4 = param3;
    i5 = param4;
    fp = o6;
    i7 = param10;
    i1 = param1;
    if (param1 != 0) {
        o0 = __stdio_fwrite(); /* Warning: also results in param6, param7, param8, param9, param10, i1, i2, i3, i4, i5, fp, i7 */
    }
    i2_1 = i2;
    i3_1 = i3;
    i4_1 = i4;
    i5_1 = i5;
    fp_1 = fp;
    i7_1 = i7;
    l0 = *fp_1;
    l1 = *(fp_1 + 4);
    l2 = *(fp_1 + 8);
    l3 = *(fp_1 + 12);
    l4 = *(fp_1 + 16);
    l5 = *(fp_1 + 20);
    l6 = *(fp_1 + 24);
    l7 = *(fp_1 + 28);
    i0 = *(fp_1 + 32);
    i2 = *(fp_1 + 40);
    i3 = *(fp_1 + 44);
    i4 = *(fp_1 + 48);
    i5 = *(fp_1 + 52);
    fp = *(fp_1 + 56);
    i7 = *(fp_1 + 60);
    return i2_1 - i1; /* WARNING: Also returning: g2 := param6, g3 := param7, g4 := param8, g5 := param9, g6 := param10, o1 := i1, o2 := i2_1, o3 := i3_1, o4 := i4_1, o5 := i5_1, o7 := i7_1, l0 := l0, l1 := l1, l2 := l2, l3 := l3, l4 := l4, l5 := l5, l6 := l6, l7 := l7, i0 := i0, i2 := i2, i3 := i3, i4 := i4, i5 := i5, fp := fp, i7 := i7 */
}

