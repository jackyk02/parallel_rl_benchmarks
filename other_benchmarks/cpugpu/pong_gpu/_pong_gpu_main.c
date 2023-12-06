#include "include/api/api.h"
#include "include/pong_gpu/pong_gpu.h"
#include "_pong_gpu_main.h"
_pong_gpu_main_main_self_t* new__pong_gpu_main() {
    _pong_gpu_main_main_self_t* self = (_pong_gpu_main_main_self_t*)_lf_new_reactor(sizeof(_pong_gpu_main_main_self_t));

    return self;
}
