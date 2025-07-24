#!/bin/bash
set -e

prompt=""
view_results=0

# Parse args
while [[ $# -gt 0 ]]; do
  key="$1"
  case $key in
    --prompt)
      prompt="$2"
      shift 2
      ;;
    --view_results)
      view_results=1
      shift
      ;;
    *)
      echo "Unknown option: $1"
      exit 1
      ;;
  esac
done

if [[ -z "$prompt" ]]; then
  echo "Error: --prompt argument is required."
  exit 1
fi

if command -v python &>/dev/null; then
  PYTHON=python
elif command -v python3 &>/dev/null; then
  PYTHON=python3
else
  echo "Error: Python is not installed." >&2
  exit 1
fi

# Run generation scripts
$PYTHON texture_gen.py "$prompt"
$PYTHON normalmap_gen.py
$PYTHON displacement_gen.py

if [[ $view_results -eq 1 ]]; then
  echo "Launching Flask app..."
  $PYTHON app.py &

  FLASK_PID=$!

  sleep 3

  if command -v xdg-open &>/dev/null; then
    xdg-open http://127.0.0.1:5000
  elif command -v open &>/dev/null; then
    open http://127.0.0.1:5000
  else
    echo "Please open your browser and go to http://127.0.0.1:5000"
  fi

  wait $FLASK_PID
fi
