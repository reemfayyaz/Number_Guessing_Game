import random
import streamlit as st


# ---------------------------------------------------------
# Page configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="Number Guessing Game",
    page_icon="🎯",
    layout="centered",
    initial_sidebar_state="collapsed",
)


# ---------------------------------------------------------
# Custom styling
# ---------------------------------------------------------
st.markdown(
    """
    <style>
        .block-container {
            max-width: 760px;
            padding-top: 2rem;
            padding-bottom: 2rem;
        }

        .game-header {
            text-align: center;
            padding: 1.5rem 1rem;
            border-radius: 18px;
            background: linear-gradient(135deg, #4f46e5, #7c3aed);
            color: white;
            margin-bottom: 1.5rem;
        }

        .game-header h1 {
            margin: 0;
            font-size: 2.3rem;
        }

        .game-header p {
            margin: 0.5rem 0 0;
            font-size: 1.05rem;
            opacity: 0.95;
        }

        .status-card {
            padding: 1rem;
            border-radius: 14px;
            background-color: rgba(127, 127, 127, 0.08);
            text-align: center;
            margin: 0.8rem 0;
        }

        div.stButton > button {
            border-radius: 10px;
            font-weight: 600;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# Game state
# ---------------------------------------------------------
def start_new_game() -> None:
    """Reset all values and generate a new secret number."""
    st.session_state.secret_number = random.randint(1, 10)
    st.session_state.attempts = 0
    st.session_state.message = "Enter a number and press **Submit Guess**."
    st.session_state.message_type = "info"
    st.session_state.game_over = False
    st.session_state.guess_history = []


if "secret_number" not in st.session_state:
    start_new_game()


# ---------------------------------------------------------
# Header
# ---------------------------------------------------------
st.markdown(
    """
    <div class="game-header">
        <h1>🎯 Number Guessing Game</h1>
        <p>Can you guess the secret number between 1 and 10?</p>
    </div>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# Game information
# ---------------------------------------------------------
metric_1, metric_2 = st.columns(2)

with metric_1:
    st.metric("Attempts", st.session_state.attempts)

with metric_2:
    st.metric("Possible Range", "1 – 10")


# ---------------------------------------------------------
# Guess form
# ---------------------------------------------------------
with st.form("guess_form", clear_on_submit=False):
    guess = st.number_input(
        "Your guess",
        min_value=1,
        max_value=10,
        value=5,
        step=1,
        disabled=st.session_state.game_over,
        help="Choose a whole number from 1 to 10.",
    )

    submitted = st.form_submit_button(
        "Submit Guess",
        use_container_width=True,
        disabled=st.session_state.game_over,
    )


if submitted:
    guess = int(guess)
    st.session_state.attempts += 1
    st.session_state.guess_history.append(guess)

    if guess == st.session_state.secret_number:
        st.session_state.message = (
            f"🎉 Correct! The secret number was **{st.session_state.secret_number}**. "
            f"You guessed it in **{st.session_state.attempts} attempt(s)**."
        )
        st.session_state.message_type = "success"
        st.session_state.game_over = True

    elif guess < st.session_state.secret_number:
        st.session_state.message = "📉 Too low. Try a higher number."
        st.session_state.message_type = "warning"

    else:
        st.session_state.message = "📈 Too high. Try a lower number."
        st.session_state.message_type = "warning"

    st.rerun()


# ---------------------------------------------------------
# Feedback
# ---------------------------------------------------------
if st.session_state.message_type == "success":
    st.success(st.session_state.message)
    st.balloons()
elif st.session_state.message_type == "warning":
    st.warning(st.session_state.message)
else:
    st.info(st.session_state.message)


# ---------------------------------------------------------
# Guess history
# ---------------------------------------------------------
if st.session_state.guess_history:
    history = " → ".join(str(value) for value in st.session_state.guess_history)
    st.markdown(
        f"""
        <div class="status-card">
            <strong>Guess History</strong><br>
            {history}
        </div>
        """,
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------
# New game control
# ---------------------------------------------------------
if st.button("🔄 Start New Game", use_container_width=True):
    start_new_game()
    st.rerun()


st.divider()
st.caption("Built with Python and Streamlit.")
