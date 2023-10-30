import { useState } from "react";
import Page from "../components/Page";

function LoginPage() {
  const [login, setLogin] = useState("");
  const handleSubmit = (e: any) => {
    e.preventDefault();
    console.log(e);
  };

  const handleChange = (e: any) => {
    setLogin(e.target.value);
  };

  return (
    <Page>
      <div>
        <form onSubmit={handleSubmit}>
          <input
            type="string"
            className="px-4 py-4 border-2 w-full rounded-md focus:outline-indigo-500"
            onChange={handleChange}
          />
        </form>
      </div>
    </Page>
  );
}

export default LoginPage;
