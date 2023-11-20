#include "include/api/api.h"
#include "include/pong_lf/pong_lf.h"
#include "_pong_lf_main.h"
_pong_lf_main_main_self_t* new__pong_lf_main() {
    _pong_lf_main_main_self_t* self = (_pong_lf_main_main_self_t*)_lf_new_reactor(sizeof(_pong_lf_main_main_self_t));

    return self;
}
