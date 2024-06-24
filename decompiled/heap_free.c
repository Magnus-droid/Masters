// address: 0x24dc4
void __heap_link_free_area(__size32 *param1, __size32 param2, __size32 param3, __size32 param4) {
    *(__size32*)(param2 + 8) = param3;
    *(__size32*)(param2 + 4) = param4;
    if (param3 == 0) {
        *(__size32*)param1 = param2;
    } else {
        *(__size32*)(param3 + 4) = param2;
    }
    return;
}

