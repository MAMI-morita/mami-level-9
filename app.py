import streamlit as st

st.title("🛡️ エラー処理アプリ")

st.write("数字を入れてわり算するよ！")

kazu1 = st.number_input("わられる数", value=10)
kazu2 = st.number_input("わる数", value=2)

if st.button("計算する"):
    try:
        kotae = kazu1 / kazu2
        st.success(f"こたえ: {kotae}")
    except ZeroDivisionError:
        st.error("0ではわれないよ！")
    except Exception as e:
        st.error(f"エラーが出たよ: {e}")
