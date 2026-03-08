import { Routes, Route } from "react-router-dom";
import { SignIn, SignUp } from "@clerk/clerk-react";
import LandingPage from "./pages/LandingPage";
import StudentDashboard from "./pages/StudentDashboard";
import TeacherDashboard from "./pages/TeacherDashboard";
import AuthLayout from "./components/ui/AuthLayout";

export default function App() {
  return (
    <Routes>
      {/* Public */}
      <Route path="/" element={<LandingPage />} />

      {/* Auth pages */}
      <Route
        path="/sign-in/*"
        element={
          <AuthLayout>
            <SignIn routing="path" path="/sign-in" />
          </AuthLayout>
        }
      />
      <Route
        path="/sign-up/*"
        element={
          <AuthLayout>
            <SignUp routing="path" path="/sign-up" />
          </AuthLayout>
        }
      />

      {/* Student area */}
      <Route path="/dashboard" element={<StudentDashboard />} />

      {/* Teacher area */}
      <Route path="/teacher" element={<TeacherDashboard />} />

      {/* 404 fallback */}
      <Route
        path="*"
        element={
          <div
            style={{
              display: "flex",
              flexDirection: "column",
              alignItems: "center",
              justifyContent: "center",
              minHeight: "100vh",
              gap: "16px",
            }}
          >
            <h1 style={{ fontSize: "3rem", fontWeight: 700, color: "var(--accent)" }}>404</h1>
            <p style={{ color: "var(--text-muted)" }}>Page not found</p>
            <a href="/" className="btn-primary" style={{ marginTop: "8px" }}>
              ← Back to Home
            </a>
          </div>
        }
      />
    </Routes>
  );
}
