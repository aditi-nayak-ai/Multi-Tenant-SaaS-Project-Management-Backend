import { useNavigate } from "react-router-dom";

export default function Navbar({ selectedOrgName }) {
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem("token");
    navigate("/");
  };

  return (
    <div style={styles.navbar}>
      {/* Left Section */}
      <div style={styles.left}>
        <h3 style={styles.logo}>SaaS Dashboard</h3>
      </div>

      {/* Center Section */}
      <div style={styles.center}>
        {selectedOrgName && (
          <span style={styles.org}>
            Organization: <b>{selectedOrgName}</b>
          </span>
        )}
      </div>

      {/* Right Section */}
      <div style={styles.right}>
        <button style={styles.button} onClick={handleLogout}>
          Logout
        </button>
      </div>
    </div>
  );
}

const styles = {
  navbar: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    padding: "15px 30px",
    backgroundColor: "#1f2937",
    color: "white",
  },
  left: {
    fontSize: "18px",
    fontWeight: "bold",
  },
  center: {
    fontSize: "14px",
  },
  right: {},
  logo: {
    margin: 0,
  },
  org: {
    backgroundColor: "#374151",
    padding: "6px 12px",
    borderRadius: "8px",
  },
  button: {
    backgroundColor: "#ef4444",
    border: "none",
    padding: "8px 14px",
    color: "white",
    borderRadius: "6px",
    cursor: "pointer",
  },
};
