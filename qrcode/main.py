import streamlit as st
import qrcode
import pyqrcode 
from PIL import Image
#import pyzbar
from pyzbar.pyzbar import decode



st.sidebar.write("使い方")
add_selectbox = st.sidebar.selectbox(
    "この下のバーでQRコードの読み取り方法・作成方法の使い方説明を切り替えることができます",
    ("QRコード読み取り方法", "QRコード作成方法")
)


if add_selectbox == "QRコード読み取り方法":
    image1 = Image.open('説明QRコード読み込み１.png')
    image2 = Image.open('説明QRコード読み込み2.png')
    image3 = Image.open('説明QRコード読み込み3.png')
    st.sidebar.image(image1)
    st.sidebar.write("①　「QRコード読み込み」と表示されているか確認")
    st.sidebar.write("②　②の位置に読み込みたいQRコードの画像をドラック＆ドロップする")
    st.sidebar.image(image2)
    st.sidebar.write("ドラック＆ドロップが成功すると「Drag and drop file here」の下に画像の名前が表示されます")
    st.sidebar.write("③　「読み込み」ボタンを数回押す")
    st.sidebar.image(image3)
    st.sidebar.write("「読み込み」ボタンを押すと上の画像のように読み込んだ画像とその下にQRコードを読み取った結果が表示されます")

elif add_selectbox == "QRコード作成方法":
    image4 = Image.open("説明QRコード作成1.png")
    image5 = Image.open("説明QRコード作成2.png")
    st.sidebar.image(image4)
    st.sidebar.write("①　「QRコード作成」と表示されているか確認")
    st.sidebar.write("②　②のところにQRコードにしたいURLを入力します")
    st.sidebar.write("③　画像として保存するので、その名前を入力します")
    st.sidebar.write("④　④で画像の拡張子を設定することができます")
    st.sidebar.write("選べる拡張子は「png」「jpeg」です")
    st.sidebar.write("⑤　「作成」ボタンを数回押します")
    st.sidebar.image(image5)
    st.sidebar.write("「作成」ボタンを押すと上の画像のように作成したQRコードが表示されます")
    st.sidebar.write("その下の「Download QRコード」ボタンから作成したQRコードをダウンロードすることできます")


st.title("QRコード読み取り・作成サイト")
#QRコードの読み込みと作成を切り替えるウィジェット
qr_option = st.selectbox(
     'QRコード読み込み・作成切り替え',
     ('QRコード読み込み', 'QRコード作成'))

#QRコードの読み込み
if qr_option == 'QRコード読み込み':

    st.title('QRコード読み込み')
    uploaded_file = st.file_uploader("読み取りたいQRコードをドロップ＆ドロップしてください")
    if st.button('読み込み'):
        st.write('読み込み完了')
        image = Image.open(uploaded_file)
        st.image(image,caption = '読み込んだQRコード')
        d = decode(Image.open(uploaded_file))
        #st.info("読み込み結果:")
        #st.write(d[0].data.decode("utf-8"))
        z = d[0].data.decode("utf-8")
        st.info("読み込み結果 : {}".format(z))
       
elif qr_option == 'QRコード作成': 
    st.title('QRコード作成')
    qr = st.text_input('QRコードにしたいURLを入力してください')
    name = st.text_input('保存する画像の名前を入力してください')

    option = st.selectbox(
        '作成するQRコードの拡張子を選択してください',
        ('png', 'jpeg'))

    st.write('選択している拡張子:', option)

    if st.button('作成'):
        st.write('作成完了')
        img = qrcode.make('{}'.format(qr))
        img.save('{}.{}'.format(name,option))
        image = Image.open('{}.{}'.format(name,option))
        st.image(image,caption = '作成したQRコード')

        with open('{}.{}'.format(name,option), "rb") as file:
            btn = st.download_button(
                    label="Download QRコード",
                    data=file,
                    file_name='{}.{}'.format(name,option),
                    mime="image/"+str('{}.{}'.format(name,option))
                )
