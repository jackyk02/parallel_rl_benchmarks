#include "include/api/api.h"
#include "include/sample_batch/EnvReactor.h"
#include "_envreactor.h"
#include "include/api/set.h"
void _envreactorreaction_function_0(void* instance_args){
    _envreactor_self_t* self = (_envreactor_self_t*)instance_args; SUPPRESS_UNUSED_WARNING(self);
    
    #line 18 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    // Acquire the GIL (Global Interpreter Lock) to be able to call Python APIs.
    PyGILState_STATE gstate;
    gstate = PyGILState_Ensure();
    
    LF_PRINT_DEBUG("Calling reaction function _envreactor.reaction_function_0");
    PyObject *rValue = PyObject_CallObject(
        self->_lf_py_reaction_function_0, 
        Py_BuildValue("()")
    );
    if (rValue == NULL) {
        lf_print_error("FATAL: Calling reaction _envreactor.reaction_function_0 failed.");
        if (PyErr_Occurred()) {
            PyErr_PrintEx(0);
            PyErr_Clear(); // this will reset the error indicator so we can run Python code again
        }
        /* Release the thread. No Python API allowed beyond this point. */
    PyGILState_Release(gstate);
        Py_FinalizeEx();
        exit(1);
    }
    
    /* Release the thread. No Python API allowed beyond this point. */
    /* Release the thread. No Python API allowed beyond this point. */
    PyGILState_Release(gstate);
}
#include "include/api/set_undef.h"
#include "include/api/set.h"
void _envreactorreaction_function_1(void* instance_args){
    _envreactor_self_t* self = (_envreactor_self_t*)instance_args; SUPPRESS_UNUSED_WARNING(self);
    _envreactor_seed_t* seed = self->_lf_seed;
    int seed_width = self->_lf_seed_width; SUPPRESS_UNUSED_WARNING(seed_width);
    _envreactor_infos_t* infos = &self->_lf_infos;
    #line 23 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    // Acquire the GIL (Global Interpreter Lock) to be able to call Python APIs.
    PyGILState_STATE gstate;
    gstate = PyGILState_Ensure();
    
    LF_PRINT_DEBUG("Calling reaction function _envreactor.reaction_function_1");
    PyObject *rValue = PyObject_CallObject(
        self->_lf_py_reaction_function_1, 
        Py_BuildValue("(OO)", convert_C_port_to_py(seed, seed_width), convert_C_port_to_py(infos, -2))
    );
    if (rValue == NULL) {
        lf_print_error("FATAL: Calling reaction _envreactor.reaction_function_1 failed.");
        if (PyErr_Occurred()) {
            PyErr_PrintEx(0);
            PyErr_Clear(); // this will reset the error indicator so we can run Python code again
        }
        /* Release the thread. No Python API allowed beyond this point. */
    PyGILState_Release(gstate);
        Py_FinalizeEx();
        exit(1);
    }
    
    /* Release the thread. No Python API allowed beyond this point. */
    /* Release the thread. No Python API allowed beyond this point. */
    PyGILState_Release(gstate);
}
#include "include/api/set_undef.h"
_envreactor_self_t* new__envreactor() {
    _envreactor_self_t* self = (_envreactor_self_t*)_lf_new_reactor(sizeof(_envreactor_self_t));
    #line 14 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    // Set input by default to an always absent default input.
    #line 14 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    self->_lf_seed = &self->_lf_default__seed;
    #line 14 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    // Set the default source reactor pointer
    #line 14 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    self->_lf_default__seed._base.source_reactor = (self_base_t*)self;
    #line 17 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    self->_lf__reaction_0.number = 0;
    #line 17 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    self->_lf__reaction_0.function = _envreactorreaction_function_0;
    #line 17 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    self->_lf__reaction_0.self = self;
    #line 17 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    self->_lf__reaction_0.deadline_violation_handler = NULL;
    #line 17 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    self->_lf__reaction_0.STP_handler = NULL;
    #line 17 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    self->_lf__reaction_0.name = "?";
    #line 17 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    self->_lf__reaction_0.mode = NULL;
    #line 22 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    self->_lf__reaction_1.number = 1;
    #line 22 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    self->_lf__reaction_1.function = _envreactorreaction_function_1;
    #line 22 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    self->_lf__reaction_1.self = self;
    #line 22 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    self->_lf__reaction_1.deadline_violation_handler = NULL;
    #line 22 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    self->_lf__reaction_1.STP_handler = NULL;
    #line 22 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    self->_lf__reaction_1.name = "?";
    #line 22 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    self->_lf__reaction_1.mode = NULL;
    #ifdef FEDERATED_DECENTRALIZED
    self->_lf__startup.intended_tag = (tag_t) { .time = NEVER, .microstep = 0u};
    #endif // FEDERATED_DECENTRALIZED
    self->_lf__startup_reactions[0] = &self->_lf__reaction_0;
    self->_lf__startup.last = NULL;
    self->_lf__startup.reactions = &self->_lf__startup_reactions[0];
    self->_lf__startup.number_of_reactions = 1;
    self->_lf__startup.is_timer = false;
    #line 14 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    self->_lf__seed.last = NULL;
    #line 14 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    #ifdef FEDERATED_DECENTRALIZED
    #line 14 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    self->_lf__seed.intended_tag = (tag_t) { .time = NEVER, .microstep = 0u};
    #line 14 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    #endif // FEDERATED_DECENTRALIZED
    #line 14 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    #line 14 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    self->_lf__seed_reactions[0] = &self->_lf__reaction_1;
    #line 14 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    self->_lf__seed.reactions = &self->_lf__seed_reactions[0];
    #line 14 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    self->_lf__seed.number_of_reactions = 1;
    #line 14 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    #ifdef FEDERATED
    #line 14 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    self->_lf__seed.physical_time_of_arrival = NEVER;
    #line 14 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    #endif // FEDERATED
    self->_lf__seed.tmplt.type.element_size = sizeof(PyObject);
    return self;
}
