import os
import shutil
import re
import subprocess
from datetime import datetime

# Paths
SOURCE_REPO = r"C:\kali-shared\Web-Security-Academy-Series"
TARGET_REPO = r"C:\kali-shared\Web-Security-Series-With-Chandru"
README_PATH = os.path.join(TARGET_REPO, "README.md")

def run_git_command(command, cwd):
    print(f"Running: {' '.join(command)}")
    result = subprocess.run(command, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error executing command: {result.stderr}")
    return result

def main():
    if not os.path.exists(README_PATH):
        print("README.md not found!")
        return

    # Read README
    with open(README_PATH, 'r') as f:
        content = f.read()

    # Find the first uncompleted vulnerability
    match = re.search(r'- \[ \] ([\w-]+)', content)
    if not match:
        print("No more pending vulnerabilities found in README. All done!")
        return

    vuln_name = match.group(1)
    print(f"Next vulnerability to push: {vuln_name}")

    source_dir = os.path.join(SOURCE_REPO, vuln_name)
    target_dir = os.path.join(TARGET_REPO, vuln_name)

    if not os.path.exists(source_dir):
        print(f"Source directory {source_dir} does not exist!")
        return

    # Copy directory
    if os.path.exists(target_dir):
        shutil.rmtree(target_dir)
    shutil.copytree(source_dir, target_dir)
    print(f"Copied {vuln_name} to target repository.")

    # Update README
    updated_content = content.replace(f'- [ ] {vuln_name}', f'- [x] {vuln_name}', 1)
    with open(README_PATH, 'w') as f:
        f.write(updated_content)
    print("Updated README tracker.")

    # Calculate current day based on number of completed items
    day_count = len(re.findall(r'- \[x\]', updated_content))
    commit_msg = f"Day {day_count}: Add {vuln_name} module"

    # Git commands
    run_git_command(["git", "add", "."], TARGET_REPO)
    run_git_command(["git", "commit", "-m", commit_msg], TARGET_REPO)
    
    # Check if there's a remote origin before pushing
    remote_check = run_git_command(["git", "remote"], TARGET_REPO)
    if "origin" in remote_check.stdout:
        push_res = run_git_command(["git", "push", "-u", "origin", "main"], TARGET_REPO)
        print(push_res.stdout)
    else:
        print("No remote 'origin' configured yet. Skipping push.")

if __name__ == "__main__":
    main()
