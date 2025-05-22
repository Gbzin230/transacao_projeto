import streamlit as st
import pandas as pd
import os

CSV_PATH = os.path.join(os.path.dirname(__file__), "..", "transacoes.csv")

def main():
    st.title("Dashboard de Transações")

    csv_path = CSV_PATH

    if not os.path.exists(CSV_PATH):
        st.warning("Nenhuma transação encontrada.")
        return

    df = pd.read_csv(CSV_PATH)

    if df.empty:
        st.write("Nenhuma transação encontrada.")
    else:
        st.dataframe(df)
        total = df["valor"].sum()
        st.metric("Total de Transações", f"R$ {total:.2f}")

if __name__ == "__main__":
    main()
