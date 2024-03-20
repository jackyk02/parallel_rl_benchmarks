#ifndef __LF_GENDELAY_0_H
#define __LF_GENDELAY_0_H
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
typedef generic_port_instance_struct __lf_gendelay_0_inp_t;
typedef generic_port_instance_struct __lf_gendelay_0_out_t;
typedef generic_action_instance_struct __lf_gendelay_0_act_t;
typedef struct {
    struct self_base_t base;
    char *_lf_name;
    PyObject* _lf_py_reaction_function_0;
    PyObject* _lf_py_reaction_function_1;
    interval_t delay;
    
    __lf_gendelay_0_act_t _lf_act;
    __lf_gendelay_0_inp_t* _lf_inp;
    // width of -2 indicates that it is not a multiport.
    int _lf_inp_width;
    // Default input (in case it does not get connected)
    __lf_gendelay_0_inp_t _lf_default__inp;
    __lf_gendelay_0_out_t _lf_out;
    int _lf_out_width;
    reaction_t _lf__reaction_0;
    reaction_t _lf__reaction_1;
    trigger_t _lf__act;
    reaction_t* _lf__act_reactions[1];
    trigger_t _lf__inp;
    reaction_t* _lf__inp_reactions[1];
    #ifdef FEDERATED
    
    #endif // FEDERATED
} __lf_gendelay_0_self_t;
__lf_gendelay_0_self_t* new___lf_gendelay_0();
#endif // __LF_GENDELAY_0_H
