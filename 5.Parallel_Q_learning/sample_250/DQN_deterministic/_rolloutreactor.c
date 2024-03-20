#include "include/api/api.h"
#include "include/DQN_deterministic/RolloutReactor.h"
#include "_rolloutreactor.h"
#include "include/api/set.h"
void _rolloutreactorreaction_function_0(void* instance_args){
    _rolloutreactor_self_t* self = (_rolloutreactor_self_t*)instance_args; SUPPRESS_UNUSED_WARNING(self);
    
    #line 90 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    // Acquire the GIL (Global Interpreter Lock) to be able to call Python APIs.
    PyGILState_STATE gstate;
    gstate = PyGILState_Ensure();
    
    LF_PRINT_DEBUG("Calling reaction function _rolloutreactor.reaction_function_0");
    PyObject *rValue = PyObject_CallObject(
        self->_lf_py_reaction_function_0, 
        Py_BuildValue("()")
    );
    if (rValue == NULL) {
        lf_print_error("FATAL: Calling reaction _rolloutreactor.reaction_function_0 failed.");
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
void _rolloutreactorreaction_function_1(void* instance_args){
    _rolloutreactor_self_t* self = (_rolloutreactor_self_t*)instance_args; SUPPRESS_UNUSED_WARNING(self);
    _rolloutreactor_gradients_t* gradients = self->_lf_gradients;
    int gradients_width = self->_lf_gradients_width; SUPPRESS_UNUSED_WARNING(gradients_width);
    _rolloutreactor_trajectories_t* trajectories = &self->_lf_trajectories;
    #line 99 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    // Acquire the GIL (Global Interpreter Lock) to be able to call Python APIs.
    PyGILState_STATE gstate;
    gstate = PyGILState_Ensure();
    
    LF_PRINT_DEBUG("Calling reaction function _rolloutreactor.reaction_function_1");
    PyObject *rValue = PyObject_CallObject(
        self->_lf_py_reaction_function_1, 
        Py_BuildValue("(OO)", convert_C_port_to_py(gradients, gradients_width), convert_C_port_to_py(trajectories, -2))
    );
    if (rValue == NULL) {
        lf_print_error("FATAL: Calling reaction _rolloutreactor.reaction_function_1 failed.");
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
_rolloutreactor_self_t* new__rolloutreactor() {
    _rolloutreactor_self_t* self = (_rolloutreactor_self_t*)_lf_new_reactor(sizeof(_rolloutreactor_self_t));
    #line 81 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    // Set input by default to an always absent default input.
    #line 81 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    self->_lf_gradients = &self->_lf_default__gradients;
    #line 81 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    // Set the default source reactor pointer
    #line 81 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    self->_lf_default__gradients._base.source_reactor = (self_base_t*)self;
    #line 89 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    self->_lf__reaction_0.number = 0;
    #line 89 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    self->_lf__reaction_0.function = _rolloutreactorreaction_function_0;
    #line 89 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    self->_lf__reaction_0.self = self;
    #line 89 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    self->_lf__reaction_0.deadline_violation_handler = NULL;
    #line 89 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    self->_lf__reaction_0.STP_handler = NULL;
    #line 89 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    self->_lf__reaction_0.name = "?";
    #line 89 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    self->_lf__reaction_0.mode = NULL;
    #line 98 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    self->_lf__reaction_1.number = 1;
    #line 98 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    self->_lf__reaction_1.function = _rolloutreactorreaction_function_1;
    #line 98 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    self->_lf__reaction_1.self = self;
    #line 98 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    self->_lf__reaction_1.deadline_violation_handler = NULL;
    #line 98 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    self->_lf__reaction_1.STP_handler = NULL;
    #line 98 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    self->_lf__reaction_1.name = "?";
    #line 98 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    self->_lf__reaction_1.mode = NULL;
    #ifdef FEDERATED_DECENTRALIZED
    self->_lf__startup.intended_tag = (tag_t) { .time = NEVER, .microstep = 0u};
    #endif // FEDERATED_DECENTRALIZED
    self->_lf__startup_reactions[0] = &self->_lf__reaction_0;
    self->_lf__startup.last = NULL;
    self->_lf__startup.reactions = &self->_lf__startup_reactions[0];
    self->_lf__startup.number_of_reactions = 1;
    self->_lf__startup.is_timer = false;
    #line 81 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    self->_lf__gradients.last = NULL;
    #line 81 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    #ifdef FEDERATED_DECENTRALIZED
    #line 81 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    self->_lf__gradients.intended_tag = (tag_t) { .time = NEVER, .microstep = 0u};
    #line 81 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    #endif // FEDERATED_DECENTRALIZED
    #line 81 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    #line 81 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    self->_lf__gradients_reactions[0] = &self->_lf__reaction_1;
    #line 81 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    self->_lf__gradients.reactions = &self->_lf__gradients_reactions[0];
    #line 81 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    self->_lf__gradients.number_of_reactions = 1;
    #line 81 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    #ifdef FEDERATED
    #line 81 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    self->_lf__gradients.physical_time_of_arrival = NEVER;
    #line 81 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    #endif // FEDERATED
    self->_lf__gradients.tmplt.type.element_size = sizeof(PyObject);
    return self;
}
