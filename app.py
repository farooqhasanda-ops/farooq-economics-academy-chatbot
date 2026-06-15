import gradio as gr

academy_info = {
    "academy_name": "Farooq Economics Academy",
    "founder": "Farooq Hasan",
    "experience": "20+ Years Teaching Experience",
    "subjects": "Economics, Civics, Commerce, Accounts",
    "classes": "Intermediate 1st Year and 2nd Year",
    "timings": "5 PM to 11 PM",
    "contact": "+91 9989221983",
    "email": "frkfarooqhasan@gmail.com",
    "location": "Tolichowki, Hyderabad",
    "fees": "Please contact the academy for the latest fee structure.",
}


def chatbot(message, history):
    """Simple rule-based academy assistant."""
    msg = (message or "").lower().strip()

    if any(word in msg for word in ["subject", "subjects", "teach", "course", "courses"]):
        return f"Subjects Offered: {academy_info['subjects']}"

    if any(word in msg for word in ["contact", "phone", "mobile", "call", "email"]):
        return f"Phone: {academy_info['contact']}\nEmail: {academy_info['email']}"

    if any(word in msg for word in ["location", "address", "where"]):
        return f"Location: {academy_info['location']}"

    if any(word in msg for word in ["experience", "years"]):
        return academy_info["experience"]

    if any(word in msg for word in ["fee", "fees", "cost", "price"]):
        return academy_info["fees"]

    if any(word in msg for word in ["timing", "time", "batch"]):
        return f"Class Timings: {academy_info['timings']}"

    if any(word in msg for word in ["class", "classes", "intermediate", "1st year", "2nd year"]):
        return f"Classes Available: {academy_info['classes']}"

    if any(word in msg for word in ["admission", "admissions", "join", "enroll", "enrol"]):
        return (
            "🎓 Admissions Open\n\n"
            "Please provide:\n"
            "1. Student Name\n"
            "2. Mobile Number\n"
            "3. Class (1st Year / 2nd Year)\n\n"
            f"📞 {academy_info['contact']}"
        )

    if "whatsapp" in msg:
        return f"WhatsApp: {academy_info['contact']}"

    return (
        f"Welcome to {academy_info['academy_name']}\n\n"
        f"Founder: {academy_info['founder']}\n"
        f"Experience: {academy_info['experience']}\n"
        f"Subjects: {academy_info['subjects']}\n"
        f"Classes: {academy_info['classes']}\n"
        f"Timings: {academy_info['timings']}\n"
        f"Contact: {academy_info['contact']}"
    )


demo = gr.ChatInterface(
    fn=chatbot,
    title="Farooq Economics Academy AI Assistant",
    description="Ask about subjects, admissions, fees, timings, location, and contact details.",
    examples=[
        "What subjects do you teach?",
        "How can I contact the academy?",
        "Where is the academy located?",
        "Tell me about admissions",
        "What are the timings?",
    ],
)


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
