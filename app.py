import streamlit as st

def main():
    st.title("Calculadora")

    num1 = st.number_input("Digite o primeiro número:", format="%.2f")
    operator = st.selectbox("Escolha a operação:", ["+", "-", "*", "/"])
    num2 = st.number_input("Digite o segundo número:", format="%.2f")

    if st.button("Calcular"):
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2 if num2 != 0 else "Erro: Divisão por zero!"
        st.success(f"Resultado: {result}")

if __name__ == "__main__":
    main()
