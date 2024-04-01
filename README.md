# Online Theatre Reservation API

![Theatre]

## Introduction

This API allows visitors of the local theatre to make reservations online and choose their preferred seats without the need to physically visit the theatre.

## Features

- **User Authentication**: Users can create accounts and authenticate to make reservations.
- **Reservation Management**: Users can browse available performances and reserve seats for their preferred shows.
- **Seat Selection**: The API allows users to select seats from an interactive seating map.
- **Admin Panel**: Administrators can manage performances, theatre halls, and reservations.

## Technologies Used

- Django: Python web framework for backend development.
- Django REST Framework: Toolkit for building RESTful APIs with Django.
- SQLite: Database management system.
- Docker: Containerization platform for easy deployment.
- Swagger/OpenAPI: Documentation tool for API endpoints.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [API Endpoints](#api-endpoints)

## Getting Started

### Prerequisites

- Python 3.x
- Django
- Django REST Framework

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/achernyshovv/theatre-reservation-api

2. **Install dependencies:**

   ```pip install -r requirements.txt```

3. **Run migrations**
    ```
   python manage.py migrate
   ```

4.  **Start development server**
    ```
    python manage.py runserver
    ```

## API Endpoints

- `/api/theatre/performances/`: Get a list of available performances.
- `/api/theatre/reservations/`: Make a reservation for a performance.
- `/api/theatre/seats/`: View and select available seats.
