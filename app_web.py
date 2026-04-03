import streamlit as st
from PIL import Image
import random

st.set_page_config(layout="wide")

if "pontos" not in st.session_state:
    st.session_state.pontos = 0
    st.session_state.xp = 0
    st.session_state.nivel = 1
    st.session_state.casa = []
    st.session_state.player_pos = [0, 0]
    st.session_state.pet_pos = [1, 0]

missoes = [
    "Beber água 💧",
    "Estudar 📚",
    "Modo foco 🎯",
    "Organizar a casa 🏡"
]

if "missoes" not in st.session_state:
    st.session_state.missoes = random.sample(missoes, 3)

st.title("🎮 Rotina Gamer WEB")

col1, col2 = st.columns([2,1])

with col1:
    st.subheader("🏡 Sua Casa")

    grid_size = 5
    for y in range(grid_size):
        cols = st.columns(grid_size)
        for x in range(grid_size):

            cell = "⬜"

            if [x,y] == st.session_state.player_pos:
                cell = "🧍"
            elif [x,y] == st.session_state.pet_pos:
                cell = "🐱"

            for obj in st.session_state.casa:
                if obj == [x,y]:
                    cell = "🛋️"

            if cols[x].button(cell, key=f"{x}-{y}"):
                st.session_state.casa.append([x,y])

    st.write("### 🎮 Controles")

    colA, colB, colC = st.columns(3)

    if colA.button("⬅️"):
        st.session_state.player_pos[0] -= 1

    if colB.button("⬆️"):
        st.session_state.player_pos[1] -= 1

    if colC.button("➡️"):
        st.session_state.player_pos[0] += 1

    if st.button("⬇️"):
        st.session_state.player_pos[1] += 1

    px, py = st.session_state.player_pos
    petx, pety = st.session_state.pet_pos

    st.session_state.pet_pos = [
        petx + (px - petx)//2,
        pety + (py - pety)//2
    ]

with col2:
    st.subheader("🎯 Missões")

    for i, m in enumerate(st.session_state.missoes):
        if st.button(f"✔ {m}", key=i):
            st.session_state.pontos += 10
            st.session_state.xp += 20
            st.session_state.missoes.pop(i)
            st.rerun()

    st.write("---")

    st.subheader("📊 Progresso")

    st.write(f"⭐ Pontos: {st.session_state.pontos}")
    st.write(f"🧬 XP: {st.session_state.xp}")
    st.write(f"🏆 Nível: {st.session_state.nivel}")

    if st.session_state.xp >= 100:
        st.session_state.xp = 0
        st.session_state.nivel += 1
        st.success("LEVEL UP!")

st.write("---")
if st.button("🔄 Resetar jogo"):
    st.session_state.clear()
    st.rerun()
