
import os

BLUESKY_HANDLE = os.getenv(
    "BLUESKY_HANDLE",
    "tirolerfussball.bsky.social"
)

def main():
    print("UnterHaustria - Ergebnisautomatik")
    print("Bluesky-Konto:", BLUESKY_HANDLE)
    print("Status: Testbetrieb")
    print("TFV- und KFV-Abfrage noch nicht eingerichtet")
    print("Keine Beitraege werden veroeffentlicht.")

if __name__ == "__main__":
    main()
