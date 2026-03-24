<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=4f46e5&height=180&section=header&text=Travel%20Website%20DB&fontSize=56&fontColor=ffffff&fontAlignY=38&animation=fadeIn" width="100%"/>

<br/>

[![Typing SVG](https://readme-typing-svg.demolab.com?font=DM+Mono&size=18&duration=3000&pause=1000&color=4F46E5&center=true&vCenter=true&multiline=true&repeat=true&width=600&height=80&lines=Dual-Database+Architecture;RDBMS+%2B+NoSQL+Implementation;Travel+Platform+Data+Modeling)](https://github.com/Joeljozzz/Travel_Website_Database)

<br/>

[![Repository](https://img.shields.io/badge/GitHub-Repo-0B0D0E?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Joeljozzz/Travel_Website_Database)
[![Built by Joel](https://img.shields.io/badge/Built%20by-Joel%20Jose-4f46e5?style=for-the-badge)](https://github.com/Joeljozzz)

<br/>

</div>

---

## System Objective

Modern web applications require flexible data storage solutions. This project is a travel website architecture built to showcase the integration and practical implementation of both Relational (RDBMS) and Non-Relational (NoSQL) databases within the same ecosystem. By splitting the data model, the system optimizes for both structural integrity in transactions and flexible scalability in unstructured data.

---

## Architecture Flow

```text
┌─────────────────────────────────────────────────────────┐
│  CLIENT TIER               [Travel Web Interface]       │
│  User interactions, search queries, and bookings        │
├─────────────────────────────────────────────────────────┤
│  APPLICATION TIER          [Backend Server]             │
│  Routing logic and database connection pooling          │
├─────────────────────────┬───────────────────────────────┤
│  DATA TIER (RDBMS)      │  DATA TIER (NoSQL)            │
│  [Database 1]           │  [Database 2]                 │
│  Structured data        │  Unstructured / Graph data    │
│  (Users, Bookings)      │  (Reviews, Logs, Relations)   │
└─────────────────────────┴───────────────────────────────┘
```
