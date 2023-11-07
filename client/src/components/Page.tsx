import { ReactElement, ReactNode, useContext, useEffect } from "react";
import Navbar from "./Navbar";
import AuthContext from "../helpers/authContext";
import { redirect, useLocation, useNavigate } from "react-router-dom";

interface Props {
  children: ReactNode;
  active?: string;
}
function Page({ children, active }: Props): ReactElement {
  const { token } = useContext(AuthContext);
  const navigate = useNavigate();
  const location = useLocation();
  useEffect(() => {
    if (!token && location.pathname !== "/login") {
      navigate("/login");
    }
  });

  useEffect(() => {
    if (token && location.pathname === "/login") {
      navigate("/");
    }
  });

  return (
    <div className="flex justify-center w-full h-screen">
      <Navbar active={active} />
      <div className="w-content mt-80px">{children}</div>
    </div>
  );
}

export default Page;
