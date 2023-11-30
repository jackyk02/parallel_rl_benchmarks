#include "include/api/api.h"
#include "include/trafficv10/trafficv10.h"
#include "_trafficv10_main.h"
_trafficv10_main_main_self_t* new__trafficv10_main() {
    _trafficv10_main_main_self_t* self = (_trafficv10_main_main_self_t*)_lf_new_reactor(sizeof(_trafficv10_main_main_self_t));

    return self;
}
