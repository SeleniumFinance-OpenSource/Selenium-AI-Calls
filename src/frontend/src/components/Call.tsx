import React, { useEffect } from 'react';
import { useWebRTC } from '../hooks/useWebRTC';

const Call: React.FC = () => {
  const { startCall, stream } = useWebRTC();

  useEffect(() => {
    startCall();
  }, [startCall]);

  return (
    <div className="p-4">
      <video autoPlay playsInline ref={(video) => video && (video.srcObject = stream)} />
      <button className="bg-blue-500 text-white p-2 rounded">Start Call</button>
    </div>
  );
};

export default Call;
