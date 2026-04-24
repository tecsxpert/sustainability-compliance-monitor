import { useEffect, useState } from "react";
import API from "../services/api";

function ListPage() {
  const [data, setData] = useState([]);
  const [status, setStatus] = useState("");
  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
  const fetchData = async () => {
    setLoading(true);

    try {
      const url = query
        ? `/api/search?q=${query}`
        : status
        ? `/api/status/${status}`
        : "/api/all";

      const res = await API.get(url);
      setData(res.data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  fetchData();
}, [status, query]);
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Compliance Records</h1>

      {/* SEARCH */}
      <input
        placeholder="Search..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        className="border p-2 mb-4"
      />

      {/* FILTER */}
      <select
        onChange={(e) => setStatus(e.target.value)}
        className="mb-4 border p-2"
      >
        <option value="">All</option>
        <option value="COMPLIANT">Compliant</option>
        <option value="NON-COMPLIANT">Non-Compliant</option>
      </select>

      {loading ? (
        <p>Loading...</p>
      ) : data.length === 0 ? (
        <p>No records found</p>
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