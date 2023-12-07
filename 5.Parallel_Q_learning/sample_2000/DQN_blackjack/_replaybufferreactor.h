#ifndef _REPLAYBUFFERREACTOR_H
#define _REPLAYBUFFERREACTOR_H
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
#include "include/core/reactor.h"
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
#line 103 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_blackjack.lf"
typedef generic_port_instance_struct _replaybufferreactor_trajectories_t;
#line 104 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_blackjack.lf"
typedef generic_port_instance_struct _replaybufferreactor_dataset_t;
typedef struct {
    struct self_base_t base;
    char *_lf_name;
    PyObject* _lf_py_reaction_function_0;
    PyObject* _lf_py_reaction_function_1;
    
    #line 106 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_blackjack.lf"
    PyObject* experiences;
    #line 103 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_blackjack.lf"
    // Multiport input array will be malloc'd later.
    #line 103 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_blackjack.lf"
    _replaybufferreactor_trajectories_t** _lf_trajectories;
    #line 103 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_blackjack.lf"
    int _lf_trajectories_width;
    #line 103 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_blackjack.lf"
    // Default input (in case it does not get connected)
    #line 103 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_blackjack.lf"
    _replaybufferreactor_trajectories_t _lf_default__trajectories;
    #line 103 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_blackjack.lf"
    // Struct to support efficiently reading sparse inputs.
    #line 103 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_blackjack.lf"
    lf_sparse_io_record_t* _lf_trajectories__sparse;
    #line 104 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_blackjack.lf"
    _replaybufferreactor_dataset_t _lf_dataset;
    #line 104 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_blackjack.lf"
    int _lf_dataset_width;
    #line 108 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_blackjack.lf"
    reaction_t _lf__reaction_0;
    #line 113 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_blackjack.lf"
    reaction_t _lf__reaction_1;
    trigger_t _lf__startup;
    reaction_t* _lf__startup_reactions[1];
    #line 103 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_blackjack.lf"
    trigger_t _lf__trajectories;
    #line 103 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_blackjack.lf"
    reaction_t* _lf__trajectories_reactions[1];
    #ifdef FEDERATED
    trigger_t* _lf__trajectories_network_port_status;
    
    #endif // FEDERATED
} _replaybufferreactor_self_t;
_replaybufferreactor_self_t* new__replaybufferreactor();
#endif // _REPLAYBUFFERREACTOR_H
