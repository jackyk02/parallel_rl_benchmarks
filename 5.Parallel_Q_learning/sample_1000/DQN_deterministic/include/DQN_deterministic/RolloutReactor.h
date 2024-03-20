#ifndef _rolloutreactor_H
#define _rolloutreactor_H
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
typedef struct rolloutreactor_self_t{
    self_base_t base; // This field is only to be used by the runtime, not the user.
    PyObject* env;
    PyObject* obs;
    PyObject* q_net;
    PyObject* rng;
    int end[0]; // placeholder; MSVC does not compile empty structs
} rolloutreactor_self_t;
#line 81 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
typedef generic_port_instance_struct _rolloutreactor_gradients_t;
#line 82 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
typedef generic_port_instance_struct _rolloutreactor_trajectories_t;
#endif
