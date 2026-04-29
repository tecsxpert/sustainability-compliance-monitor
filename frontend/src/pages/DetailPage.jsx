import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import API from "../services/api";

function DetailPage() {
  const { id } = useParams();
  const [data, setData] = useState(null);

  useEffect(() => {
    API.get(`/api/${id}`)
      .then((res) => setData(res.data))
      .catch((err) => console.error(err));
  }, [id]);

  if (!data) {
    return <p className="p-6">Loading...</p>;
  }

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Record Details</h1>

      <div className="bg-white shadow p-4 rounded space-y-2">

        <p>
          <strong>Company:</strong> {data.companyName}
        </p>

        <p>
          <strong>Score:</strong> {data.complianceScore}
        </p>

        <p>
          <strong>Status:</strong> {data.status}
        </p>

        <p>
          <strong>Description:</strong> {data.description}
        </p>

      </div>

      <button
        onClick={() => window.history.back()}
        className="mt-4 bg-gray-800 text-white px-3 py-2 rounded"
      >
        Back
      </button>
    </div>
  );
}

export default DetailPage;