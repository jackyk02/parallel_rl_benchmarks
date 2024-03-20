#include "include/api/api.h"
#include "include/DQN_deterministic/ReplayBufferReactor.h"
#include "_replaybufferreactor.h"
#include "include/api/set.h"
void _replaybufferreactorreaction_function_0(void* instance_args){
    _replaybufferreactor_self_t* self = (_replaybufferreactor_self_t*)instance_args; SUPPRESS_UNUSED_WARNING(self);
    
    #line 135 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    // Acquire the GIL (Global Interpreter Lock) to be able to call Python APIs.
    PyGILState_STATE gstate;
    gstate = PyGILState_Ensure();
    
    LF_PRINT_DEBUG("Calling reaction function _replaybufferreactor.reaction_function_0");
    PyObject *rValue = PyObject_CallObject(
        self->_lf_py_reaction_function_0, 
        Py_BuildValue("()")
    );
    if (rValue == NULL) {
        lf_print_error("FATAL: Calling reaction _replaybufferreactor.reaction_function_0 failed.");
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
void _replaybufferreactorreaction_function_1(void* instance_args){
    _replaybufferreactor_self_t* self = (_replaybufferreactor_self_t*)instance_args; SUPPRESS_UNUSED_WARNING(self);
    _replaybufferreactor_trajectories_t** trajectories = self->_lf_trajectories;
    int trajectories_width = self->_lf_trajectories_width; SUPPRESS_UNUSED_WARNING(trajectories_width);
    _replaybufferreactor_dataset_t* dataset = &self->_lf_dataset;
    #line 140 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    // Acquire the GIL (Global Interpreter Lock) to be able to call Python APIs.
    PyGILState_STATE gstate;
    gstate = PyGILState_Ensure();
    
    LF_PRINT_DEBUG("Calling reaction function _replaybufferreactor.reaction_function_1");
    PyObject *rValue = PyObject_CallObject(
        self->_lf_py_reaction_function_1, 
        Py_BuildValue("(OO)", convert_C_port_to_py(trajectories, trajectories_width), convert_C_port_to_py(dataset, -2))
    );
    if (rValue == NULL) {
        lf_print_error("FATAL: Calling reaction _replaybufferreactor.reaction_function_1 failed.");
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
_replaybufferreactor_self_t* new__replaybufferreactor() {
    _replaybufferreactor_self_t* self = (_replaybufferreactor_self_t*)_lf_new_reactor(sizeof(_replaybufferreactor_self_t));
    #line 129 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    // Set the default source reactor pointer
    #line 129 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    self->_lf_default__trajectories._base.source_reactor = (self_base_t*)self;
    #line 134 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    self->_lf__reaction_0.number = 0;
    #line 134 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    self->_lf__reaction_0.function = _replaybufferreactorreaction_function_0;
    #line 134 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    self->_lf__reaction_0.self = self;
    #line 134 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    self->_lf__reaction_0.deadline_violation_handler = NULL;
    #line 134 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    self->_lf__reaction_0.STP_handler = NULL;
    #line 134 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    self->_lf__reaction_0.name = "?";
    #line 134 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    self->_lf__reaction_0.mode = NULL;
    #line 139 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    self->_lf__reaction_1.number = 1;
    #line 139 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    self->_lf__reaction_1.function = _replaybufferreactorreaction_function_1;
    #line 139 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    self->_lf__reaction_1.self = self;
    #line 139 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    self->_lf__reaction_1.deadline_violation_handler = NULL;
    #line 139 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    self->_lf__reaction_1.STP_handler = NULL;
    #line 139 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    self->_lf__reaction_1.name = "?";
    #line 139 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    self->_lf__reaction_1.mode = NULL;
    #ifdef FEDERATED_DECENTRALIZED
    self->_lf__startup.intended_tag = (tag_t) { .time = NEVER, .microstep = 0u};
    #endif // FEDERATED_DECENTRALIZED
    self->_lf__startup_reactions[0] = &self->_lf__reaction_0;
    self->_lf__startup.last = NULL;
    self->_lf__startup.reactions = &self->_lf__startup_reactions[0];
    self->_lf__startup.number_of_reactions = 1;
    self->_lf__startup.is_timer = false;
    #line 129 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    self->_lf__trajectories.last = NULL;
    #line 129 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    #ifdef FEDERATED_DECENTRALIZED
    #line 129 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    self->_lf__trajectories.intended_tag = (tag_t) { .time = NEVER, .microstep = 0u};
    #line 129 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    #endif // FEDERATED_DECENTRALIZED
    #line 129 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    #line 129 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    self->_lf__trajectories_reactions[0] = &self->_lf__reaction_1;
    #line 129 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    self->_lf__trajectories.reactions = &self->_lf__trajectories_reactions[0];
    #line 129 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    self->_lf__trajectories.number_of_reactions = 1;
    #line 129 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    #ifdef FEDERATED
    #line 129 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    self->_lf__trajectories.physical_time_of_arrival = NEVER;
    #line 129 "/mnt/c/Users/jacky/Desktop/simple_multi/src/DQN_deterministic.lf"
    #endif // FEDERATED
    self->_lf__trajectories.tmplt.type.element_size = sizeof(PyObject);
    return self;
}
