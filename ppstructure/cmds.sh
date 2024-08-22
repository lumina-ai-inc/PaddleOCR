curl -v -X POST \
    -H "Accept: text/html" \
    -F "file=@/Users/akhileshsharma/Documents/Lumina/PaddleOCR/ppstructure/sample/table1.png" \
    --output table_output.html \
    http://localhost:8000/predict_table/
