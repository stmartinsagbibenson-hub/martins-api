# Week 8 Practice: From API Data to Your Own Analytics API

**Goal:** Pull real data from an API, think through questions about it, answer them in Python, then turn your answers into **FastAPI endpoints** in your own repo, shipped with a clean Git history.

**Source API:** `https://week2-people-ops-api.vercel.app/api/people-ops`

---

## 0. Know your data first

Call the API and look before you code. Each record looks like this:

```json
{
  "employee_id": "EMP-3001",
  "department": "Sales",
  "role": "Associate",
  "application_date": "2025-01-08",
  "offer_accepted_date": "2025-01-18",
  "start_date": "2025-01-25",
  "exit_date": "",
  "status": "Active"
}
```

The response also has `record_count`, a `schema`, and a `query` block with `start`, `end`, `department`, `status`.

**Explore questions**
1. What status code do you get back? What would a `404` or `500` have meant?
2. What is the top-level type of the JSON (list or dict)? Where do the employees actually live?
3. How many records are there? Does it match `record_count`?
4. Try adding `?department=Sales` or `?status=Active` to the URL. What changes? What does the `query` block tell you?
5. Find the **odd records**. Which ones have blank fields or a blank `status`? What would break if you ignored them?

---

## 1. Analyze in Python (scripts first)

Use `requests`, then plain loops, conditionals and dictionaries.

**For every question, save the code you wrote *and* the answer it gave you.** Keep them together in an `answers.md` file in your repo, like this:

````markdown
### Q1. Sales employees
```python
# the code you ran
```
**Answer:**
```
# the output you got
```
**How I got there:** one sentence in your own words.
````

### Warm-up
1. List the `employee_id` of every employee in **Sales**.
2. List all **Active** employees.
3. How many employees are in each department? (Hint: a dictionary as a counter.)
4. How many are Active, Exited, Candidate, or blank?
5. What distinct roles exist? Which department has which roles?

### Core
6. Which employees **exited**? Show their department and exit date.
7. Which department has had the most exits? Which has had none?
8. For each employee with an offer, how many days between `application_date` and `offer_accepted_date`? Use `datetime`.
9. What is the **average time-to-offer** per department?
10. What is the average days between `offer_accepted_date` and `start_date`?
11. **Tenure:** for exited employees, how many days from `start_date` to `exit_date`? Who stayed the shortest?
12. How many people were hired (started) in each month? Which month was busiest?

### Stretch (think before you code)
13. Which department is **slowest to hire**? Defend your answer with numbers.
14. What is the **attrition rate** per department (exited ÷ total hired)? Is a small sample misleading here?
15. How many employees were employed at some chosen date (started on or before it, not exited before it)?
16. Which records are **invalid** (missing dates, missing status, exit before start)? Write a function `is_valid(record)` and use it to clean the data.

---

## 2. Turn answers into endpoints (FastAPI)

Your FastAPI app calls the People Ops API, processes the data, and returns **your own** JSON. Build these one at a time:

| Endpoint | Returns |
|---|---|
| `GET /employees` | all clean records (optional `?department=` and `?status=` filters) |
| `GET /employees/active` | only Active employees |
| `GET /departments/{name}/employees` | employees in one department (e.g. Sales) |
| `GET /stats/headcount` | count per department |
| `GET /stats/status-summary` | count by status |
| `GET /stats/exits` | exited employees with tenure in days |
| `GET /stats/time-to-offer` | average days to offer, per department |
| `GET /stats/hiring-by-month` | hires per month |
| `GET /data-quality` | the invalid records and why they are invalid |

**For each endpoint, add to `answers.md`:** the endpoint code and the JSON response you got when you called it.

**Build rules**
- Put the fetch logic in **one function** (e.g. `fetch_people_ops()`) that every endpoint reuses.
- Handle failure: if the upstream API is down or returns a non-200 status, return a clear error with a proper status code, not a crash.
- Unknown department? Return `404` with a helpful message.
- Keep calculation logic in plain functions so you can test them without the server.

