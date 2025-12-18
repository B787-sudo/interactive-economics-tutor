import { useState } from "react";
import "./App.css";

function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const askTeacher = async () => {
    if (!question.trim()) return;

    try {
      setLoading(true);

     const res = await fetch(
  `${import.meta.env.VITE_API_URL}/ask`,
  {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question }),
  }
);


      const data = await res.json();
      setAnswer(data.teacher);

      // 🔊 Text-to-Speech
      if (data.teacher) {
        window.speechSynthesis.cancel();
        const speech = new SpeechSynthesisUtterance(data.teacher);
        speech.lang = "en-US";
        window.speechSynthesis.speak(speech);
      }
    } catch (error) {
      setAnswer("Sorry, something went wrong. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      <div className="content">

        {/* HEADER */}
        <header>
          <h1>📘 Interactive Economics Tutor</h1>
          <p>Learn economics through AI explanations, PDF content & videos</p>
        </header>

        {/* ASK TEACHER */}
        <div className="card">
          <h2>👩‍🏫 Ask the Teacher</h2>

          <div className="ask-row">
            <input
              type="text"
              placeholder="Type your economics question..."
              value={question}
              onChange={(e) => setQuestion(e.target.value)}
            />

            <button onClick={askTeacher} disabled={loading}>
              {loading ? "Thinking..." : "Ask"}
            </button>
          </div>

          {answer && (
            <div className="answer">
              <strong>Teacher:</strong> {answer}
            </div>
          )}
        </div>

        {/* VIDEO LEARNING */}
        <div className="card">
          <h2>🎥 Video Learning</h2>

          <div className="video-grid">
            <div className="video-card">
              <iframe
                src="https://www.youtube.com/embed/Ec19ljjvlCI"
                title="Economics Video 1"
                allowFullScreen
              />
              <p>Core concepts of economics explained simply.</p>
            </div>

            <div className="video-card">
              <iframe
                src="https://www.youtube.com/embed/Z_S0VA4jKes"
                title="Economics Video 2"
                allowFullScreen
              />
              <p>Quick revision for exams and understanding basics.</p>
            </div>
          </div>
        </div>

      </div>
    </div>
  );
}

export default App;
