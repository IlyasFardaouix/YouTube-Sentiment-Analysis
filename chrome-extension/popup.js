document.addEventListener("DOMContentLoaded", function () {
  const analyzeBtn = document.getElementById("analyzeBtn");
  const loading = document.getElementById("loading");
  const results = document.getElementById("results");
  const errorDiv = document.getElementById("error");
  const commentsList = document.getElementById("commentsList");

  analyzeBtn.addEventListener("click", async () => {
    // Reset UI
    results.classList.add("hidden");
    errorDiv.classList.add("hidden");
    loading.classList.remove("hidden");
    analyzeBtn.disabled = true;

    try {
      // Get active tab
      const [tab] = await chrome.tabs.query({
        active: true,
        currentWindow: true,
      });

      if (!tab.url.includes("youtube.com/watch")) {
        throw new Error("Please use this extension on a YouTube video page.");
      }

      // Execute content script to get comments
      const comments = await chrome.tabs.sendMessage(tab.id, {
        action: "getComments",
      });

      if (!comments || comments.length === 0) {
        throw new Error(
          "No comments found. Please scroll down to load comments first."
        );
      }

      // Prepare payload
      const payload = {
        comments: comments.map((text, index) => ({
          id: index.toString(),
          text: text,
        })),
      };

      // Call API
      // Note: In production, replace with your Hugging Face URL
      const apiUrl = "https://has1elb-youtube-sentiment-analysis.hf.space/predict_batch";

      const response = await fetch(apiUrl, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
      });

      if (!response.ok) {
        throw new Error(`API Error: ${response.statusText}`);
      }

      const data = await response.json();
      displayResults(data);

    } catch (err) {
      if (err.message.includes("Could not establish connection")) {
        errorDiv.textContent = "Error: Please refresh the YouTube page and try again.";
      } else {
        errorDiv.textContent = err.message;
      }
      errorDiv.classList.remove('hidden');
    } finally {
      loading.classList.add('hidden');
      analyzeBtn.disabled = false;
    }
  });

  function displayResults(data) {
    // Update stats
    document.getElementById(
      "posPct"
    ).textContent = `${data.stats.positive_pct}%`;
    document.getElementById(
      "neuPct"
    ).textContent = `${data.stats.neutral_pct}%`;
    document.getElementById(
      "negPct"
    ).textContent = `${data.stats.negative_pct}%`;
    document.getElementById("totalCount").textContent = data.stats.total;

    // Update list
    commentsList.innerHTML = "";
    data.predictions.forEach((pred, index) => {
      const div = document.createElement("div");
      const sentimentClass =
        pred.sentiment === 1 ? "pos" : pred.sentiment === -1 ? "neg" : "neu";
      div.className = `comment-item ${sentimentClass}`;

      // Find original text (we could pass it back from API but we have it in payload logic if we kept it)
      // For simplicity, we rely on index matching or just display sentiment
      // Better: API returns text or we map it.
      // Let's assume we want to show text. The API response in schemas.py only has id, sentiment, confidence.
      // We need to map back using ID.
      // But wait, I don't have the text in the response.
      // I should probably modify the API to return text or just map it here if I kept the original list.
      // I'll map it here assuming order is preserved or using ID.

      // Actually, I don't have the original text easily accessible here unless I stored it.
      // Let's just show "Comment #ID: Sentiment" for now or store it.
      // I'll store the comments in a variable.

      div.textContent = `Comment ${pred.id}: ${getSentimentLabel(
        pred.sentiment
      )} (${(pred.confidence * 100).toFixed(1)}%)`;
      commentsList.appendChild(div);
    });

    results.classList.remove("hidden");
  }

  function getSentimentLabel(s) {
    if (s === 1) return "Positive";
    if (s === -1) return "Negative";
    return "Neutral";
  }
});
