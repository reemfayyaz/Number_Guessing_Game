import random
import streamlit as st
from typing import Tuple


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

        .difficulty-badge {
            display: inline-block;
            padding: 0.4rem 0.8rem;
            border-radius: 8px;
            font-weight: 600;
            font-size: 0.9rem;
            margin: 0.5rem 0.25rem;
        }

        .difficulty-easy {
            background-color: rgba(34, 197, 94, 0.2);
            color: #16a34a;
        }

        .difficulty-medium {
            background-color: rgba(251, 146, 60, 0.2);
            color: #ea580c;
        }

        .difficulty-hard {
            background-color: rgba(239, 68, 68, 0.2);
            color: #dc2626;
        }

        div.stButton > button {
            border-radius: 10px;
            font-weight: 600;
        }

        .stats-box {
            padding: 1rem;
            border-radius: 12px;
            background-color: rgba(100, 116, 139, 0.08);
            margin: 0.8rem 0;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# Difficulty settings
# ---------------------------------------------------------
DIFFICULTY_SETTINGS = {
    "Easy": {"min": 1, "max": 10, "emoji": "🟢"},
    "Medium": {"min": 1, "max": 50, "emoji": "🟠"},
    "Hard": {"min": 1, "max": 100, "emoji": "🔴"},
}


def get_difficulty_range(difficulty: str) -> Tuple[int, int]:
    """Get the min and max range for the selected difficulty."""
    return DIFFICULTY_SETTINGS[difficulty]["min"], DIFFICULTY_SETTINGS[difficulty]["max"]


def get_difficulty_emoji(difficulty: str) -> str:
    """Get the emoji for the selected difficulty."""
    return DIFFICULTY_SETTINGS[difficulty]["emoji"]


# ---------------------------------------------------------
# Game state initialization
# ---------------------------------------------------------
def start_new_game(difficulty: str) -> None:
    """Reset all values and generate a new secret number based on difficulty."""
    min_val, max_val = get_difficulty_range(difficulty)
    st.session_state.difficulty = difficulty
    st.session_state.secret_number = random.randint(min_val, max_val)
    st.session_state.attempts = 0
    st.session_state.message = "Enter a number and press **Submit Guess**."
    st.session_state.message_type = "info"
    st.session_state.game_over = False
    st.session_state.guess_history = []
    st.session_state.min_value = min_val
    st.session_state.max_value = max_val


if "secret_number" not in st.session_state:
    start_new_game("Easy")


# ---------------------------------------------------------
# Header
# ---------------------------------------------------------
st.markdown(
    """
    <div class="game-header">
        <h1>🎯 Number Guessing Game</h1>
        <p>Can you guess the secret number?</p>
    </div>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# Difficulty selector
# ---------------------------------------------------------
st.subheader("📊 Select Difficulty Level")

difficulty_col1, difficulty_col2, difficulty_col3 = st.columns(3)

with difficulty_col1:
    if st.button(
        "🟢 Easy\n(1-10)",
        use_container_width=True,
        key="difficulty_easy",
    ):
        start_new_game("Easy")
        st.rerun()

with difficulty_col2:
    if st.button(
        "🟠 Medium\n(1-50)",
        use_container_width=True,
        key="difficulty_medium",
    ):
        start_new_game("Medium")
        st.rerun()

with difficulty_col3:
    if st.button(
        "🔴 Hard\n(1-100)",
        use_container_width=True,
        key="difficulty_hard",
    ):
        start_new_game("Hard")
        st.rerun()

# Display current difficulty
difficulty_emoji = get_difficulty_emoji(st.session_state.difficulty)
st.markdown(
    f"""
    <div style="text-align: center; margin: 1rem 0;">
        <span class="difficulty-badge difficulty-{st.session_state.difficulty.lower()}">
            {difficulty_emoji} Current Level: <strong>{st.session_state.difficulty}</strong>
        </span>
    </div>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# Game information
# ---------------------------------------------------------
metric_1, metric_2, metric_3 = st.columns(3)

with metric_1:
    st.metric("Attempts", st.session_state.attempts)

with metric_2:
    st.metric("Range", f"{st.session_state.min_value} – {st.session_state.max_value}")

with metric_3:
    # Calculate difficulty score (fewer attempts = higher score)
    if st.session_state.game_over and st.session_state.attempts > 0:
        max_attempts = {
            "Easy": 5,
            "Medium": 8,
            "Hard": 10,
        }[st.session_state.difficulty]
        score = max(0, 100 - (st.session_state.attempts - 1) * 10)
        st.metric("Score", f"{score}/100")
    else:
        st.metric("Score", "—")


# ---------------------------------------------------------
# Guess form
# ---------------------------------------------------------
with st.form("guess_form", clear_on_submit=False):
    guess = st.number_input(
        "Your guess",
        min_value=st.session_state.min_value,
        max_value=st.session_state.max_value,
        value=(st.session_state.min_value + st.session_state.max_value) // 2,
        step=1,
        disabled=st.session_state.game_over,
        help=f"Choose a whole number from {st.session_state.min_value} to {st.session_state.max_value}.",
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
# Game statistics (shown when game is over)
# ---------------------------------------------------------
if st.session_state.game_over:
    st.markdown("---")
    st.subheader("📈 Game Statistics")

    stats_col1, stats_col2, stats_col3 = st.columns(3)

    with stats_col1:
        st.metric("Difficulty", st.session_state.difficulty)

    with stats_col2:
        st.metric("Total Guesses", st.session_state.attempts)

    with stats_col3:
        max_attempts = {
            "Easy": 5,
            "Medium": 8,
            "Hard": 10,
        }[st.session_state.difficulty]
        efficiency = f"{(100 - (st.session_state.attempts - 1) * 10)}%"
        st.metric("Efficiency", efficiency)

    # Performance message
    if st.session_state.attempts == 1:
        performance = "🌟 Perfect! Incredible luck!"
    elif st.session_state.attempts <= 3:
        performance = "⭐ Excellent! Great guessing strategy."
    elif st.session_state.attempts <= 5:
        performance = "👍 Good job! Well done."
    else:
        performance = "💪 Keep practicing! You'll get better."

    st.info(performance)


# ---------------------------------------------------------
# New game control
# ---------------------------------------------------------
st.divider()

if st.button("🔄 Start New Game", use_container_width=True):
    start_new_game(st.session_state.difficulty)
    st.rerun()

st.caption("Built with Python and Streamlit.")
