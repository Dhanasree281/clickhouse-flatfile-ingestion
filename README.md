# ClickHouse & Flat File Ingestion Tool

A full-stack web application that facilitates bidirectional data ingestion between a ClickHouse database and flat files (CSV).  
This project includes a **Flask backend** for connecting to ClickHouse, uploading CSV files, and ingesting data,  
and a **simple HTML/JavaScript frontend** for user interaction.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup & Installation](#setup--installation)
  - [Prerequisites](#prerequisites)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
  - [Running ClickHouse with Docker](#running-clickhouse-with-docker)
- [Usage](#usage)
  - [Connecting to ClickHouse](#connecting-to-clickhouse)
  - [Uploading and Ingesting CSV Data](#uploading-and-ingesting-csv-data)
- [Git & Deployment](#git--deployment)
- [AI Tools and Prompts](#ai-tools-and-prompts)
- [License](#license)

---

## Overview

This project provides a simple yet powerful tool for transferring data between a ClickHouse database and flat files. The backend uses Flask and several Python libraries to handle database connections and CSV parsing, while the frontend offers a user-friendly interface for inputting database credentials, uploading files, and selecting columns.

---

## Features

- **ClickHouse Connection**: Connect to a ClickHouse instance using host, port, user, and JWT (used as a password) for authentication.
- **CSV Upload**: Upload a CSV file to extract column names.
- **Column Selection**: Select which CSV columns to ingest.
- **Data Ingestion**: Ingest CSV data into a ClickHouse table.
- **Bidirectional Flow**: Designed to handle both ClickHouse → Flat File and Flat File → ClickHouse ingestion (extendable as needed).
- **Simple UI**: A clean, easy-to-use HTML interface.

---

## Project Structure



---

## Setup & Installation

### Prerequisites

- **Python 3.x** installed on your system
- **Docker** (for running ClickHouse locally)
- **Git** (for version control)
- A code editor like **VS Code**

### Backend Setup

1. **Navigate to the `backend` folder:**

   Open your terminal and change directory:
   ```bash
   cd path/to/clickhouse-flatfile-ingestion/backend
**###Frontend Setup** 
Navigate to the frontend folder:

Make sure you have an index.html file in the frontend directory.

Check the file contents:

The file should contain HTML and JavaScript code for:

Inputting ClickHouse connection details

Uploading CSV files

Displaying table and column information

Sending requests to the backend API

