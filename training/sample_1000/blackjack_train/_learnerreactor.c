#include "include/api/api.h"
#include "include/blackjack_train/LearnerReactor.h"
#include "_learnerreactor.h"
#include "include/api/set.h"
void _learnerreactorreaction_function_0(void* instance_args){
    _learnerreactor_self_t* self = (_learnerreactor_self_t*)instance_args; SUPPRESS_UNUSED_WARNING(self);
    _learnerreactor_gradients_t* gradients = &self->_lf_gradients;
    #line 125 "/mnt/c/Users/jacky/Desktop/simple_multi/src/blackjack_train.lf"
    // Acquire the GIL (Global Interpreter Lock) to be able to call Python APIs.
    PyGILState_STATE gstate;
    gstate = PyGILState_Ensure();
    
    LF_PRINT_DEBUG("Calling reaction function _learnerreactor.reaction_function_0");
    PyObject *rValue = PyObject_CallObject(
        self->_lf_py_reaction_function_0, 
        Py_BuildValue("(O)", convert_C_port_to_py(gradients, -2))
    );
    if (rValue == NULL) {
        lf_print_error("FATAL: Calling reaction _learnerreactor.reaction_function_0 failed.");
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
void _learnerreactorreaction_function_1(void* instance_args){
    _learnerreactor_self_t* self = (_learnerreactor_self_t*)instance_args; SUPPRESS_UNUSED_WARNING(self);
    _learnerreactor_dataset_t* dataset = self->_lf_dataset;
    int dataset_width = self->_lf_dataset_width; SUPPRESS_UNUSED_WARNING(dataset_width);
    _learnerreactor_gradients_t* gradients = &self->_lf_gradients;
    #line 133 "/mnt/c/Users/jacky/Desktop/simple_multi/src/blackjack_train.lf"
    // Acquire the GIL (Global Interpreter Lock) to be able to call Python APIs.
    PyGILState_STATE gstate;
    gstate = PyGILState_Ensure();
    
    LF_PRINT_DEBUG("Calling reaction function _learnerreactor.reaction_function_1");
    PyObject *rValue = PyObject_CallObject(
        self->_lf_py_reaction_function_1, 
        Py_BuildValue("(OO)", convert_C_port_to_py(dataset, dataset_width), convert_C_port_to_py(gradients, -2))
    );
    if (rValue == NULL) {
        lf_print_error("FATAL: Calling reaction _learnerreactor.reaction_function_1 failed.");
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
_learnerreactor_self_t* new__learnerreactor() {
    _learnerreactor_self_t* self = (_learnerreactor_self_t*)_lf_new_reactor(sizeof(_learnerreactor_self_t));
    #line 118 "/mnt/c/Users/jacky/Desktop/simple_multi/src/blackjack_train.lf"
    // Set input by default to an always absent default input.
    #line 118 "/mnt/c/Users/jacky/Desktop/simple_multi/src/blackjack_train.lf"
    self->_lf_dataset = &self->_lf_default__dataset;
    #line 118 "/mnt/c/Users/jacky/Desktop/simple_multi/src/blackjack_train.lf"
    // Set the default source reactor pointer
    #line 118 "/mnt/c/Users/jacky/Desktop/simple_multi/src/blackjack_train.lf"
    self->_lf_default__dataset._base.source_reactor = (self_base_t*)self;
    #line 124 "/mnt/c/Users/jacky/Desktop/simple_multi/src/blackjack_train.lf"
    self->_lf__reaction_0.number = 0;
    #line 124 "/mnt/c/Users/jacky/Desktop/simple_multi/src/blackjack_train.lf"
    self->_lf__reaction_0.function = _learnerreactorreaction_function_0;
    #line 124 "/mnt/c/Users/jacky/Desktop/simple_multi/src/blackjack_train.lf"
    self->_lf__reaction_0.self = self;
    #line 124 "/mnt/c/Users/jacky/Desktop/simple_multi/src/blackjack_train.lf"
    self->_lf__reaction_0.deadline_violation_handler = NULL;
    #line 124 "/mnt/c/Users/jacky/Desktop/simple_multi/src/blackjack_train.lf"
    self->_lf__reaction_0.STP_handler = NULL;
    #line 124 "/mnt/c/Users/jacky/Desktop/simple_multi/src/blackjack_train.lf"
    self->_lf__reaction_0.name = "?";
    #line 124 "/mnt/c/Users/jacky/Desktop/simple_multi/src/blackjack_train.lf"
    self->_lf__reaction_0.mode = NULL;
    #line 132 "/mnt/c/Users/jacky/Desktop/simple_multi/src/blackjack_train.lf"
    self->_lf__reaction_1.number = 1;
    #line 132 "/mnt/c/Users/jacky/Desktop/simple_multi/src/blackjack_train.lf"
    self->_lf__reaction_1.function = _learnerreactorreaction_function_1;
    #line 132 "/mnt/c/Users/jacky/Desktop/simple_multi/src/blackjack_train.lf"
    self->_lf__reaction_1.self = self;
    #line 132 "/mnt/c/Users/jacky/Desktop/simple_multi/src/blackjack_train.lf"
    self->_lf__reaction_1.deadline_violation_handler = NULL;
    #line 132 "/mnt/c/Users/jacky/Desktop/simple_multi/src/blackjack_train.lf"
    self->_lf__reaction_1.STP_handler = NULL;
    #line 132 "/mnt/c/Users/jacky/Desktop/simple_multi/src/blackjack_train.lf"
    self->_lf__reaction_1.name = "?";
    #line 132 "/mnt/c/Users/jacky/Desktop/simple_multi/src/blackjack_train.lf"
    self->_lf__reaction_1.mode = NULL;
    #ifdef FEDERATED_DECENTRALIZED
    self->_lf__startup.intended_tag = (tag_t) { .time = NEVER, .microstep = 0u};
    #endif // FEDERATED_DECENTRALIZED
    self->_lf__startup_reactions[0] = &self->_lf__reaction_0;
    self->_lf__startup.last = NULL;
    self->_lf__startup.reactions = &self->_lf__startup_reactions[0];
    self->_lf__startup.number_of_reactions = 1;
    self->_lf__startup.is_timer = false;
    #line 118 "/mnt/c/Users/jacky/Desktop/simple_multi/src/blackjack_train.lf"
    self->_lf__dataset.last = NULL;
    #line 118 "/mnt/c/Users/jacky/Desktop/simple_multi/src/blackjack_train.lf"
    #ifdef FEDERATED_DECENTRALIZED
    #line 118 "/mnt/c/Users/jacky/Desktop/simple_multi/src/blackjack_train.lf"
    self->_lf__dataset.intended_tag = (tag_t) { .time = NEVER, .microstep = 0u};
    #line 118 "/mnt/c/Users/jacky/Desktop/simple_multi/src/blackjack_train.lf"
    #endif // FEDERATED_DECENTRALIZED
    #line 118 "/mnt/c/Users/jacky/Desktop/simple_multi/src/blackjack_train.lf"
    #line 118 "/mnt/c/Users/jacky/Desktop/simple_multi/src/blackjack_train.lf"
    self->_lf__dataset_reactions[0] = &self->_lf__reaction_1;
    #line 118 "/mnt/c/Users/jacky/Desktop/simple_multi/src/blackjack_train.lf"
    self->_lf__dataset.reactions = &self->_lf__dataset_reactions[0];
    #line 118 "/mnt/c/Users/jacky/Desktop/simple_multi/src/blackjack_train.lf"
    self->_lf__dataset.number_of_reactions = 1;
    #line 118 "/mnt/c/Users/jacky/Desktop/simple_multi/src/blackjack_train.lf"
    #ifdef FEDERATED
    #line 118 "/mnt/c/Users/jacky/Desktop/simple_multi/src/blackjack_train.lf"
    self->_lf__dataset.physical_time_of_arrival = NEVER;
    #line 118 "/mnt/c/Users/jacky/Desktop/simple_multi/src/blackjack_train.lf"
    #endif // FEDERATED
    self->_lf__dataset.tmplt.type.element_size = sizeof(PyObject);
    return self;
}
