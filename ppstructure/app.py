import os
import tempfile
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from table.predict_table import TableSystem, parse_args
import cv2

app = FastAPI()

# Initialize TableSystem with default arguments
args = parse_args()
args.det_model_dir = 'inference/en_ppocr_mobile_v2.0_table_det_infer'
args.rec_model_dir = 'inference/en_ppocr_mobile_v2.0_table_rec_infer'
args.table_model_dir = 'inference/en_ppocr_mobile_v2.0_table_structure_infer'
args.rec_char_dict_path = '../ppocr/utils/dict/table_dict.txt'
args.table_char_dict_path = '../ppocr/utils/dict/table_structure_dict.txt'
args.det_limit_side_len = 736
args.det_limit_type = 'min'

table_system = TableSystem(args)

@app.get("/readiness")
def readiness():
    return {"status": "ready"}

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.post("/predict_table")
async def predict_table(file: UploadFile = File(...)):
    print("File received:", file.filename)
    # Create a temporary directory to store the input and output files
    with tempfile.TemporaryDirectory() as temp_dir:
        # Save the uploaded file
        file_path = os.path.join(temp_dir, file.filename)
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())
        
        # Read the image
        img = cv2.imread(file_path)
        
        # Process the image
        pred_res, _ = table_system(img)
        
        # Generate HTML and Excel output
        html_output = pred_res["html"]
        
        # Return the Excel file
        return FileResponse(html_output, filename="table_output.html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)