from scoring_engine.engine.basic_check import BasicCheck

class HTTPProxyCheck(BasicCheck):
    required_properties = ['uri']
    CMD = 'curl -v --proxy {0}:{1} {2}'

    def command_format(self, properties):
        return (
            self.host,
            self.port,
            properties["uri"]
        )

