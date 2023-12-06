#ifndef _replaybufferreactor_H
#define _replaybufferreactor_H
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
typedef struct replaybufferreactor_self_t{
    self_base_t base; // This field is only to be used by the runtime, not the user.
    PyObject* experiences;
    int end[0]; // placeholder; MSVC does not compile empty structs
} replaybufferreactor_self_t;
#line 94 "/mnt/c/Users/jacky/Desktop/simple_multi/src/blackjack_train.lf"
typedef generic_port_instance_struct _replaybufferreactor_trajectories_t;
#line 95 "/mnt/c/Users/jacky/Desktop/simple_multi/src/blackjack_train.lf"
typedef generic_port_instance_struct _replaybufferreactor_dataset_t;
#endif
