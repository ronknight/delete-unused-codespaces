<p><a target="_blank" href="https://app.eraser.io/workspace/Go1xRQnNKDSqMrahbLIv" id="edit-in-eraser-github-link"><img alt="Edit in Eraser" src="https://firebasestorage.googleapis.com/v0/b/second-petal-295822.appspot.com/o/images%2Fgithub%2FOpen%20in%20Eraser.svg?alt=media&amp;token=968381c8-a7e7-472a-8ed6-4a6626da5501"></a></p>

<h1 align="center"><a href="https://github.com/ronknight/delete-unused-codespaces">Delete Unused Codespaces</a></h1>

<h4 align="center">This Python script automates the process of deleting unused GitHub Codespaces, helping to free up resources and manage your development environment efficiently.
</h4>

<p align="center">
<a href="https://twitter.com/PinoyITSolution"><img src="https://img.shields.io/twitter/follow/PinoyITSolution?style=social"></a>
<a href="https://github.com/ronknight?tab=followers"><img src="https://img.shields.io/github/followers/ronknight?style=social"></a>
<a href="https://github.com/ronknight/ronknight/stargazers"><img src="https://img.shields.io/github/stars/BEPb/BEPb.svg?logo=github"></a>
<a href="https://github.com/ronknight/ronknight/network/members"><img src="https://img.shields.io/github/forks/BEPb/BEPb.svg?color=blue&logo=github"></a>
<a href="https://youtube.com/@PinoyITSolution"><img src="https://img.shields.io/youtube/channel/subscribers/UCeoETAlg3skyMcQPqr97omg"></a>
<a href="https://github.com/ronknight/delete-unused-codespaces/issues"><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"></a>
<a href="https://github.com/ronknight/delete-unused-codespaces/blob/master/LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
<a href="#"><img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg"></a>
<a href="https://github.com/ronknight"><img src="https://img.shields.io/badge/Made%20with%20%F0%9F%A4%8D%20by%20-%20Ronknight%20-%20red"></a>
</p>

<p align="center">
  <a href="#requirements">Requirements</a> •
  <a href="#usage">Usage</a> •
  <a href="#script">Script</a> •
  <a href="#disclaimer">Disclaimer</a> •
  <a href="#diagrams">Diagrams</a>
</p>

---

## 📋 Requirements

To run this script, you need:

- Python 3.x
- GitHub Personal Access Token with appropriate permissions
- The following Python packages (install using `pip install -r requirements.txt`):
    - requests
    - python-dotenv

### 🔑 Creating a GitHub Personal Access Token

1. Go to [GitHub Settings > Developer Settings > Personal access tokens](https://github.com/settings/tokens) 
2. Click on "Generate new token" (classic)
3. Give your token a descriptive name
4. Set the expiration as needed
5. Select the following scopes:
    - `codespace`: Full control of codespaces
    - `repo`: Full control of private repositories (needed to check branch status)
6. Click "Generate token"
7. Copy the generated token (you won't be able to see it again)

Make sure to keep your token secure and never share it publicly.

## 🚀 Usage

1. Clone the repository:
```
git clone https://github.com/ronknight/delete-unused-codespaces.git
cd delete-unused-codespaces
```

2. Install the required dependencies:
```
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your GitHub credentials:
```
GITHUB_ACCESS_TOKEN=your_access_token_here
GITHUB_USERNAME=your_github_username
```

4. Run the script:
```
python delete-unused-codespaces.py
```

## 📜 Script

The main script `delete-unused-codespaces.py` performs the following actions:

1. Fetches all codespaces for the authenticated user
2. Checks each codespace for pending changes
3. Deletes codespaces without pending changes
4. Saves deletion status and codespace information to JSON files

Key functions:

- `get_codespaces()`: Fetches all codespaces
- `get_branch_status()`: Checks for pending changes in a repository
- `delete_codespace()`: Deletes a specific codespace
- `save_deletion_status_to_json()`: Saves deletion status to a JSON file

## ⚠️ Disclaimer

**IMPORTANT: This script will delete all unused codespaces without prompting for confirmation.**

- Use this script with extreme caution.
- Ensure you have backups of any important work stored in your codespaces.
- The script considers a codespace "unused" if it doesn't have pending changes. This may not always align with your definition of "unused".
- Once a codespace is deleted, its contents cannot be recovered.
- The author is not responsible for any data loss, unintended deletions, or any other negative consequences resulting from the use of this script.
- By using this script, you acknowledge that you understand the risks and accept full responsibility for any outcomes.

It is strongly recommended to review the list of codespaces manually before running this script, especially if you're using it for the first time.

USE AT YOUR OWN RISK.

## 📊 Diagrams

<!-- eraser-additional-files -->
<a href="/README-Delete Unused Codespaces Flowchart-1.eraserdiagram" data-element-id="6LVNr7YL9oukPfmuPK5L-"><img src="/.eraser/Go1xRQnNKDSqMrahbLIv___3Jivg2tjMecMlrHwbIVIBR8f7U03___---diagram----08e9d1b75af79254bff1bd14cc512517-Delete-Unused-Codespaces-Flowchart.png" alt="" data-element-id="6LVNr7YL9oukPfmuPK5L-" /></a>
<!-- end-eraser-additional-files -->

---

Made with ❤️ by [Ronknight](https://github.com/ronknight)
