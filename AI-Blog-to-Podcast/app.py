import streamlit as st

from src.article.extractor import extract_article
from src.agent.podcast_agent import generate_podcast_script
from src.podcast.podcast_generator import generate_podcast_audio


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="PodCraft AI",
    page_icon="🎙️",
    layout="wide"
)


# ============================================================
# DARK UI
# ============================================================

st.markdown(
    """
    <style>

    /* ---------- MAIN BACKGROUND ---------- */

    .stApp {
        background-color: #08090d;
        color: #f5f5f5;
    }

    [data-testid="stAppViewContainer"] {
        background:
            radial-gradient(
                circle at 50% -10%,
                rgba(99, 102, 241, 0.14),
                transparent 35%
            ),
            #08090d;
    }

    .main .block-container {
        max-width: 1050px;
        padding-top: 2.5rem;
        padding-bottom: 4rem;
    }


    /* ---------- HIDE DEFAULT STREAMLIT UI ---------- */

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        background: transparent !important;
    }


    /* ---------- TEXT ---------- */

    h1 {
        color: #ffffff !important;
        font-weight: 800 !important;
        letter-spacing: -1.5px;
    }

    h2 {
        color: #ffffff !important;
        font-weight: 700 !important;
    }

    h3 {
        color: #e5e7eb !important;
    }

    p {
        color: #9ca3af;
    }


    /* ---------- INPUT ---------- */

    [data-testid="stTextInput"] label {
        color: #cbd5e1 !important;
        font-weight: 600 !important;
    }

    [data-testid="stTextInput"] input {
        background-color: #111318 !important;
        color: #ffffff !important;

        border: 1px solid #292d38 !important;
        border-radius: 12px !important;

        height: 48px !important;

        padding-left: 16px !important;

        transition: all 0.2s ease;
    }

    [data-testid="stTextInput"] input:focus {
        border-color: #6366f1 !important;

        box-shadow:
            0 0 0 2px rgba(99, 102, 241, 0.15) !important;
    }

    [data-testid="stTextInput"] input::placeholder {
        color: #555b68 !important;
    }


    /* ---------- PRIMARY BUTTON ---------- */

    .stButton > button {

        background: linear-gradient(
            135deg,
            #6366f1,
            #7c3aed
        ) !important;

        color: white !important;

        border: none !important;

        border-radius: 12px !important;

        height: 48px !important;

        font-weight: 700 !important;

        transition: all 0.2s ease;
    }

    .stButton > button:hover {

        transform: translateY(-1px);

        box-shadow:
            0 10px 30px rgba(99, 102, 241, 0.25);
    }


    /* ---------- TEXT AREA ---------- */

    [data-testid="stTextArea"] textarea {

        background-color: #0f1116 !important;

        color: #dbe1ea !important;

        border: 1px solid #292d38 !important;

        border-radius: 14px !important;

        line-height: 1.7 !important;

        font-size: 0.92rem !important;
    }


    /* ---------- AUDIO ---------- */

    [data-testid="stAudio"] {

        background-color: #111318 !important;

        border: 1px solid #292d38 !important;

        border-radius: 14px !important;

        padding: 8px !important;
    }


    /* ---------- DOWNLOAD BUTTON ---------- */

    .stDownloadButton > button {

        background-color: #111318 !important;

        color: #e5e7eb !important;

        border: 1px solid #292d38 !important;

        border-radius: 10px !important;

        font-weight: 600 !important;

        width: 100%;
    }

    .stDownloadButton > button:hover {

        background-color: #181b22 !important;

        border-color: #454a58 !important;
    }


    /* ---------- ALERTS ---------- */

    [data-testid="stAlert"] {

        background-color: #111318 !important;

        border-radius: 12px !important;
    }


    /* ---------- DIVIDERS ---------- */

    hr {
        border-color: #1f232c !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    "# 🎙️ PodCraft AI"
)

st.caption(
    "Transform any article into an AI-generated podcast conversation."
)

st.write("")


# ============================================================
# INPUT SECTION
# ============================================================

st.subheader("Create a podcast")

url = st.text_input(
    "Article URL",
    placeholder="Paste a blog or article URL here..."
)

generate = st.button(
    "✦  Generate Podcast",
    use_container_width=True
)


# ============================================================
# GENERATION
# ============================================================

if generate:

    if not url.strip():

        st.warning(
            "Please enter an article URL."
        )

    else:

        try:

            # ------------------------------------------------
            # ARTICLE EXTRACTION
            # ------------------------------------------------

            with st.spinner(
                "Reading the article..."
            ):

                article = extract_article(url)


            if not article["text"].strip():

                st.error(
                    "Could not extract meaningful content from this page."
                )

                st.stop()


            # ------------------------------------------------
            # ARTICLE INFORMATION
            # ------------------------------------------------

            st.divider()

            st.subheader(
                "📄 Source Article"
            )

            st.write(
                f"**{article['title']}**"
            )

            if article["authors"]:

                st.caption(
                    f"By {', '.join(article['authors'])}"
                )


            # ------------------------------------------------
            # GENERATE SCRIPT
            # ------------------------------------------------

            with st.spinner(
                "Writing the podcast conversation..."
            ):

                podcast_script = generate_podcast_script(
                    article["text"]
                )


            # ------------------------------------------------
            # SHOW SCRIPT
            # ------------------------------------------------

            st.divider()

            st.subheader(
                "💬 Podcast Conversation"
            )

            st.text_area(
                "Generated Script",
                podcast_script,
                height=450,
                label_visibility="collapsed"
            )


            # ------------------------------------------------
            # GENERATE AUDIO
            # ------------------------------------------------

            with st.spinner(
                "Generating podcast audio..."
            ):

                audio_path = generate_podcast_audio(
                    podcast_script
                )


            audio_bytes = audio_path.read_bytes()


            # ------------------------------------------------
            # AUDIO PLAYER
            # ------------------------------------------------

            st.divider()

            st.subheader(
                "🎧 Your Podcast"
            )

            st.audio(
                audio_bytes,
                format="audio/wav"
            )


            # ------------------------------------------------
            # DOWNLOAD
            # ------------------------------------------------

            st.download_button(
                label="↓  Download Podcast",
                data=audio_bytes,
                file_name="podcast.wav",
                mime="audio/wav",
                use_container_width=True
            )

            st.success(
                "Your podcast is ready!"
            )


        except Exception as e:

            st.error(
                f"Something went wrong: {e}"
            )