import { useEffect, useState } from "react";
import API from "../services/api";

function ListPage() {
  const [data, setData] = useState([]);

  useEffect(() => {
    API.get("/api/all")
      .then((res) => setData(res.data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Compliance Records</h1>

      {data.length === 0 ? (
        <p>Loading...</p>
      ) : (
        <table className="table-auto border w-full">
          <thead>
            <tr>
              <th className="border px-4">ID</th>
              <th className="border px-4">Company</th>
              <th className="border px-4">Status</th>
            </tr>
          </thead>
          <tbody>
            {data.map((item) => (
              <tr key={item.id}>
                <td className="border px-4">{item.id}</td>
                <td className="border px-4">{item.company_name}</td>
                <td className="border px-4">{item.status}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default ListPage;