#include "include/api/api.h"
#include "include/sample_batch/sample_batch.h"
#include "_sample_batch_main.h"
_sample_batch_main_main_self_t* new__sample_batch_main() {
    _sample_batch_main_main_self_t* self = (_sample_batch_main_main_self_t*)_lf_new_reactor(sizeof(_sample_batch_main_main_self_t));

    return self;
}
