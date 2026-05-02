import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import API from "../services/api";

export default function EditPage() {
  const { id } = useParams();

  const [form, setForm] = useState({
    companyName: "",
    complianceScore: "",
    status: "",
    description: ""
  });

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const res = await API.get(`/api/${id}`);
      setForm(res.data);
    } catch (err) {
      console.error("Error loading record:", err);
    }
  };

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value
    });
  };

  const handleUpdate = async () => {
    try {
      await API.put(`/api/${id}`, form);
      alert("Updated successfully");
      window.location.href = "/list";
    } catch (err) {
      console.error("Update failed:", err);
    }
  };

  return (
    <div className="p-6">
      <h2 className="text-xl mb-4">Edit Record</h2>

      <input
        name="companyName"
        value={form.companyName}
        onChange={handleChange}
        className="border p-2 mb-2 block"
      />

      <input
        name="complianceScore"
        value={form.complianceScore}
        onChange={handleChange}
        className="border p-2 mb-2 block"
      />

      <input
        name="status"
        value={form.status}
        onChange={handleChange}
        className="border p-2 mb-2 block"
      />

      <textarea
        name="description"
        value={form.description}
        onChange={handleChange}
        className="border p-2 mb-2 block"
      />

      <button
        onClick={handleUpdate}
        className="bg-green-500 text-white px-4 py-2"
      >
        Update
      </button>
    </div>
  );
}