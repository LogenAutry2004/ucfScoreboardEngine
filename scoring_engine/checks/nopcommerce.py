from scoring_engine.engine.basic_check import BasicCheck, CHECKS_BIN_PATH


class NopCommerceCheck(BasicCheck):
    CMD = CHECKS_BIN_PATH + '/nopcommerce_check {0} {1} {2} {3}'

    def command_format(self, properties):
        account = self.get_random_account()
        return (
            self.host,
            self.port,
            account.username,
            account.password
        )

