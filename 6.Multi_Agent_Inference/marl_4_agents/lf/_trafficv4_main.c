#include "include/api/api.h"
#include "include/trafficv4/trafficv4.h"
#include "_trafficv4_main.h"
_trafficv4_main_main_self_t* new__trafficv4_main() {
    _trafficv4_main_main_self_t* self = (_trafficv4_main_main_self_t*)_lf_new_reactor(sizeof(_trafficv4_main_main_self_t));

    return self;
}
