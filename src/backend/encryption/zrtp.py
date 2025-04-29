import hashlib

class ZRTP:
    def __init__(self, config):
        self.config = config

    def initiate_key_exchange(self, session_id):
        # Dynamic key sharing for ZRTP
        key = hashlib.sha256(str(session_id).encode()).digest()
        return key
