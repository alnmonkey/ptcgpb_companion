for lang in en zh ja de fr ko es it; do
    uv run pylupdate6 app/*.py app/**/*.py main.py -ts "app/translations/${lang}.ts"
    uv run python auto_translate.py "app/translations/${lang}.ts"
    lrelease "app/translations/${lang}.ts"
  done
