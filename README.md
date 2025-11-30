text
# Django + React Analytics Dashboard

This project is a full-stack analytics dashboard:

- **Backend:** Django + Django REST Framework + SQLite, with filtering and aggregation APIs.
- **Frontend:** React + Chart.js (via `react-chartjs-2`) + Bootstrap.
- **Data:** Imported from `jsondata.json` via a custom management command.

## 1. Prerequisites

- Python 3.10+
- Node.js (LTS) and npm
- Git (optional, for version control)

## 2. Backend setup

cd django-react-dashboard

python -m venv venv

Windows:
venv\Scripts\activate

macOS/Linux:
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

cd backend
python manage.py makemigrations
python manage.py migrate

text

Place your `jsondata.json` file inside the `backend/` folder, then run:

python manage.py import_json --file jsondata.json

text

Start the Django development server:

python manage.py runserver

text

Backend will be available at `http://127.0.0.1:8000/api/`.

## 3. Frontend setup

In a new terminal window:

cd django-react-dashboard/frontend
npm install
npm start

text

Frontend will run at `http://localhost:3000`.

## 4. API endpoints

- `GET /api/entries/` — paginated list with filters:
  - Query params: `page`, `page_size`, `search`, `topic`, `sector`, `region`, `country`, `city`, `pestle`, `source`, `swot`, `start_year`, `end_year`, `published_from`, `published_to`, `ordering`.
- `GET /api/entries/<id>/` — entry detail.
- `GET /api/filters/` — distinct values for dropdowns.
- `GET /api/aggregations/intensity-by-year/` — average intensity per year.
- `GET /api/aggregations/likelihood-trend/?topic=<topic>` — likelihood trend.

## 5. Charts and interactions

- **Bar chart:** average intensity by year.
- **Line chart:** trend of likelihood over years.
- **Pie chart:** distribution of topics.
- **Scatter chart:** relevance vs intensity, colored by region, bubble size = likelihood.
- **Table:** paginated list of filtered entries.

All charts update when filters in the UI change.

## 6. Packaging for submission

1. Stop servers.
2. Remove the `venv/` folder if present.
3. From `django-react-dashboard`, create a zip:

cd ..
zip -r django-react-dashboard.zip django-react-dashboard -x "django-react-dashboard/venv/*" "django-react-dashboard/db.sqlite3"

text

4. Upload `django-react-dashboard.zip` to Google Drive.
5. Add screenshots of the UI and paste the short report (see below) into a Google Docs file.
6. Share the Drive folder and paste the link into the Google Form.

## 7. Short report template (example)

Use this as a starting point for your 200–400 word report in Google Docs:

> This project implements a full-stack analytics dashboard built with Django REST Framework on the backend and React with Chart.js on the frontend. The data originates from a JSON file that is imported into a SQLite database using a custom Django management command.
>
> The backend exposes a set of RESTful endpoints to list, filter, and inspect individual records. It also provides aggregation endpoints that calculate the average intensity by year and the trend of likelihood over time. These aggregations allow the frontend to efficiently display bar and line charts without transferring large raw datasets.
>
> The frontend consumes these APIs using Axios and renders interactive visualizations with `react-chartjs-2`. Users can filter the data by topic, sector, region, country, city, PESTLE category, source, SWOT type, and year ranges. When filters change, the dashboard refreshes the charts and the paginated data table, making it easy to explore relationships between intensity, relevance, and likelihood across regions and topics.
>
> From the sample dataset, several insights emerge. For example, some topics show steadily increasing likelihood over the years, while others remain flat or decline. Certain regions exhibit higher average intensity, indicating that the associated issues may be more impactful there. The topic distribution chart highlights which themes dominate the dataset. Overall, the dashboard demonstrates how to combine Django, REST APIs, and React-based visualizations to turn a raw JSON dataset into an interactive analytical tool.

## 8. Submission checklist

- [ ] `django-react-dashboard.zip` uploaded to Google Drive.
- [ ] Contains backend (`backend/`) and frontend (`frontend/`) code.
- [ ] Contains `requirements.txt` and `README.md`.
- [ ] Contains example `jsondata.json` or instructions on where to place it.
- [ ] Screenshots of the dashboard in the same Drive folder.
- [ ] Google Docs file with short report (copied from template and customized).
- [ ] Google Form filled with:
  - Name, email, and other requested details.
  - GitHub/Drive link to the project (if requested).
  - Link to the Google Drive folder containing the zip, screenshots, and report.
F. Example Google Form answers (what to fill)
Project title: “Django + React Analytics Dashboard”

Tech stack: “Django 4, Django REST Framework, SQLite, React, Chart.js, Bootstrap”

Repository / Drive link: paste the shared Google Drive folder URL.

Setup instructions: “See README.md in the root of the project. Steps: create virtualenv, install Python dependencies, run migrations, import jsondata.json, run Django server, then run npm install and npm start in frontend.”

Summary / approach: copy and slightly customize the short report template above.

G. Final runbook (fresh machine to running UI)
From nothing to full dashboard:

bash
# 1. Clone or unzip project
cd django-react-dashboard

# 2. Python environment
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

# 3. Backend DB + import
cd backend
python manage.py makemigrations
python manage.py migrate

# Copy your jsondata.json into backend/ if not already there
python manage.py import_json --file jsondata.json

# 4. Run backend server (keep this terminal open)
python manage.py runserver
Open a new terminal:

bash
# 5. Frontend
cd django-react-dashboard/frontend
npm install
npm start
Then:

Open http://localhost:3000 to use the dashboard.

Test backend via curl "http://127.0.0.1:8000/api/entries/?page=1" to confirm data is returned.

This completes the full backend + frontend implementation and submission flow.