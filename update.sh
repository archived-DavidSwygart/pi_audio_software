#!/bin/bash
echo "git pull latest microphone code"
cd "$(dirname "$0")"
git pull
echo "mic/update.sh finished "
