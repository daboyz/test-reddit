# reddit-cli
Reddit command-line client

# Installation
```pip install git+https://github.com/daboyz/test-reddit.git```

# Usage:

Search subreddits by name
```bash
reddit-cli search <search_query>
```

Show subreddit submissions
```bash
reddit-cli subreddit <subreddit_name> --limit=20 --order=hot
```

Show submission comments
```bash
reddit-cli submission <subreddit_id>
```
