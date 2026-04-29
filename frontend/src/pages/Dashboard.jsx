import { useEffect, useState } from "react";
import API from "../services/api";

function Dashboard() {
  const [stats, setStats] = useState(null);

  useEffect(() => {
    API.get("/api/stats")
      .then((res) => {
        setStats(res.data);
      })
      .catch((err) => {
        console.error("Error loading stats:", err);
      });
  }, []);

  if (!stats) {
    return <p className="p-6">Loading...</p>;
  }

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-6">Dashboard</h1>

      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">

        <div className="bg-blue-500 text-white p-4 rounded shadow">
          <h2>Total Records</h2>
          <p className="text-xl font-bold">{stats.total}</p>
        </div>

        <div className="bg-green-500 text-white p-4 rounded shadow">
          <h2>Compliant</h2>
          <p className="text-xl font-bold">{stats.compliant}</p>
        </div>

        <div className="bg-red-500 text-white p-4 rounded shadow">
          <h2>Non-Compliant</h2>
          <p className="text-xl font-bold">{stats.nonCompliant}</p>
        </div>

        <div className="bg-yellow-500 text-white p-4 rounded shadow">
          <h2>Average Score</h2>
          <p className="text-xl font-bold">
            {stats.avgScore ? stats.avgScore.toFixed(2) : 0}
          </p>
        </div>

      </div>
    </div>
  );
}

export default Dashboard;