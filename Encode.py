# pip install qrcode
import qrcode

def encode_text_to_qr_code(text, image_path='qr_code.png'):
    # QRコード生成
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=4,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(image_path)

    return image_path

if __name__ == "__main__":
    # 使用例
    text = "2024/03/12 15:10:0"
    qr_image_path = encode_text_to_qr_code(text)
    print(f"エンコードされたQRコードはこちら: {qr_image_path}")