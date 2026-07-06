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
RESUME_URL = "https://thebright10.github.io/Portfolio_Sudip/Sudip_Kumar_Adak_Resume.pdf"

# Ensure secrets are available
GMAIL_USER = os.environ.get("GMAIL_USER")
GMAIL_APP_PASSWORD = os.environ.get("GMAIL_APP_PASSWORD")

# Target cities for fresher jobs
TARGET_CITIES = ["Pune, India", "Mumbai, India", "Bangalore, India", "Chennai, India", "Hyderabad, India", "Kolkata, India", "Ahmedabad, India"]
SEARCH_TERM = "Software Developer Fresher"
NUM_JOBS_PER_CITY = 2 # Keep small to avoid rate limits

# Target companies for cold emailing when there is no specific job post
COLD_EMAIL_TARGETS = [
    {"company": "TCS", "hr_email": "careers@tcs.com", "location": "Pan India"},
    {"company": "Infosys", "hr_email": "talentacquisition@infosys.com", "location": "Pan India"},
    {"company": "Wipro", "hr_email": "careers@wipro.com", "location": "Pan India"},
    {"company": "Cognizant", "hr_email": "hrindia@cognizant.com", "location": "Pan India"},
    {"company": "Tech Mahindra", "hr_email": "fresherjobs@techmahindra.com", "location": "Pan India"},
    {"company": "Capgemini", "hr_email": "recruitment.in@capgemini.com", "location": "Pan India"},
    {"company": "Accenture", "hr_email": "india.careers@accenture.com", "location": "Pan India"},
    {"company": "Persistent Systems", "hr_email": "careers@persistent.com", "location": "Pune, India"},
    {"company": "Zoho", "hr_email": "careers@zohocorp.com", "location": "Chennai, India"}
]

def fetch_jobs():
    import random
    # Pick 1 random city each run so we don't scrape too much at once and get blocked
    cities_to_search = random.sample(TARGET_CITIES, 1)
    jobs_list = []
    
    for city in cities_to_search:
        print(f"Scraping online jobs for '{SEARCH_TERM}' in '{city}'...")
        try:
            jobs_df = scrape_jobs(
                site_name=["indeed", "linkedin"],
                search_term=SEARCH_TERM,
                location=city,
                results_wanted=NUM_JOBS_PER_CITY,
                country_indeed='India'
            )
            
            if not jobs_df.empty:
                for _, row in jobs_df.iterrows():
                    jobs_list.append({
                        "title": row.get('title', 'Software Developer (Fresher)'),
                        "company": row.get('company', 'Unknown Company'),
                        "location": row.get('location', city),
                        "url": row.get('job_url', ''),
                        "status": "Apply Online" # Will not generate an email
                    })
        except Exception as e:
            print(f"Error scraping jobs in {city}: {e}")
            
    # Fallback if entirely blocked or no jobs found
    if not jobs_list:
        print("No jobs found via scraper. Using fallback online generic jobs.")
        jobs_list = [
            {"title": "Junior Software Engineer", "company": "IBM", "location": "Bangalore, Karnataka", "url": "https://www.ibm.com/in-en/employment/", "status": "Apply Online"},
            {"title": "Entry Level Frontend Developer", "company": "Amazon", "location": "Hyderabad, Telangana", "url": "https://amazon.jobs", "status": "Apply Online"}
        ]
        
    return jobs_list

def generate_cold_emails():
    """Selects 2 random companies to send a cold application draft to."""
    import random
    targets = random.sample(COLD_EMAIL_TARGETS, 2)
    draft_list = []
    
    for target in targets:
        print(f"Creating cold email draft for {target['company']}...")
        status = save_draft_to_gmail(target)
        draft_list.append({
            "title": "Cold Application (Fresher)",
            "company": target['company'],
            "location": target['location'],
            "url": f"mailto:{target['hr_email']}",
            "status": status
        })
        time.sleep(1)
        
    return draft_list

def save_draft_to_gmail(target):
    """
    Connects to Gmail via IMAP and saves a cold cover letter in the Drafts folder.
    """
    subject = f"Application for Software Developer (Fresher) - {MY_NAME}"
    
    body = f"""Dear HR Team at {target['company']},

I am writing to express my strong interest in joining {target['company']} as a Software Developer or similar entry-level role.

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
    msg['To'] = target['hr_email']
    msg.set_content(body)

    if not GMAIL_USER or not GMAIL_APP_PASSWORD:
        return "Simulated Draft"
        
    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(GMAIL_USER, GMAIL_APP_PASSWORD)
        drafts_folder = '"[Gmail]/Drafts"'
        date_time = imaplib.Time2Internaldate(time.time())
        mail.append(drafts_folder, '', date_time, str(msg).encode('utf8'))
        mail.logout()
        return "Draft Saved"
    except Exception as e:
        return f"Error: {e}"

def update_dashboard_data(all_items):
    """
    Saves the fetched jobs and drafts to jobs.json
    """
    data = {
        "last_updated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_jobs_today": len([i for i in all_items if i['status'] == 'Apply Online']),
        "total_drafts_saved": len([i for i in all_items if 'Saved' in i['status'] or 'Simulated' in i['status']]),
        "jobs": all_items
    }
    
    with open('jobs.json', 'w') as f:
        json.dump(data, f, indent=4)
    print("Updated jobs.json successfully.")

def main():
    print(f"Starting Daily Job Bot for {MY_NAME}...")
    
    # 1. Fetch online jobs (no emails drafted for these)
    online_jobs = fetch_jobs()
    
    # 2. Draft cold emails for companies without specific online postings
    cold_drafts = generate_cold_emails()
    
    # Combine and save
    all_items = online_jobs + cold_drafts
    update_dashboard_data(all_items)
    print("Job Bot execution completed!")

if __name__ == "__main__":
    main()
