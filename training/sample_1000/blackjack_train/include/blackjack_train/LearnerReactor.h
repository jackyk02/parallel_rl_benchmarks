#ifndef _learnerreactor_H
#define _learnerreactor_H
#include <limits.h>
#include "include/core/platform.h"
#include "include/api/api.h"
#include "include/core/reactor.h"
#include "include/core/reactor_common.h"
#include "include/core/threaded/scheduler.h"
#include "include/core/mixed_radix.h"
#include "include/core/port.h"
#include "include/core/environment.h"
int lf_reactor_c_main(int argc, const char* argv[]);
#include "pythontarget.h"
#ifdef __cplusplus
extern "C" {
#endif
#include "../include/api/api.h"
#include "../include/core/reactor.h"
#ifdef __cplusplus
}
#endif
typedef struct learnerreactor_self_t{
    self_base_t base; // This field is only to be used by the runtime, not the user.
    PyObject* start_time;
    PyObject* policy_net_state;
    PyObject* round;
    int end[0]; // placeholder; MSVC does not compile empty structs
} learnerreactor_self_t;
#line 118 "/mnt/c/Users/jacky/Desktop/simple_multi/src/blackjack_train.lf"
typedef generic_port_instance_struct _learnerreactor_dataset_t;
#line 117 "/mnt/c/Users/jacky/Desktop/simple_multi/src/blackjack_train.lf"
typedef generic_port_instance_struct _learnerreactor_gradients_t;
#endif
