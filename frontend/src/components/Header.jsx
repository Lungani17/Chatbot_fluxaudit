import React from 'react';

function Header() {
  return (
    <div className="relative shadow-md z-10">
      {/* Main content: Avatar, Name, Status */}
      <div className="p-4 bg-blue-600 text-white pb-16">
        <div className="flex items-center space-x-4">
          
          {/* --- Avatar/Profile Picture (Size Adjusted) --- */}
          <div className="w-14 h-14 rounded-full overflow-hidden bg-blue-700 flex-shrink-0 flex items-center justify-center shadow-inner">
            <span className="text-2xl font-bold text-white">FA</span>
          </div>
          
          {/* Name & Status (Compacted) */}
          <div className="flex flex-col">
            <h1 className="text-xl font-bold">Chat with FluxAudit</h1>
            <p className="text-sm text-blue-100">
              We are online!
            </p>
          </div>

        </div>
      </div>

      {/* --- NEW: Animated Wavy Bottom Shape --- */}
      <div 
        className="w-full h-[50px] overflow-hidden leading-none absolute bottom-0 left-0"
        style={{ height: '50px' }}
      >
        <svg 
          className="h-[50px]"
          viewBox="0 0 1920 50" 
          preserveAspectRatio="none"
          style={{ 
            // We set the width to be very wide, and apply the animation
            width: '1920px', 
            animation: 'wave 8s cubic-bezier(0.36, 0.45, 0.63, 0.53) infinite'
          }}
        >
          {/* This is a new repeating path. 
            The 'wave' animation scrolls it by 960px (half its width)
            to create a seamless, infinite loop.
          */}
          <path 
            fill="#dbeafe" // Light blue
            d="M0,30 C320,10 640,10 960,30 S1600,50 1920,30 L1920,50 L0,50 Z"
          />
        </svg>
      </div>
    </div>
  );
}

export default Header;