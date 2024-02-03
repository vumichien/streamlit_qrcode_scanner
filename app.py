from src.streamlit_qrcode_scanner import qrcode_scanner
import streamlit as st
import webbrowser
import validators
from streamlit_javascript import st_javascript


# def nav_to(url):
#     js = f'window.open("{url}", "_blank").then(r => window.parent.location.href);'
#     st_javascript(js)

def nav_to(url):
    nav_script = """
        <meta http-equiv="refresh" content="0; url='%s'">
    """ % (url)
    st.write(nav_script, unsafe_allow_html=True)


def main():
    st.write("## QR Code Scanner")

    qr_code = qrcode_scanner(key='qrcode_scanner')

    if qr_code:
        st.write(qr_code)

        # Kiểm tra xem qr_code có phải là URL hợp lệ không
        if validators.url(qr_code):
            # Tạo một trang HTML tạm thời với JavaScript để chuyển hướng
            js = f"""
                <script>
                    window.location.href = '{qr_code}';
                </script>
                """
            st.markdown(js, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
