#include "include/api/api.h"
#include "include/DQN_deterministic/DQN_deterministic.h"
#include "_dqn_deterministic_main.h"
_dqn_deterministic_main_main_self_t* new__dqn_deterministic_main() {
    _dqn_deterministic_main_main_self_t* self = (_dqn_deterministic_main_main_self_t*)_lf_new_reactor(sizeof(_dqn_deterministic_main_main_self_t));

    return self;
}
