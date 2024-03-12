# brew install zbar
from PIL import Image
from pyzbar.pyzbar import decode

def decode_qr_code(image_path):
    # QRコードをデコード
    data = decode(Image.open(image_path))
    if data:
        return data[0].data.decode('utf-8')
    else:
        return "QRコードをデコードできませんでした。"

if __name__ == "__main__":
    # デコードされたテキストを表示
    decoded_text = decode_qr_code("./qr_code.png")
    print(f"デコードされたテキスト: {decoded_text}")