#! env bash
# pip install watchdog
watchmedo shell-command --pattern="*.rst;*.md" --recursive --command="make html" .