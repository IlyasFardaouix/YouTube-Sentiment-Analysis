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

      // Prepare data for API
      // Keep texts in memory to display later
      const commentsData = comments.map((text, index) => ({
        id: index.toString(),
        text: text,
      }));
      
      const payload = {
        comments: commentsData,
      };

      // API call
      // TODO: Change URL for your Hugging Face deployment
      // For local testing: http://127.0.0.1:8000/predict_batch
      const apiUrl = "https://has1elb-youtube-sentiment-analysis.hf.space/predict_batch";
      // const apiUrl = "http://127.0.0.1:8000/predict_batch";  // For local testing

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

      // Display comment text with sentiment
      const sentimentLabel = getSentimentLabel(pred.sentiment);
      const confidencePct = (pred.confidence * 100).toFixed(1);
      
      // Create content with full text
      const textSpan = document.createElement("span");
      textSpan.className = "comment-text";
      textSpan.textContent = pred.text.length > 100 
        ? pred.text.substring(0, 100) + "..." 
        : pred.text;
      
      const metaSpan = document.createElement("span");
      metaSpan.className = "comment-meta";
      metaSpan.textContent = ` [${sentimentLabel} - ${confidencePct}%]`;
      
      div.appendChild(textSpan);
      div.appendChild(metaSpan);
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
