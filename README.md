# Smart Parking System (Backend)

A backend service built with Django and Django REST Framework (DRF) to manage a parking lot: track parking slots, register vehicles entering and exiting, calculate fees based on duration, and provide real‑time slot availability. Supports role-based authentication (admin / parking staff) and basic reporting.

## 🚗 Features

- Manage parking slots (create, read, update, delete) — admin only  
- List all parking slots — accessible to authenticated users  
- Register vehicle entry — for parking staff  
- Register vehicle exit and calculate parking fee — for parking staff  
- Track vehicle history (entry and exit times, associated slot)  
- User authentication with roles (admin vs staff)  
- JSON-based REST API with clear request/response format  

## 📦 Tech Stack & Dependencies

- Python (3.10+)  
- Django  
- Django REST Framework (DRF) :contentReference[oaicite:2]{index=2}  
- (Optional future: drf‑spectacular or DRF‑yasg for API schema / documentation) :contentReference[oaicite:3]{index=3}  

## 🔧 Setup & Run Locally

1. Clone the repository  
   ```bash
   git clone https://github.com/Fabiola-I/smart-parking-backend.git
   cd smart-parking-backend
