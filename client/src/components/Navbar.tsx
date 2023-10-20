import classNames from "classnames";
import { Link } from "react-router-dom";
import navlinks from "../constants/PageConstants";
interface Props {
  active?: string;
}

function Navbar({ active }: Props) {
  return (
    <div className="px-4 absolute text-base w-full top-0 flex border-b-2">
      {navlinks.map((link) => {
        return (
          <Link
            className={classNames(
              "mx-4 px-1 py-4 font-semibold",
              active === link.id && "border-b-2 border-b-indigo-500"
            )}
            key={link.id as React.Key}
            to={link.path}
          >
            {link.name}
          </Link>
        );
      })}
    </div>
  );
}

export default Navbar;
