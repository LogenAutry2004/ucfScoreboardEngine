from scoring_engine.engine.basic_check import BasicCheck, CHECKS_BIN_PATH


class RDPCheck(BasicCheck):
    required_properties = []
    CMD = 'Xvfb :99 & export DISPLAY=:99;xfreerdp /auth-only /cert-ignore /u:{0} /p:{1} /v:{2}:{3}'
    # xfreerdp /auth-only /cert-ignore /u:{0} /p:'{1}' /v:{2}:{3}

    def command_format(self, properties):
        account = self.get_random_account()
        return (
            account.username,
            account.password,
            self.host,
            self.port,
        )