**Think about it**
- Should each request call the upstream API again, or should you cache the data for a while? What are the trade-offs (fresh vs fast)?
- Why return counts *and* the records in some endpoints?

---

## 3. Keep secrets and config out of code

1. Move the API URL into a `.env` file as `PEOPLE_OPS_URL` and read it in Python (see below).
2. Add `.env` to `.gitignore` **before** your first commit.
3. Commit a `.env.example` with fake values so others know what to set.
4. On Vercel, add the same variable in project settings.
5. *Discuss:* this URL is not secret, so why practice this now? What happens the day it needs an API key?

**How to read an environment variable**

Create a `.env` file in your project root (one `NAME=value` per line, no quotes or spaces around `=`):

```
PEOPLE_OPS_URL=https://week2-people-ops-api.vercel.app/api/people-ops
```

Install the helper: `pip install python-dotenv` (and add it to `requirements.txt`). Then in Python:

```python
import os
from dotenv import load_dotenv

load_dotenv()                      # loads .env into the environment
url = os.getenv("PEOPLE_OPS_URL")  # returns None if the variable is missing

if url is None:
    raise RuntimeError("PEOPLE_OPS_URL is not set. Check your .env file.")
```

- `os.getenv` reads a value from the environment. `load_dotenv()` fills that environment from your `.env` file, which is how it works on your laptop.
- On Vercel there is no `.env` file. The variable you add in project settings is already in the environment, so the same `os.getenv` line works unchanged.
- `os.getenv("NAME", "fallback")` returns a default when the variable is missing. Think about when a default is helpful and when failing loudly is safer.
- **Check:** change the variable name in `.env` on purpose and run your code. What happens? Is the error message helpful?

---

## 4. Git and GitHub workflow

Treat this as a real team project.

1. Create a branch per feature: `feature/active-employees`, `feature/headcount-stats`, and so on.
2. Make **small commits with clear messages** (`Add active employees endpoint`, not `update`).
3. Push each branch and open a **Pull Request** with a short description of what changed and how to test it.
4. Review a classmate's PR (or your instructor's): leave at least one comment or suggestion.
5. Merge, then pull `main` locally and delete the merged branch.
6. **Read up on `git log --oneline`.** Search for it or ask your AI tool, and try `git log` with and without `--oneline` to see the difference. Write down in your own words what each part of a line means (the short code and the message). Then run it on your repo and paste the output into your README. Does it read like a story of your project? Could a stranger understand what you did from the messages alone? If not, how would you write the messages next time?

Include a `README.md` with: what the project does, how to run it, the endpoint list, and the env variables needed.

---

## 5. AI integration

- Paste one record and the `schema` into an AI tool and ask it to explain every field in plain English. Then check its explanation against the real data.
- Ask AI how to compute days between two date strings in Python. Test its code on three records by hand.
- Ask AI to review one of your endpoints for bugs or missing edge cases. Decide which suggestions are worth taking.
- **Rule:** you must be able to explain every line you commit, whether you or AI wrote it.

---

## 6. Record a video explaining everything

Record a screen video (about 5 to 10 minutes) walking through all you did. Explain the **why**, not just the what. Cover:

1. The API and its data: what a record looks like and the odd records you found.
2. Your code for a few questions you picked: read the code aloud and explain your thinking.
3. Your FastAPI app running: call a few endpoints and show the responses.
4. Your env variable setup (never show real secrets on screen).
5. Your GitHub repo: branches, a pull request, and your `git log --oneline` output.
6. One thing that went wrong, how you debugged it, and what you learned.

Add the video link to your README. Loom, Zoom, OBS or your phone's screen recorder all work.

---

## Sanity checks (verify your results against these)

- Total records: **92**, of which 90 are normal and **2 are odd** (one `Candidate` with no offer, one with a blank status).
- Sales employees: **18**.
- Exited employees: **5**, one each from Sales, Delivery, People Ops, Engineering, and Customer Success.
- Active employees: **85**.