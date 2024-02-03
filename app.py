from src.streamlit_qrcode_scanner import qrcode_scanner
import streamlit as st
import validators


def nav_to(url):
    # nav_script = """
    #     <meta http-equiv="refresh" content="0; url='%s'">
    # """ % url
    # st.write(nav_script, unsafe_allow_html=True)
    nav_script = f"""
            <script>
                window.location.href = '{url}';
            </script>
        """
    st.markdown(nav_script, unsafe_allow_html=True)


def main():
    st.write("## QR Code Scanner")

    qr_code = qrcode_scanner(key='qrcode_scanner')

    if qr_code:
        st.write(qr_code)

        if validators.url(str(qr_code)):
            nav_to(qr_code)


if __name__ == "__main__":
    main()
