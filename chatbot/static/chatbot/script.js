function sendMessage() {
  const userMessage = document.getElementById("user-input").value;
  if (userMessage.trim() === "") return;

  const chatMessages = document.querySelector(".chat-messages");
  const message = document.createElement("div");
  message.classList.add("message", "user-message");
  message.textContent = userMessage;

  chatMessages.appendChild(message);
  document.getElementById("user-input").value = "";

  // Make an AJAX request to the Django view
  fetch(
    "/chatbot/get_openai_response/?user_message=" +
      encodeURIComponent(userMessage)
  )
    .then((response) => response.json())
    .then((data) => {
      const botMessage = document.createElement("div");
      botMessage.classList.add("message");
      botMessage.textContent = data.response;
      chatMessages.appendChild(botMessage);
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}
