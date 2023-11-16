#include "include/api/api.h"
#include "include/workers16/workers16.h"
#include "_workers16_main.h"
_workers16_main_main_self_t* new__workers16_main() {
    _workers16_main_main_self_t* self = (_workers16_main_main_self_t*)_lf_new_reactor(sizeof(_workers16_main_main_self_t));

    return self;
}
