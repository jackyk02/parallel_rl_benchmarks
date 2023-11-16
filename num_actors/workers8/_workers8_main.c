#include "include/api/api.h"
#include "include/workers8/workers8.h"
#include "_workers8_main.h"
_workers8_main_main_self_t* new__workers8_main() {
    _workers8_main_main_self_t* self = (_workers8_main_main_self_t*)_lf_new_reactor(sizeof(_workers8_main_main_self_t));

    return self;
}
