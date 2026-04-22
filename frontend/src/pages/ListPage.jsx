import { useEffect, useState } from "react";
import API from "../services/api";

function ListPage() {
  const [data, setData] = useState([]);
  const [status, setStatus] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setLoading(true);

    const url = status ? `/api/status/${status}` : "/api/all";

    API.get(url)
      .then((res) => setData(res.data))
      .catch((err) => console.error(err))
      .finally(() => setLoading(false));
  }, [status]);

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Compliance Records</h1>

      {/* Filter */}
      <select
        className="mb-4 border p-2"
        onChange={(e) => setStatus(e.target.value)}
      >
        <option value="">All</option>
        <option value="COMPLIANT">Compliant</option>
        <option value="NON-COMPLIANT">Non-Compliant</option>
      </select>

      {/* States */}
      {loading ? (
        <p>Loading...</p>
      ) : data.length === 0 ? (
        <p className="text-gray-500">No records found</p>
      ) : (
        <table className="table-auto border w-full">
          <thead>
            <tr>
              <th className="border px-4">ID</th>
              <th className="border px-4">Company</th>
              <th className="border px-4">Score</th>
              <th className="border px-4">Status</th>
            </tr>
          </thead>
          <tbody>
            {data.map((item) => (
              <tr key={item.id}>
                <td className="border px-4">{item.id}</td>
                <td className="border px-4">{item.companyName}</td>
                <td className="border px-4">{item.complianceScore}</td>
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