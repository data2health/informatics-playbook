#! env bash
# pip install watchdog
watchmedo shell-command --pattern="*.rst;*.md;*.py" --recursive --command="make html" .