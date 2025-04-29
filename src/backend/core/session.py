import uuid
import asyncio
from aiorouter import TorRouter

class SessionManager:
    def __init__(self, config):
        self.config = config
        self.sessions = {}
        self.tor = TorRouter() if config.tor_enabled else None

    async def create_session(self, user_id):
        session_id = str(uuid.uuid4())
        self.sessions[session_id] = {"user_id": user_id, "active": True}
        if self.tor:
            await self.tor.create_circuit(session_id)
        return session_id

    async def start(self):
        while True:
            for session_id, session in list(self.sessions.items()):
                if not session["active"]:
                    del self.sessions[session_id]
            await asyncio.sleep(60)

    async def stop(self):
        for session_id in self.sessions:
            if self.tor:
                await self.tor.close_circuit(session_id)
        self.sessions.clear()
