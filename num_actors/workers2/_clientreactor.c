#include "include/api/api.h"
#include "include/workers2/clientReactor.h"
#include "_clientreactor.h"
#include "include/api/set.h"
void _clientreactorreaction_function_0(void* instance_args){
    _clientreactor_self_t* self = (_clientreactor_self_t*)instance_args; SUPPRESS_UNUSED_WARNING(self);
    
    #line 15 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers2.lf"
    // Acquire the GIL (Global Interpreter Lock) to be able to call Python APIs.
    PyGILState_STATE gstate;
    gstate = PyGILState_Ensure();
    
    LF_PRINT_DEBUG("Calling reaction function _clientreactor.reaction_function_0");
    PyObject *rValue = PyObject_CallObject(
        self->_lf_py_reaction_function_0, 
        Py_BuildValue("()")
    );
    if (rValue == NULL) {
        lf_print_error("FATAL: Calling reaction _clientreactor.reaction_function_0 failed.");
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
void _clientreactorreaction_function_1(void* instance_args){
    _clientreactor_self_t* self = (_clientreactor_self_t*)instance_args; SUPPRESS_UNUSED_WARNING(self);
    _clientreactor_global_parameters_t* global_parameters = self->_lf_global_parameters;
    int global_parameters_width = self->_lf_global_parameters_width; SUPPRESS_UNUSED_WARNING(global_parameters_width);
    _clientreactor_updated_parameters_t* updated_parameters = &self->_lf_updated_parameters;
    #line 17 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers2.lf"
    // Acquire the GIL (Global Interpreter Lock) to be able to call Python APIs.
    PyGILState_STATE gstate;
    gstate = PyGILState_Ensure();
    
    LF_PRINT_DEBUG("Calling reaction function _clientreactor.reaction_function_1");
    PyObject *rValue = PyObject_CallObject(
        self->_lf_py_reaction_function_1, 
        Py_BuildValue("(OO)", convert_C_port_to_py(global_parameters, global_parameters_width), convert_C_port_to_py(updated_parameters, -2))
    );
    if (rValue == NULL) {
        lf_print_error("FATAL: Calling reaction _clientreactor.reaction_function_1 failed.");
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
_clientreactor_self_t* new__clientreactor() {
    _clientreactor_self_t* self = (_clientreactor_self_t*)_lf_new_reactor(sizeof(_clientreactor_self_t));
    #line 11 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers2.lf"
    // Set input by default to an always absent default input.
    #line 11 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers2.lf"
    self->_lf_global_parameters = &self->_lf_default__global_parameters;
    #line 11 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers2.lf"
    // Set the default source reactor pointer
    #line 11 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers2.lf"
    self->_lf_default__global_parameters._base.source_reactor = (self_base_t*)self;
    #line 14 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers2.lf"
    self->_lf__reaction_0.number = 0;
    #line 14 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers2.lf"
    self->_lf__reaction_0.function = _clientreactorreaction_function_0;
    #line 14 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers2.lf"
    self->_lf__reaction_0.self = self;
    #line 14 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers2.lf"
    self->_lf__reaction_0.deadline_violation_handler = NULL;
    #line 14 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers2.lf"
    self->_lf__reaction_0.STP_handler = NULL;
    #line 14 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers2.lf"
    self->_lf__reaction_0.name = "?";
    #line 14 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers2.lf"
    self->_lf__reaction_0.mode = NULL;
    #line 16 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers2.lf"
    self->_lf__reaction_1.number = 1;
    #line 16 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers2.lf"
    self->_lf__reaction_1.function = _clientreactorreaction_function_1;
    #line 16 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers2.lf"
    self->_lf__reaction_1.self = self;
    #line 16 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers2.lf"
    self->_lf__reaction_1.deadline_violation_handler = NULL;
    #line 16 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers2.lf"
    self->_lf__reaction_1.STP_handler = NULL;
    #line 16 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers2.lf"
    self->_lf__reaction_1.name = "?";
    #line 16 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers2.lf"
    self->_lf__reaction_1.mode = NULL;
    #ifdef FEDERATED_DECENTRALIZED
    self->_lf__startup.intended_tag = (tag_t) { .time = NEVER, .microstep = 0u};
    #endif // FEDERATED_DECENTRALIZED
    self->_lf__startup_reactions[0] = &self->_lf__reaction_0;
    self->_lf__startup.last = NULL;
    self->_lf__startup.reactions = &self->_lf__startup_reactions[0];
    self->_lf__startup.number_of_reactions = 1;
    self->_lf__startup.is_timer = false;
    #line 11 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers2.lf"
    self->_lf__global_parameters.last = NULL;
    #line 11 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers2.lf"
    #ifdef FEDERATED_DECENTRALIZED
    #line 11 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers2.lf"
    self->_lf__global_parameters.intended_tag = (tag_t) { .time = NEVER, .microstep = 0u};
    #line 11 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers2.lf"
    #endif // FEDERATED_DECENTRALIZED
    #line 11 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers2.lf"
    #line 11 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers2.lf"
    self->_lf__global_parameters_reactions[0] = &self->_lf__reaction_1;
    #line 11 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers2.lf"
    self->_lf__global_parameters.reactions = &self->_lf__global_parameters_reactions[0];
    #line 11 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers2.lf"
    self->_lf__global_parameters.number_of_reactions = 1;
    #line 11 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers2.lf"
    #ifdef FEDERATED
    #line 11 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers2.lf"
    self->_lf__global_parameters.physical_time_of_arrival = NEVER;
    #line 11 "/mnt/c/Users/jacky/Desktop/simple_multi/src/workers2.lf"
    #endif // FEDERATED
    self->_lf__global_parameters.tmplt.type.element_size = sizeof(PyObject);
    return self;
}
