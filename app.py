from src.streamlit_qrcode_scanner import qrcode_scanner
import streamlit as st
import webbrowser
import validators


def main():
    st.write("## QR Code Scanner")

    qr_code = qrcode_scanner(key='qrcode_scanner')

    if qr_code:
        st.write(qr_code)

        # Kiểm tra xem qr_code có phải là URL hợp lệ không
        if validators.url(qr_code):
            # Mở URL trong trình duyệt web mặc định
            webbrowser.open(qr_code)


if __name__ == "__main__":
    main()
