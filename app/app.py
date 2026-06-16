import streamlit as st
import pickle
import plotly.graph_objects as go
import time

# --------------------------
# Page Configuration
# --------------------------

st.set_page_config(
    page_title="ScamRadar",
    page_icon="🛡️",
    layout="centered"
)

# --------------------------
# Load Model
# --------------------------

with open("models/spam_classifier.pkl", "rb") as file:
    model = pickle.load(file)

with open("models/vectorizer.pkl", "rb") as file:
    vectorizer = pickle.load(file)

# --------------------------
# Gauge Function
# --------------------------

def create_gauge(score):

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            number={"suffix": "%"},
            title={"text": "Threat Score"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {
                    "color": "#1e293b",
                    "thickness": 0.25
                },
                "steps": [
                    {"range": [0, 30], "color": "#6BCB77"},
                    {"range": [30, 70], "color": "#FFD93D"},
                    {"range": [70, 100], "color": "#FF6B6B"}
                ],
                "threshold": {
                    "line": {
                        "color": "black",
                        "width": 6
                    },
                    "thickness": 0.8,
                    "value": score
                }
            }
        )
    )

    fig.update_layout(
        height=350,
        margin=dict(l=20, r=20, t=50, b=20)
    )

    return fig

# --------------------------
# Sidebar
# --------------------------

with st.sidebar:

    st.title("🛡️ ")

    st.divider()

    st.metric(
        "Model Accuracy",
        "98.03%"
    )

    st.divider()

    st.subheader("Technology")

    st.write("Python")
    st.write("Scikit-Learn")
    st.write("Naive Bayes")
    st.write("Streamlit")
    st.write("Plotly")

    st.divider()

    st.subheader("Future Roadmap")

    st.write("🔜 Hinglish Detection")
    st.write("🔜 Scam Categories")
    st.write("🔜 URL Detection")
    st.write("🔜 Threat Intelligence")

# --------------------------
# Main UI
# --------------------------

st.title("🛡️ ScamRadar")

st.caption(
    "Cyber Threat Analysis Dashboard"
)

st.divider()

message = st.text_area(
    "Analyze Message",
    height=180,
    placeholder="Paste a suspicious message here..."
)

# --------------------------
# Prediction
# --------------------------

if st.button(
    "🔍 Analyze Threat",
    use_container_width=True
):

    if message.strip() == "":
        st.warning(
            "Please enter a message."
        )

    else:

        features = vectorizer.transform(
            [message]
        )

        prediction = model.predict(
            features
        )[0]

        confidence = (
            model.predict_proba(features)
            .max()
            * 100
        )
        with st.spinner(" Analyzing message patterns..."):
            time.sleep(1)

        # ----------------------
        # Risk Score
        # ----------------------

        if prediction == "spam":

            risk_score = confidence

            if risk_score >= 90:
                risk_level = "CRITICAL"

            elif risk_score >= 70:
                risk_level = "HIGH"

            else:
                risk_level = "MEDIUM"

        else:

            risk_score = 100 - confidence

            if risk_score <= 20:
                risk_level = "LOW"

            else:
                risk_level = "MEDIUM"

        st.divider()

        # ----------------------
        # Threat Status
        # ----------------------

        if prediction == "spam":

            st.error(
                f"🚨 Threat Level: {risk_level}"
            )

        else:

            st.success(
                f"✅ Threat Level: {risk_level}"
            )

        # ----------------------
        # Gauge Meter
        # ----------------------

        gauge = create_gauge(
            risk_score
        )

        st.subheader("Threat Scan")

        status = st.empty()
        gauge_placeholder = st.empty()

        status.info("🔍 Initializing threat analysis...")

        for progress in [10, 25, 45, 70, 90]:

            gauge_placeholder.plotly_chart(
                create_gauge(progress),
                use_container_width=True
            )

            time.sleep(0.15)

        status.info("🧠 Running AI threat assessment...")

        time.sleep(0.4)

        gauge_placeholder.plotly_chart(
            create_gauge(risk_score),
            use_container_width=True
        )

        status.empty()

        # ----------------------
        # Metrics
        # ----------------------

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Risk Score",
                f"{risk_score:.1f}%"
            )

        with col2:

            st.metric(
                "Classification",
                prediction.upper()
            )

        # ----------------------
        # Recommendations
        # ----------------------

        st.subheader(
            "Security Recommendations"
        )

        if prediction == "spam":

            st.warning(
                """
⚠️ Do not click suspicious links

⚠️ Do not share OTPs

⚠️ Do not share banking information

⚠️ Verify sender identity

⚠️ Report suspicious activity
                """
            )

        else:

            st.info(
                """
✅ Message appears legitimate

✅ No major scam indicators found

✅ Continue normal communication

✅ Stay cautious with links
                """
            )

# --------------------------
# Footer
# --------------------------

st.divider()

st.caption(
    " Naive Bayes • 98.03% Accuracy"
)




