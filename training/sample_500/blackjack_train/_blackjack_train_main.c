#include "include/api/api.h"
#include "include/blackjack_train/blackjack_train.h"
#include "_blackjack_train_main.h"
_blackjack_train_main_main_self_t* new__blackjack_train_main() {
    _blackjack_train_main_main_self_t* self = (_blackjack_train_main_main_self_t*)_lf_new_reactor(sizeof(_blackjack_train_main_main_self_t));

    return self;
}
