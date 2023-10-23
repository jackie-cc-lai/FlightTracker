import { ReactNode } from "react";

interface Props {
  children: ReactNode;
  onClose: () => void;
}
function Sidebar({ children, onClose }: Props) {
  return (
    <div className="border-l-2 h-screen w-sidebar absolute right-0 top-80px p-4">
      <div className="sticky w-full my-2">
        <button
          onClick={() => {
            onClose();
          }}
          className="sticky right-0"
        >
          X
        </button>
      </div>
      {children}
    </div>
  );
}

export default Sidebar;
