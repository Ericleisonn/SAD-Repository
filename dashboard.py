import pandas as pd
import matplotlib.pyplot as plt

# ==============================
# Dados simulados da Big Hangus
# ==============================
dados = {
    "Mês": ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho"],
    "Vendas (R$)": [35000, 32000, 38000, 40000, 42000, 39500],
    "Pedidos": [1400, 1250, 1520, 1600, 1680, 1580],
    "Ticket Médio (R$)": [25, 25.6, 25, 25, 25, 25]
}
df = pd.DataFrame(dados)

produtos = {
    "X-Burger": 32,
    "X-Bacon": 25,
    "X-Salada": 18,
    "Combo Família": 15,
    "Outros": 10
}

canais = {
    "Delivery iFood": 60,
    "Presencial": 35,
    "WhatsApp": 5
}

avaliacao_media = 4.5

# ==============================
# Geração dos gráficos
# ==============================
# 1. Faturamento
plt.figure()
plt.plot(df["Mês"], df["Vendas (R$)"], marker="o", linewidth=2)
plt.title("Faturamento Mensal")
plt.ylabel("R$ em Vendas")
plt.savefig("faturamento.png")

# 2. Pedidos
plt.figure()
plt.bar(df["Mês"], df["Pedidos"], color="orange")
plt.title("Pedidos Mensais")
plt.ylabel("Quantidade de Pedidos")
plt.savefig("pedidos.png")

# 3. Produtos
plt.figure()
plt.pie(produtos.values(), labels=produtos.keys(), autopct="%1.1f%%", startangle=90)
plt.title("Produtos Mais Vendidos")
plt.savefig("produtos.png")

# 4. Canais
plt.figure()
plt.pie(canais.values(), labels=canais.keys(), autopct="%1.1f%%", startangle=90)
plt.title("Canais de Venda")
plt.savefig("canais.png")

# ==============================
# Criação do Markdown
# ==============================
with open("dashboard.md", "w", encoding="utf-8") as f:
    f.write("# 🍔 Dashboard Big Hangus Hamburgueria\n\n")
    f.write("## 📊 Indicadores Gerais\n")
    f.write(f"- **Faturamento (Junho):** R$ {df['Vendas (R$)'].iloc[-1]:,.2f}\n")
    f.write(f"- **Pedidos (Junho):** {df['Pedidos'].iloc[-1]}\n")
    f.write(f"- **Avaliação Média:** ⭐ {avaliacao_media}/5\n\n")

    f.write("## 📈 Faturamento Mensal\n")
    f.write("![](faturamento.png)\n\n")

    f.write("## 📦 Pedidos por Mês\n")
    f.write("![](pedidos.png)\n\n")

    f.write("## 🍟 Produtos Mais Vendidos\n")
    f.write("![](produtos.png)\n\n")

    f.write("## 📲 Canais de Venda\n")
    f.write("![](canais.png)\n\n")

    f.write("> 💡 Insight: O Delivery iFood representa **60% das vendas**, sugerindo foco em promoções nesse canal.\n")
