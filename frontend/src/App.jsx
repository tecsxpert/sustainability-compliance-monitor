import { Routes, Route } from "react-router-dom";

import Navbar from "./components/Navbar";

import LoginPage from "./pages/LoginPage";
import Dashboard from "./pages/Dashboard";
import ListPage from "./pages/ListPage";
import DetailPage from "./pages/DetailPage";
import FormPage from "./pages/FormPage";
import EditPage from "./pages/EditPage";

function App() {
  return (
    <>
      {/* ✅ Navbar OUTSIDE Routes */}
      <Navbar />

      <Routes>
        <Route path="/" element={<LoginPage />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/list" element={<ListPage />} />
        <Route path="/details/:id" element={<DetailPage />} />
        <Route path="/add" element={<FormPage />} />
        <Route path="/edit/:id" element={<EditPage />} />
      </Routes>
    </>
  );
}

export default App;