interface Props {
  headings: string[];
  data: string[][];
}
function Table({ headings, data }: Props) {
  return (
    <table className="w-full">
      <thead>
        {headings.map((heading) => (
          <th>{heading}</th>
        ))}
      </thead>
      <tbody>
        {data.map((row) => {
          console.log(row);
          return (
            <tr key={row[0]}>
              {row.map((r) => (
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
