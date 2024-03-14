import webbrowser
import time

# List of company names
companies = [
    "exl-service",
    "CGI",
    "Innovaccer",
    "Lenskart-com",
    "RazorPay",
    "Dailyhunt",
    "Meesho",
    "FirstCry",
    "ShareChat",
    "Vedantu-Interview-Kickstart",
    "Zoho",
    "BlackBuck",
    "Yatra",
    "Goibibo",
    "Accolite",
    "HP",
    "Philips",
    "Delhivery",
    "GE",
    "UnitedHealth-Group",
]

# Base URL
base_url = "https://www.linkedin.com/company/{}/jobs/"


def open_job_pages(num_companies):
    for i in range(num_companies):
        company = companies[i]
        url = base_url.format(company.lower())
        webbrowser.open_new(url)
        time.sleep(1)  # Pause for 1 second between opening each company's job page


def main():
    num_companies = int(
        input("Enter the number of company names to display and open job pages for: ")
    )
    open_job_pages(num_companies)


if __name__ == "__main__":
    main()
