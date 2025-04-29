import React, { useState } from 'react';
import Call from './components/Call';
import Chat from './components/Chat';
import Settings from './components/Settings';
import SOSButton from './components/SOSButton';

const App: React.FC = () => {
  const [activeTab, setActiveTab] = useState('call');

  return (
    <div className="min-h-screen bg-gray-100">
      <nav className="bg-blue-600 text-white p-4">
        <button onClick={() => setActiveTab('call')}>Call</button>
        <button onClick={() => setActiveTab('chat')}>Chat</button>
        <button onClick={() => setActiveTab('settings')}>Settings</button>
      </nav>
      {activeTab === 'call' && <Call />}
      {activeTab === 'chat' && <Chat />}
      {activeTab === 'settings' && <Settings />}
      <SOSButton />
    </div>
  );
};

export default App;
