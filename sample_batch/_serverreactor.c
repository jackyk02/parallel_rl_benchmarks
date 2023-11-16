#include "include/api/api.h"
#include "include/sample_batch/serverReactor.h"
#include "_serverreactor.h"
#include "include/api/set.h"
void _serverreactorreaction_function_0(void* instance_args){
    _serverreactor_self_t* self = (_serverreactor_self_t*)instance_args; SUPPRESS_UNUSED_WARNING(self);
    _serverreactor_seed_t* seed = &self->_lf_seed;
    #line 46 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    // Acquire the GIL (Global Interpreter Lock) to be able to call Python APIs.
    PyGILState_STATE gstate;
    gstate = PyGILState_Ensure();
    
    LF_PRINT_DEBUG("Calling reaction function _serverreactor.reaction_function_0");
    PyObject *rValue = PyObject_CallObject(
        self->_lf_py_reaction_function_0, 
        Py_BuildValue("(O)", convert_C_port_to_py(seed, -2))
    );
    if (rValue == NULL) {
        lf_print_error("FATAL: Calling reaction _serverreactor.reaction_function_0 failed.");
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
void _serverreactorreaction_function_1(void* instance_args){
    _serverreactor_self_t* self = (_serverreactor_self_t*)instance_args; SUPPRESS_UNUSED_WARNING(self);
    _serverreactor_infos_t** infos = self->_lf_infos;
    int infos_width = self->_lf_infos_width; SUPPRESS_UNUSED_WARNING(infos_width);
    _serverreactor_seed_t* seed = &self->_lf_seed;
    #line 51 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    // Acquire the GIL (Global Interpreter Lock) to be able to call Python APIs.
    PyGILState_STATE gstate;
    gstate = PyGILState_Ensure();
    
    LF_PRINT_DEBUG("Calling reaction function _serverreactor.reaction_function_1");
    PyObject *rValue = PyObject_CallObject(
        self->_lf_py_reaction_function_1, 
        Py_BuildValue("(OO)", convert_C_port_to_py(infos, infos_width), convert_C_port_to_py(seed, -2))
    );
    if (rValue == NULL) {
        lf_print_error("FATAL: Calling reaction _serverreactor.reaction_function_1 failed.");
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
_serverreactor_self_t* new__serverreactor() {
    _serverreactor_self_t* self = (_serverreactor_self_t*)_lf_new_reactor(sizeof(_serverreactor_self_t));
    #line 41 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    // Set the default source reactor pointer
    #line 41 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    self->_lf_default__infos._base.source_reactor = (self_base_t*)self;
    #line 45 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    self->_lf__reaction_0.number = 0;
    #line 45 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    self->_lf__reaction_0.function = _serverreactorreaction_function_0;
    #line 45 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    self->_lf__reaction_0.self = self;
    #line 45 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    self->_lf__reaction_0.deadline_violation_handler = NULL;
    #line 45 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    self->_lf__reaction_0.STP_handler = NULL;
    #line 45 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    self->_lf__reaction_0.name = "?";
    #line 45 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    self->_lf__reaction_0.mode = NULL;
    #line 50 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    self->_lf__reaction_1.number = 1;
    #line 50 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    self->_lf__reaction_1.function = _serverreactorreaction_function_1;
    #line 50 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    self->_lf__reaction_1.self = self;
    #line 50 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    self->_lf__reaction_1.deadline_violation_handler = NULL;
    #line 50 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    self->_lf__reaction_1.STP_handler = NULL;
    #line 50 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    self->_lf__reaction_1.name = "?";
    #line 50 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    self->_lf__reaction_1.mode = NULL;
    #ifdef FEDERATED_DECENTRALIZED
    self->_lf__startup.intended_tag = (tag_t) { .time = NEVER, .microstep = 0u};
    #endif // FEDERATED_DECENTRALIZED
    self->_lf__startup_reactions[0] = &self->_lf__reaction_0;
    self->_lf__startup.last = NULL;
    self->_lf__startup.reactions = &self->_lf__startup_reactions[0];
    self->_lf__startup.number_of_reactions = 1;
    self->_lf__startup.is_timer = false;
    #line 41 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    self->_lf__infos.last = NULL;
    #line 41 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    #ifdef FEDERATED_DECENTRALIZED
    #line 41 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    self->_lf__infos.intended_tag = (tag_t) { .time = NEVER, .microstep = 0u};
    #line 41 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    #endif // FEDERATED_DECENTRALIZED
    #line 41 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    #line 41 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    self->_lf__infos_reactions[0] = &self->_lf__reaction_1;
    #line 41 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    self->_lf__infos.reactions = &self->_lf__infos_reactions[0];
    #line 41 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    self->_lf__infos.number_of_reactions = 1;
    #line 41 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    #ifdef FEDERATED
    #line 41 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    self->_lf__infos.physical_time_of_arrival = NEVER;
    #line 41 "/mnt/c/Users/jacky/Desktop/simple_multi/src/sample_batch.lf"
    #endif // FEDERATED
    self->_lf__infos.tmplt.type.element_size = sizeof(PyObject);
    return self;
}
