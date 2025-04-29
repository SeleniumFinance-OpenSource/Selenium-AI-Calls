import asyncio
import logging
from .config import Config
from .session import SessionManager
from .webrtc import WebRTCManager
from ..encryption.signal import SignalProtocol
from ..ai.assistant import AIAssistant

class SeleniumAICall:
    def __init__(self):
        self.config = Config()
        self.session = SessionManager(self.config)
        self.webrtc = WebRTCManager(self.config)
        self.signal = SignalProtocol(self.config)
        self.assistant = AIAssistant(self.config)
        self.running = False

    async def start(self):
        logging.info("Starting Selenium AI Call...")
        self.running = True
        await asyncio.gather(
            self.session.start(),
            self.webrtc.start(),
            self.signal.initialize(),
            self.assistant.start()
        )

    async def stop(self):
        logging.info("Stopping Selenium AI Call...")
        self.running = False
        await self.session.stop()

if __name__ == "__main__":
    import platform
    app = SeleniumAICall()
    if platform.system() == "Emscripten":
        asyncio.ensure_future(app.start())
    else:
        asyncio.run(app.start())
