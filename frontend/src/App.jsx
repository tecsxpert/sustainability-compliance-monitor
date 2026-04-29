import { Routes, Route } from "react-router-dom";
import ListPage from "./pages/ListPage";
import FormPage from "./pages/FormPage";
import LoginPage from "./pages/LoginPage";
import Dashboard from "./pages/Dashboard";
import DetailPage from "./pages/DetailPage";

function App() {
  return (
    <Routes>
      <Route path="/" element={<ListPage />} />
      <Route path="/add" element={<FormPage />} />
      <Route path="/login" element={<LoginPage />} />
      <Route path="/dashboard" element={<Dashboard />} />
      <Route path="/details/:id" element={<DetailPage />} />
    </Routes>
  );
}

export default App;