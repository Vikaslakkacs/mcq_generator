import os
import PyPDF2
import json
import traceback

def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf_reader= PyPDF2.PdffileReader(file)
            text=""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text

        except Exception as e:
            raise Exception("Error reading Pdf file")
    
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
        
    else:
        raise Exception(
            "un-supported file format only pdf and text file supported"
        )

def get_table_data(quiz_str):
    try:
        ## Convert quiz from str to dict
        quiz_dict= json.loads(quiz_str)
        quiz_table_data= []

        # iterate over quiz dictionary and extract the required information
        for key, value in quiz_dict.items():
            mcq= value["mcq"]
            options= " || ".join(
                [
                    f"{option} -> {option_value}" for option, option_value in value['"options'].item()
                ]
            )

            correct= value['correct']
            quiz_table_data.append({"MCQ": mcq, "Choices": options, "Correct": correct})
        return quiz_table_data
    
    except Exception as e:
        tracebck.print_exception(type(e), e, e.__traceback__)
        return False