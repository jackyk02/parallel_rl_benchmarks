#include "include/api/api.h"
#include "include/DQN_blackjack/DQN_blackjack.h"
#include "_dqn_blackjack_main.h"
_dqn_blackjack_main_main_self_t* new__dqn_blackjack_main() {
    _dqn_blackjack_main_main_self_t* self = (_dqn_blackjack_main_main_self_t*)_lf_new_reactor(sizeof(_dqn_blackjack_main_main_self_t));

    return self;
}
