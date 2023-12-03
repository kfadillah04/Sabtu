import streamlit as st

#ini bagian heading aplikasi streamlit
st.title("Kuliah Praktikum Big Data")
st.write("Dillah")
st.write("# Heading 1")

# Kinerja Unit
st.metric("Kinerja", 40, -1)
st.metric("response Time", 30, 20)

# Pilihan
pilih1 = st.checkbox('Ya')
pilih2 = st.checkbox('Tidak')

st.write(pilih1)
st.write(pilih2)


"""
Ini komentar harusnya
"""

makanan = st.radio('Makanan kesukaan', ['Bakso', 'Nasi goreng', 'Mie ayam'] )

st.write(makanan)

minuman = st.selectbox('Pilih minuman yang akan dipesan', 
                       ['es teh', 'kopi', 'jus'] )

st.write(minuman)

bayar = st.multiselect('Bayar pakai:',
                       ['Tunai', 'Ovo', 'Gopay'])
st.write(bayar)

