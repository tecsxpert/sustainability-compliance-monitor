import { Routes, Route } from "react-router-dom";

import LoginPage from "./pages/LoginPage";
import Dashboard from "./pages/Dashboard";
import ListPage from "./pages/ListPage";
import DetailPage from "./pages/DetailPage";
import FormPage from "./pages/FormPage";
import EditPage from "./pages/EditPage";

function App() {
  return (
    <Routes>

      {/* 🔐 Login */}
      <Route path="/" element={<LoginPage />} />

      {/* 📊 Dashboard */}
      <Route path="/dashboard" element={<Dashboard />} />

      {/* 📋 List */}
      <Route path="/list" element={<ListPage />} />

      {/* 🔍 Detail */}
      <Route path="/details/:id" element={<DetailPage />} />

      {/* ➕ Create */}
      <Route path="/add" element={<FormPage />} />

      {/* ✏️ Edit */}
      <Route path="/edit/:id" element={<EditPage />} />

    </Routes>
  );
}

export default App;