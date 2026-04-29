import { useEffect, useState } from "react";
import API from "../services/api";

function ListPage() {
  const [data, setData] = useState([]);
  const [status, setStatus] = useState("");
  const [query, setQuery] = useState("");
  const [debouncedQuery, setDebouncedQuery] = useState("");
  const [loading, setLoading] = useState(true);

  // 🔹 DEBOUNCE (wait 500ms after typing)
  useEffect(() => {
    const timer = setTimeout(() => {
      setDebouncedQuery(query);
    }, 500);

    return () => clearTimeout(timer);
  }, [query]);

  // 🔹 FETCH DATA
  useEffect(() => {
    let ignore = false;

    const fetchData = async () => {
      try {
        setLoading(true);

        const url = debouncedQuery
          ? `/api/search?q=${debouncedQuery}`
          : status
          ? `/api/status/${status}`
          : "/api/all";

        const res = await API.get(url);

        if (!ignore) {
          setData(res.data);
        }
      } catch (err) {
        console.error(err);
      } finally {
        if (!ignore) {
          setLoading(false);
        }
      }
    };

    fetchData();

    return () => {
      ignore = true;
    };
  }, [status, debouncedQuery]);

  // 🔹 DELETE
  const handleDelete = (id) => {
    if (!window.confirm("Delete this record?")) return;

    API.delete(`/api/${id}`)
      .then(() => {
        alert("Deleted!");
        setData((prev) => prev.filter((item) => item.id !== id));
      })
      .catch((err) => console.error(err));
  };

  // 🔹 EDIT
  const handleEdit = (item) => {
    const newName = prompt("Company Name:", item.companyName);
    if (!newName) return;

    const newScore = prompt("Score:", item.complianceScore);
    const newStatus = prompt(
      "Status (COMPLIANT/NON-COMPLIANT):",
      item.status
    );

    const payload = {
      companyName: newName,
      complianceScore: newScore ? Number(newScore) : null,
      status: newStatus,
      description: item.description,
    };

    API.put(`/api/${item.id}`, payload)
      .then(() => {
        alert("Updated!");
        setData((prev) =>
          prev.map((it) =>
            it.id === item.id ? { ...it, ...payload } : it
          )
        );
      })
      .catch((err) => console.error(err));
  };

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">
        Compliance Records
      </h1>

      {/* 🔹 DASHBOARD BUTTON */}
      <button
        onClick={() => (window.location.href = "/dashboard")}
        className="bg-gray-800 text-white px-3 py-2 mb-4 mr-2"
      >
        Dashboard
      </button>

      {/* 🔹 ADD BUTTON */}
      <button
        onClick={() => (window.location.href = "/add")}
        className="bg-blue-500 text-white px-3 py-2 mb-4"
      >
        Add Record
      </button>

      {/* 🔹 SEARCH */}
      <input
        placeholder="Search companies..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        className="border p-2 mb-4 block"
      />

      {/* 🔹 TYPING INDICATOR */}
      {query !== debouncedQuery && (
        <p className="text-sm text-gray-500 mb-2">Typing...</p>
      )}

      {/* 🔹 FILTER */}
      <select
        onChange={(e) => setStatus(e.target.value)}
        className="mb-4 border p-2"
      >
        <option value="">All</option>
        <option value="COMPLIANT">Compliant</option>
        <option value="NON-COMPLIANT">
          Non-Compliant
        </option>
      </select>

      {/* 🔹 TABLE */}
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
              <th className="border px-4">Actions</th>
            </tr>
          </thead>

          <tbody>
            {data.map((item) => (
              <tr
                key={item.id}
                onClick={() =>
                  (window.location.href = `/details/${item.id}`)
                }
                className="cursor-pointer hover:bg-gray-100"
              >
                <td className="border px-4">{item.id}</td>
                <td className="border px-4">
                  {item.companyName}
                </td>
                <td className="border px-4">
                  {item.complianceScore}
                </td>
                <td className="border px-4">
                  {item.status}
                </td>

                <td className="border px-4 space-x-2">
                  <button
                    onClick={(e) => {
                      e.stopPropagation();
                      handleEdit(item);
                    }}
                    className="bg-yellow-500 text-white px-2 py-1"
                  >
                    Edit
                  </button>

                  <button
                    onClick={(e) => {
                      e.stopPropagation();
                      handleDelete(item.id);
                    }}
                    className="bg-red-500 text-white px-2 py-1"
                  >
                    Delete
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default ListPage;