"""
figure_pdf_to_png_converter.py

Iveta Lolova
21.11.2024
"""

from pdf2image import convert_from_path
import os


def create_directory(directory_path):
    """
    Creates given directory_path, if it does not already exists.
    """
    if not os.path.exists(directory_path):
        try:
            os.makedirs(directory_path)
            print(f"Directory '{directory_path}' created successfully.")
        except OSError as e:
            print(f"Error: {e}")
    else:
        print(f"Directory '{directory_path}' already exists.")


def convert_one_pdf_to_png(file_name, source_pdf_directory, target_png_directory):
    pdf_path = source_pdf_directory + "\\" + file_name +".pdf"
    images = convert_from_path(pdf_path)
    for index, image in enumerate(images):
        png_path= target_png_directory + "\\" + file_name +".png"
        image.save(png_path)


def convert_directory_of_pdfs_to_destination_directories_of_pngs(parent_directory_of_pdfs_directory):
    """
    Converts all pdf files images to png files images.
    Then .png files are stored in new parent_directory_of_pdfs_directory/PNG
    """
    pdfs_directory = parent_directory_of_pdfs_directory + "/PDF"

    pngs_directory = parent_directory_of_pdfs_directory + "/PNG"
    create_directory(pngs_directory)

    files = os.listdir(pdfs_directory)
    for count, file in enumerate(files):
        file_name_without_extension = file.strip(".pdf")
        convert_one_pdf_to_png(file_name=file_name_without_extension,
                               source_pdf_directory=pdfs_directory,
                               target_png_directory=pngs_directory)
        print(count, "/", len(files))


# Ensure this block runs only when the script is executed directly
if __name__ == "__main__":

    directory = r"C:\Users\lolova\Repository\TO_LSSynRM3Material_Triangle\Individual_Results_13082024\Results_from_script\Selection_Synchronized\paretofront"  # replace with the path to your directory
    convert_directory_of_pdfs_to_destination_directories_of_pngs(directory)

    print("End of main script!")



