#!/usr/bin/env python3
"""Generate a GitHub App installation token using local template defaults or env vars."""

import argparse
import json
import os
import subprocess
import sys
import time

import jwt


DEFAULT_APP_ID = os.environ.get("GITHUB_APP_ID", "123456")
DEFAULT_INSTALLATION_ID = os.environ.get("GITHUB_INSTALLATION_ID", "12345678")
DEFAULT_KEY_PATH = os.environ.get(
    "GITHUB_APP_PRIVATE_KEY_PATH",
    "/home/agent0/workspace/example-project/secrets/github-app-private-key.pem",
)


def get_token(app_id: str, installation_id: str, private_key: str) -> str:
    payload = {
        "iat": int(time.time()),
        "exp": int(time.time()) + 600,
        "iss": app_id,
    }
    jwt_token = jwt.encode(payload, private_key, algorithm="RS256")

    result = subprocess.run(
        [
            "curl",
            "-s",
            "-X",
            "POST",
            "-H",
            f"Authorization: Bearer {jwt_token}",
            "-H",
            "Accept: application/vnd.github+json",
            f"https://api.github.com/app/installations/{installation_id}/access_tokens",
        ],
        capture_output=True,
        text=True,
        check=True,
    )

    data = json.loads(result.stdout)
    if "token" not in data:
        raise RuntimeError(f"Failed to get token: {data}")
    return data["token"]


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a GitHub App installation token")
    parser.add_argument("--app-id", default=DEFAULT_APP_ID)
    parser.add_argument("--installation-id", default=DEFAULT_INSTALLATION_ID)
    parser.add_argument("--key-file", default=DEFAULT_KEY_PATH)
    args = parser.parse_args()

    if not args.key_file:
        print("Error: --key-file required", file=sys.stderr)
        sys.exit(1)

    with open(args.key_file) as f:
        private_key = f.read()

    print(get_token(args.app_id, args.installation_id, private_key))


if __name__ == "__main__":
    main()
