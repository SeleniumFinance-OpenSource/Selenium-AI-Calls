from .biometric import BiometricAuth

class SOSBroadcast:
    def __init__(self, config):
        self.config = config
        self.biometric = BiometricAuth(config)

    async def send(self, geolocation, trusted_contacts):
        if await self.biometric.authenticate(None, None):
            # Send encrypted SOS message
            pass
