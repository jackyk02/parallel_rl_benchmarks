#include "include/api/api.h"
#include "include/workers4/workers4.h"
#include "_workers4_main.h"
_workers4_main_main_self_t* new__workers4_main() {
    _workers4_main_main_self_t* self = (_workers4_main_main_self_t*)_lf_new_reactor(sizeof(_workers4_main_main_self_t));

    return self;
}
