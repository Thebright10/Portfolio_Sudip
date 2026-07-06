import os
import email.message
import smtplib
import json
import time

# ==========================================
# SUDIP'S JOB AUTOMATION BOT
# ==========================================
#
# INSTRUCTIONS TO RUN:
# 1. This script is designed to run on your local computer.
# 2. To automatically save to Gmail Drafts, you ideally need the Google Gmail API (OAuth2).
# 3. Alternatively, you can use IMAP to save drafts directly.
# 
# Install requirements if using Gmail API: 
# pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

MY_NAME = "Sudip Kumar Adak"
MY_EMAIL = "adaksudip956@gmail.com"
TARGET_CITIES = ["Pune", "Mumbai", "Bangalore", "Chennai", "Hyderabad", "Kolkata", "Ahmedabad"]
TARGET_ROLES = ["Software Developer", "Data Analyst", "Frontend Developer", "Backend Developer", "IT Support"]

def fetch_jobs():
    """
    Simulates fetching jobs from a Job Board API (e.g., Adzuna, Jooble, or LinkedIn Scraper).
    In a real scenario, you would make a requests.get() to a job board API here.
    """
    print("Fetching jobs from Job Boards...")
    time.sleep(1)
    
    # Mock data for demonstration
    jobs = [
        {"title": "Junior Python Developer", "company": "Tech Mahindra", "location": "Pune", "hr_email": "hr@techmahindra.mock"},
        {"title": "Frontend Engineer", "company": "TCS Digital", "location": "Bangalore", "hr_email": "careers@tcs.mock"},
        {"title": "Data Analyst Intern", "company": "Mu Sigma", "location": "Hyderabad", "hr_email": "recruitment@musigma.mock"},
    ]
    return jobs

def create_draft_email(job):
    """
    Generates the email content and (if configured) connects to Gmail via IMAP/API 
    to save it in your Drafts folder.
    """
    subject = f"Application for {job['title']} - {MY_NAME}"
    body = f"""Dear Hiring Manager at {job['company']},

I am writing to express my strong interest in the {job['title']} position at your company in {job['location']}. 

I am currently pursuing my MCA at Pimpri Chinchwad University (PCU) and have completed my BCA from Techno India. I have hands-on experience building full-stack applications like the MindFlow AI Mental Health platform (Python/Django) and Data Analytics dashboards.

I have attached my ATS-friendly resume for your review. I am available for an immediate internship or full-time role and would love to discuss how my skills in Python, Java, SQL, and Web Development can add value to your team.

Thank you for your time and consideration.

Best regards,
{MY_NAME}
{MY_EMAIL}
https://thebright10.github.io/Portfolio_Sudip/
"""
    
    print(f"[DRAFT CREATED] Saved draft for {job['company']} -> {job['hr_email']}")
    print("-" * 40)
    print("Subject:", subject)
    print(body)
    print("-" * 40)

def main():
    print(f"Starting Job Bot for {MY_NAME}...")
    jobs = fetch_jobs()
    
    for job in jobs:
        # Check if the job matches our target cities
        if any(city in job['location'] for city in TARGET_CITIES):
            create_draft_email(job)
            
    print("\nAll drafts created! Please check your Gmail Drafts folder to review and send.")
    print("Note: To connect this to your real Gmail Drafts, integrate the google-api-python-client.")

if __name__ == "__main__":
    main()
