from devpost import scrapeDevpost
from mongodb import addHackathonsToMongoDB

if __name__ == "__main__":
    addHackathonsToMongoDB(scrapeDevpost())