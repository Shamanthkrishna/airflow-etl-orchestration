# Workflow Orchestration with Apache Airflow (Mini Project)

## 📌 Overview

This project demonstrates **workflow orchestration using Apache Airflow**.
It defines a simple **ETL (Extract → Transform → Load)** pipeline as an Airflow DAG to showcase:

* DAG structure and task dependencies
* Scheduling and orchestration
* Monitoring pipeline runs through the Airflow UI

The pipeline has **3 tasks**:

1. **Extract** → Read data from a CSV file
2. **Transform** → Process the data with `pandas`
3. **Load** → Store the transformed data into a **SQLite database**

---

## ⚙️ Tech Stack

* **Apache Airflow** (workflow orchestration)
* **Python** (task logic, data processing with pandas)
* **SQLite** (lightweight database for storage)
* **Docker / Local Airflow environment** (optional for running)

---

## 📂 Project Structure

```
airflow-etl-orchestration/
│── dags/
│   └── etl_pipeline.py    # Main Airflow DAG
│── data/
│   └── input_data.csv     # Sample input CSV
│── output/
│   └── etl_output.db      # SQLite DB after pipeline run
│── requirements.txt       # Python dependencies
│── README.md              # Project documentation
```

---

## 🚀 How It Works

1. **Extract Task**

   * Reads raw data from `input_data.csv`

2. **Transform Task**

   * Uses `pandas` to clean/process data
   * Example: handle nulls, derive new columns, filter records

3. **Load Task**

   * Writes the transformed data into a SQLite database (`etl_output.db`)

---

## ▶️ Running the Project

### 1. Setup Environment

```bash
# Clone the repo
git clone https://github.com/your-username/airflow-etl-orchestration.git
cd airflow-etl-orchestration

# Install requirements
pip install -r requirements.txt
```

### 2. Start Airflow

```bash
# Initialize Airflow DB
airflow db init

# Start webserver & scheduler
airflow webserver --port 8080
airflow scheduler
```

### 3. Access UI

* Open [http://localhost:8080](http://localhost:8080)
* Enable and trigger the DAG **etl\_pipeline**

---

## 📊 Example DAG View

The DAG looks like this in Airflow:

```
extract_csv >> transform_data >> load_to_sqlite
```

---

## 📌 Key Learnings

* How to define DAGs and tasks in Airflow
* Using `PythonOperator` to run custom Python functions
* Managing task dependencies (`>>`)
* Scheduling jobs with Airflow
* Monitoring pipelines in the Airflow UI

---

## ✅ Extensions (Future Improvements)

* Add data validation checks before loading
* Send email alerts on pipeline failures
* Parameterize input file path with `dagrun.conf`
* Run with **Dockerized Airflow** (`docker-compose.yml`)

