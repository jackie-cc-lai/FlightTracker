import classNames from "classnames";

interface Props {
  headings: string[];
  data: { key: string; data: string[] }[];
  onClick?: (data: any) => void;
}
function Table({ headings, data, onClick }: Props) {
  console.log(data);
  return (
    <table className="w-full">
      <thead className="border-b-2">
        <tr>
          {headings.map((heading) => (
            <th className="text-left">{heading}</th>
          ))}
        </tr>
      </thead>
      <tbody>
        {data.map((row) => {
          return (
            <tr
              className={classNames(
                "py-2 hover:bg-white",
                onClick && "cursor-pointer"
              )}
              key={row.key}
              onClick={() => onClick?.(row.key)}
            >
              {row.data.map((r) => (
                <td>{r}</td>
              ))}
            </tr>
          );
        })}
      </tbody>
    </table>
  );
}
export default Table;
