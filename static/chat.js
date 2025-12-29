async function sendMessage() {
  const input = document.getElementById("message");
  const text = input.value.trim();
  if (!text) return;

  addMessage("You", text);
  input.value = "";

  try {
    const res = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        user_id: getUserId(),
        message: text
      })
    });

    const data = await res.json();
    addMessage("Bot", data.reply || "No response");

  } catch (err) {
    addMessage("Bot", "Connection error. Try again.");
  }
}

function addMessage(sender, text) {
  const chat = document.getElementById("chat");
  const div = document.createElement("div");
  div.textContent = `${sender}: ${text}`;
  chat.appendChild(div);
  chat.scrollTop = chat.scrollHeight;
}

function getUserId() {
  if (!localStorage.user_id) {
    localStorage.user_id = "user_" + Date.now();
  }
  return localStorage.user_id;
}
