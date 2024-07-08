import os
import json
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

ACCESS_TOKEN = os.getenv('GITHUB_ACCESS_TOKEN')
USERNAME = os.getenv('GITHUB_USERNAME')
HEADERS = {'Authorization': f'token {ACCESS_TOKEN}'}
BASE_URL = 'https://api.github.com'

def get_codespaces():
    url = f'{BASE_URL}/user/codespaces'
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        raise Exception(f'Error fetching codespaces: {response.json()}')
    return response.json()

def get_branch_status(owner, repo):
    url = f'{BASE_URL}/repos/{owner}/{repo}/branches/main'  # Adjust branch if necessary
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        raise Exception(f'Error fetching branch status for {repo}: {response.json()}')
    branch_data = response.json()
    return branch_data['commit']['sha'] if branch_data.get('commit') else None

def delete_codespace(codespace_name):
    url = f'{BASE_URL}/user/codespaces/{codespace_name}'
    response = requests.delete(url, headers=HEADERS)
    if response.status_code == 204:
        return {'status': 'success', 'message': f'Deleted codespace: {codespace_name}'}
    else:
        return {'status': 'error', 'message': f'Failed to delete codespace: {codespace_name}', 'response': response.json()}

def save_deletion_status_to_json(deletion_status):
    with open('deletion_status.json', 'a') as f:
        json.dump(deletion_status, f, indent=4)
        f.write('\n')  # Add newline for each status entry

def main():
    try:
        codespaces = get_codespaces()
        print(f'Fetched codespaces: {codespaces}')
        
        # Save fetched codespaces to a prettified JSON file
        save_deletion_status_to_json(codespaces)
        print('Codespaces data has been saved to codespaces.json')

        for codespace in codespaces.get('codespaces', []):
            codespace_name = codespace['name']
            print(f'Checking codespace: {codespace_name}')
            
            # Extract owner and repo name from codespace name if possible
            try:
                owner, repo = codespace_name.split('/')
            except ValueError:
                print(f'Skipping codespace {codespace_name}: It has unsaved changes.')
                continue
            
            # Check branch status to determine pending changes
            try:
                branch_sha = get_branch_status(owner, repo)
                if branch_sha:
                    print(f'Codespace {codespace_name} has pending changes, skipping deletion...')
                else:
                    print(f'Deleting codespace: {codespace_name}')
                    deletion_status = delete_codespace(codespace_name)
                    save_deletion_status_to_json(deletion_status)
            except Exception as branch_error:
                print(f'Error checking branch status for {codespace_name}: {branch_error}')
        
        print('All relevant codespaces have been processed.')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    main()
