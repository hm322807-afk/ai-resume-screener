# Running on GitHub Codespaces

This project is configured to run on GitHub Codespaces.

## Quick Start

1. Go to your repository: `https://github.com/hm322807-afk/ai-resume-screener`
2. Click the green **Code** button
3. Select **Codespaces** tab
4. Click **Create codespace on main**

The environment will automatically:
- Install Python 3.11
- Install all dependencies from `requirements.txt`
- Forward port 5000

## Running the App

Once the Codespace loads:

```bash
python app.py
```

A notification will appear with a link to open the app in your browser.

## Notes

- The first launch may take 2-3 minutes to download BERT models
- Port 5000 is automatically forwarded and made public
- Changes you make are saved in the Codespace
