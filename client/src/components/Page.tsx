import { ReactElement, ReactNode } from "react";
import Navbar from "./Navbar";

interface Props {
  children: ReactNode;
  active?: string;
}
function Page({ children, active }: Props): ReactElement {
  return (
    <div className="flex justify-center w-full h-screen bg-slate-300">
      <Navbar active={active} />
      <div className="w-content mt-80px">{children}</div>
    </div>
  );
}

export default Page;
