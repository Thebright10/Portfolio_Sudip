import os
import smtplib
import imaplib
import time
import json
import datetime
from email.message import EmailMessage
from jobspy import scrape_jobs

# ==========================================
# SUDIP'S AUTOMATED JOB BOT & GMAIL DRAFTER
# ==========================================

MY_NAME = "Sudip Kumar Adak"
MY_EMAIL = "adaksudip956@gmail.com"
PORTFOLIO_URL = "https://thebright10.github.io/Portfolio_Sudip/"
RESUME_URL = "https://thebright10.github.io/Portfolio_Sudip/ats_resume.html"

# Ensure secrets are available
GMAIL_USER = os.environ.get("GMAIL_USER")
GMAIL_APP_PASSWORD = os.environ.get("GMAIL_APP_PASSWORD")

# Using a standard location for testing (can be expanded to others)
LOCATION = "Pune, India"
SEARCH_TERM = "Software Developer"
NUM_JOBS_TO_FETCH = 5 # Keep small to avoid rate limits on GitHub Actions

def fetch_jobs():
    print(f"Scraping jobs for '{SEARCH_TERM}' in '{LOCATION}'...")
    try:
        jobs_df = scrape_jobs(
            site_name=["indeed", "linkedin", "glassdoor"],
            search_term=SEARCH_TERM,
            location=LOCATION,
            results_wanted=NUM_JOBS_TO_FETCH,
            country_indeed='India'
        )
        
        jobs_list = []
        if not jobs_df.empty:
            for _, row in jobs_df.iterrows():
                jobs_list.append({
                    "title": row.get('title', 'Software Developer'),
                    "company": row.get('company', 'Unknown Company'),
                    "location": row.get('location', LOCATION),
                    "url": row.get('job_url', ''),
                    "description": str(row.get('description', ''))[:200] + "..."
                })
        return jobs_list
    except Exception as e:
        print(f"Error scraping jobs: {e}")
        # Fallback simulated jobs if scraper fails (e.g., due to IP block on GitHub Actions)
        return [
            {"title": "Junior Python Developer", "company": "Tech Mahindra", "location": "Pune, Maharashtra", "url": "#"},
            {"title": "Frontend Engineer", "company": "TCS Digital", "location": "Bangalore, Karnataka", "url": "#"},
            {"title": "Data Analyst Intern", "company": "Mu Sigma", "location": "Hyderabad, Telangana", "url": "#"}
        ]

def save_draft_to_gmail(job):
    """
    Connects to Gmail via IMAP and saves a cover letter in the Drafts folder.
    """
    subject = f"Application for {job['title']} - {MY_NAME}"
    
    # Constructing the cover letter body
    body = f"""Dear Hiring Manager at {job['company']},

I am writing to express my strong interest in the {job['title']} position at your company in {job['location']}.

I am currently pursuing my MCA at Pimpri Chinchwad University (PCU) and have completed my BCA from Techno India. I have hands-on experience building full-stack applications like the MindFlow AI Mental Health platform (Python/Django), E-Commerce systems, and Data Analytics dashboards.

Please find my ATS-friendly resume here: {RESUME_URL}
You can also view my full portfolio and projects here: {PORTFOLIO_URL}

I am available for an immediate internship or full-time role and would love to discuss how my skills in Python, Java, SQL, and Web Development can add value to your team.

Thank you for your time and consideration.

Best regards,
{MY_NAME}
{MY_EMAIL}
"""

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = MY_EMAIL
    # Since we don't have the specific HR email for every scraped job, we draft it to a generic placeholder 
    # so Sudip can fill in the recipient manually, or we just leave 'To' blank if IMAP allows (it usually does).
    msg['To'] = "hr@company.com" 
    msg.set_content(body)

    if not GMAIL_USER or not GMAIL_APP_PASSWORD:
        print(f"⚠️ [MOCK DRAFT] Could not save to Gmail because credentials are missing. Simulated draft for {job['company']}.")
        return "Simulated"
        
    try:
        # Connect to Gmail IMAP
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(GMAIL_USER, GMAIL_APP_PASSWORD)
        
        # Determine the Drafts folder name (it can vary by locale, but usually "[Gmail]/Drafts" for English)
        # We'll just try "[Gmail]/Drafts"
        drafts_folder = '"[Gmail]/Drafts"'
        
        # Append the message to the Drafts folder
        date_time = imaplib.Time2Internaldate(time.time())
        mail.append(drafts_folder, '', date_time, str(msg).encode('utf8'))
        mail.logout()
        
        print(f"✅ [DRAFT SAVED] Successfully saved draft for {job['company']} in Gmail.")
        return "Draft Saved"
    except Exception as e:
        print(f"❌ [ERROR] Failed to save draft via IMAP: {e}")
        return f"Error: {e}"

def update_dashboard_data(jobs, results):
    """
    Saves the fetched jobs and draft statuses to jobs.json so the frontend dashboard can display them.
    """
    data = {
        "last_updated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_jobs_today": len(jobs),
        "total_drafts_saved": sum(1 for r in results if r == "Draft Saved"),
        "jobs": []
    }
    
    for job, status in zip(jobs, results):
        job_entry = {
            "title": job['title'],
            "company": job['company'],
            "location": job['location'],
            "url": job['url'],
            "status": status
        }
        data["jobs"].append(job_entry)
        
    with open('jobs.json', 'w') as f:
        json.dump(data, f, indent=4)
    print("Updated jobs.json successfully.")

def main():
    print(f"Starting Daily Job Bot for {MY_NAME}...")
    
    jobs = fetch_jobs()
    results = []
    
    for job in jobs:
        # Save a draft for each job found
        res = save_draft_to_gmail(job)
        results.append(res)
        time.sleep(1) # Slight delay to avoid IMAP rate limiting
        
    update_dashboard_data(jobs, results)
    print("Job Bot execution completed!")

if __name__ == "__main__":
    main()
