from services.ocr_service import extract_text_from_file

def run_ocr_agent(file_path):
    return extract_text_from_file(file_path)