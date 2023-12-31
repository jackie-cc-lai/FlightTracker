import { useContext, useState } from "react";
import Page from "../components/Page";
import api from "../helpers/api";
import AuthContext from "../helpers/authContext";
import { useNavigate } from "react-router-dom";

function LoginPage() {
  const navigate = useNavigate();
  const { setUser, setToken } = useContext(AuthContext);
  const handleSubmit = async (e: any) => {
    e.preventDefault();
    const email = e.target.elements.email.value;
    const password = e.target.elements.password.value;

    const response = await api.login({ email, password });
    const { token, user } = response;
    if (response.user) {
      setUser(user);
    }
    if (response.token) {
      localStorage.setItem("token", token);
      setToken(token);
    }
    navigate("/");
  };

  return (
    <Page>
      <div>
        <form onSubmit={handleSubmit}>
          <input
            name="email"
            type="string"
            placeholder="Email"
            className="px-4 py-4 border-2 w-full rounded-md focus:outline-indigo-500"
          />
          <input
            name="password"
            type="password"
            placeholder="Password"
            className="mt-4 px-4 py-4 border-2 w-full rounded-md focus:outline-indigo-500"
          />
          <input type="submit" hidden />
        </form>
      </div>
    </Page>
  );
}

export default LoginPage;
