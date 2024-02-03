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
            # Tạo một trang HTML tạm thời với JavaScript để chuyển hướng
            html_string = f"""
                    <html>
                        <head>
                            <meta http-equiv="refresh" content="0; URL='{qr_code}'" />
                        </head>
                        <body>
                            <p>If you are not redirected, please click <a href="{qr_code}">here</a>.</p>
                        </body>
                    </html>
                    """
            st.markdown(html_string, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
