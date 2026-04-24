import os

# Path to the attached folder
base_path = "/home/tino/Desktop/work/Bespoke/bespoke-harbor-task/jobs/2026-04-02__16-18-03"

for subfolder in os.listdir(base_path):
    subfolder_path = os.path.join(base_path, subfolder)
    if not os.path.isdir(subfolder_path):
        continue
    agent_path = os.path.join(subfolder_path, "agent")
    if not os.path.isdir(agent_path):
        continue
    for episode in os.listdir(agent_path):
        episode_path = os.path.join(agent_path, episode)
        if not os.path.isdir(episode_path):
            continue
        prompt_file = os.path.join(episode_path, "prompt.txt")
        response_file = os.path.join(episode_path, "response.txt")
        if os.path.isfile(prompt_file) and os.path.isfile(response_file):
            print(f"=== {subfolder}/agent/{episode} ===")
            print("--- prompt.txt ---")
            with open(prompt_file, "r", encoding="utf-8") as f:
                print(f.read())
            print("--- response.txt ---")
            with open(response_file, "r", encoding="utf-8") as f:
                print(f.read())
            print()