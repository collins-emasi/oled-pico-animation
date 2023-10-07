import os
import sys
import subprocess
import ampy

def upload_files_to_pico(folder_path : str, pico_port: str):
    try:
        result = subprocess.run()
        pico = ampy(port=pico_port)
        files = os.listdir(folder_path)

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: $ python upload_to_pico.py <folder_path> <pico_port>")
        sys.exit(1)
    
    folder_path = sys.argv[1]
    pico_port = sys.argv[2]

    if not os.path.isdir(folder_path):
        print("Error: The specified folder does not exist.")
        sys.exit(1)
    
    upload_files_to_pico(folder_path=folder_path, pico_port=pico_port)