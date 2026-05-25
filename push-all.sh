#!/bin/bash
# Push to all 3 remotes: citfj (origin) + GitHub public + GitHub private
set -e
git push origin main
git push github main
git push github-private main
echo "✓ Pushed to all 3 remotes"
