import requests

def download_drive_image(drive_id: str, output_path: str = "temp_image.jpg"):
    url = f"https://drive.google.com/uc?export=download&id={drive_id}"
    response = requests.get(url)
    if response.status_code == 200:
        with open(output_path, "wb") as f:
            f.write(response.content)
        return output_path
    raise Exception("Error al descargar imagen desde Drive")
