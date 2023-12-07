#include "include/api/api.h"
#include "include/workers2/workers2.h"
#include "_workers2_main.h"
_workers2_main_main_self_t* new__workers2_main() {
    _workers2_main_main_self_t* self = (_workers2_main_main_self_t*)_lf_new_reactor(sizeof(_workers2_main_main_self_t));

    return self;
}
