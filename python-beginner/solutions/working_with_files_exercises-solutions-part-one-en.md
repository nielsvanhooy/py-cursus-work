# ✅ Answers

### 1. Basic SELECT
```sql
SELECT hostname, dep.name AS department
FROM Device d
JOIN Department dep ON d.dept_id = dep.dept_id;
```

---

### 2. Filtering
```sql
SELECT hostname, assigned_date
FROM Device
WHERE assigned_date > '2023-02-01';
```

---

### 3. One-to-Many (JOIN)
```sql
SELECT d.hostname, d.ip_address
FROM Device d
JOIN Department dep ON d.dept_id = dep.dept_id
WHERE dep.name = 'IT';
```

---

### 4. Aggregation
```sql
SELECT dep.name AS department, COUNT(d.device_id) AS device_count
FROM Department dep
LEFT JOIN Device d ON dep.dept_id = d.dept_id
GROUP BY dep.name;
```

---

### 5. Many-to-Many (JOIN)
```sql
SELECT d.hostname, d.ip_address
FROM User u
JOIN UserDevice ud ON u.user_id = ud.user_id
JOIN Device d ON ud.device_id = d.device_id
WHERE u.name = 'Alice';
```

---

### 6. Reverse Many-to-Many
```sql
SELECT u.name
FROM User u
JOIN UserDevice ud ON u.user_id = ud.user_id
JOIN Device d ON ud.device_id = d.device_id
WHERE d.hostname = 'printer01';
```

---

### 7. Combined Join
```sql
SELECT dep.name AS department, u.name AS user, d.hostname AS device
FROM Department dep
JOIN Device d ON dep.dept_id = d.dept_id
JOIN UserDevice ud ON d.device_id = ud.device_id
JOIN User u ON ud.user_id = u.user_id
ORDER BY dep.name, u.name;
```

---

### 8. Extra Challenge
```sql
SELECT d.hostname, COUNT(ud.user_id) AS user_count
FROM Device d
JOIN UserDevice ud ON d.device_id = ud.device_id
GROUP BY d.device_id
HAVING COUNT(ud.user_id) > 1;
```
