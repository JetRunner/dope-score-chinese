for file in "$1"/*; do
  echo $file
  python dope_score.py "$file"
done
