from devpost import scrapeDevpost
from mongodb import addHackathonsToMongoDB
from devfolio import scrapeDevfolio

if __name__ == "__main__":
    devfolioHackthons = scrapeDevfolio()
    devpostHackthons = scrapeDevpost()
    hackathons = devfolioHackthons + devpostHackthons
    addHackathonsToMongoDB(hackathons)
