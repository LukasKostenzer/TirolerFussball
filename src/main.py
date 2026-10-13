
import os
import json
import urllib.request
import urllib.error

def main():
    print("UnterHaustria - Bluesky Verbindungstest")

    handle = os.environ.get("BLUESKY_HANDLE")
    password = os.environ.get("BLUESKY_APP_PASSWORD")

    if not handle or not password:
        raise RuntimeError("Bluesky Secrets fehlen!")

    url = "https://bsky.social/xrpc/com.atproto.server.createSession"

    payload = json.dumps({
        "identifier": handle,
        "password": password
    }).encode("utf-8")

    request = urllib.request.Request(
        url,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            result = json.load(response)

        if result.get("did"):
            print("Bluesky Anmeldung erfolgreich!")
            print("Konto:", handle)
            print("DID:", result["did"])
            print("TESTMODUS: Kein Beitrag veröffentlicht.")
        else:
            raise RuntimeError("Keine DID erhalten.")

    except urllib.error.HTTPError as error:
        print("Bluesky Anmeldung fehlgeschlagen.")
        print("HTTP-Status:", error.code)
        raise RuntimeError("Verbindungstest fehlgeschlagen.") from None

if __name__ == "__main__":
    main()
