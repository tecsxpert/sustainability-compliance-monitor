import { useEffect, useState } from "react";
import API from "../services/api";

export default function ListPage() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const res = await API.get("/api/all");
      setData(res.data);
    } catch (err) {
      console.error("Error loading data:", err);
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async (id) => {
    try {
      await API.delete(`/api/${id}`);
      alert("Deleted successfully");
      fetchData(); // refresh list
    } catch (err) {
      console.error("Delete failed:", err);
    }
  };

  if (loading) return <div className="p-4">Loading...</div>;
  if (data.length === 0) return <div className="p-4">No records found</div>;

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-4">Compliance List</h2>

      {data.map((item) => (
        <div
          key={item.id}
          className="border p-4 mb-3 rounded shadow"
        >
          <p className="font-semibold text-lg">
            {item.companyName}
          </p>
          <p>Status: {item.status}</p>
          <p>Score: {item.complianceScore}</p>

          <div className="mt-3 flex gap-2">
            
            {/* VIEW */}
            <button
              className="bg-blue-500 text-white px-3 py-1 rounded"
              onClick={() =>
                (window.location.href = `/details/${item.id}`)
              }
            >
              View
            </button>

            {/* EDIT */}
            <button
              className="bg-yellow-500 text-white px-3 py-1 rounded"
              onClick={() =>
                (window.location.href = `/edit/${item.id}`)
              }
            >
              Edit
            </button>

            {/* DELETE */}
            <button
              className="bg-red-500 text-white px-3 py-1 rounded"
              onClick={() => handleDelete(item.id)}
            >
              Delete
            </button>

          </div>
        </div>
      ))}
    </div>
  );
}