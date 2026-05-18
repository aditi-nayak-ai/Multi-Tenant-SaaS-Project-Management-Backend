export default function OrgSwitcher({
  organizations,
  selectedOrg,
  onChange,
}) {
  return (
    <div style={styles.container}>
      <label style={styles.label}>Select Organization:</label>

      <select
        value={selectedOrg || ""}
        onChange={(e) => onChange(e.target.value)}
        style={styles.select}
      >
        {organizations.length === 0 && (
          <option value="">No Organizations</option>
        )}

        {organizations.map((org) => (
          <option key={org.id} value={org.id}>
            {org.name}
          </option>
        ))}
      </select>
    </div>
  );
}

const styles = {
  container: {
    margin: "20px 0",
  },
  label: {
    marginRight: "10px",
    fontWeight: "bold",
  },
  select: {
    padding: "8px 12px",
    borderRadius: "6px",
    border: "1px solid #ccc",
    cursor: "pointer",
  },
};
