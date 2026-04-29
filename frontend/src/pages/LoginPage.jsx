import { useState } from "react";
import API from "../services/api";

function LoginPage() {
  const [form, setForm] = useState({
    username: "",
    password: "",
  });

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  };

  const handleLogin = async (e) => {
    e.preventDefault();

    try {
      const res = await API.post("/auth/login", {
        username: form.username,
        password: form.password,
      });

      localStorage.setItem("token", res.data.token);

      alert("Login successful!");
      window.location.href = "/";
    } catch (err) {
      console.error(err);
      alert("Invalid credentials");
    }
  };

  return (
    <div className="p-6">
      <h1 className="text-xl font-bold mb-4">Login</h1>

      <form onSubmit={handleLogin} className="space-y-4">

        {/* USERNAME */}
        <input
          name="username"                // ✅ IMPORTANT
          placeholder="Username"
          value={form.username}
          onChange={handleChange}
          className="border p-2 w-full"
        />

        {/* PASSWORD */}
        <input
          type="password"
          name="password"                // ✅ IMPORTANT
          placeholder="Password"
          value={form.password}
          onChange={handleChange}
          className="border p-2 w-full"
        />

        <button
          type="submit"
          className="bg-blue-500 text-white px-4 py-2"
        >
          Login
        </button>
      </form>
    </div>
  );
}

export default LoginPage;