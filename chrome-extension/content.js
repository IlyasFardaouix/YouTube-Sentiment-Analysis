chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "getComments") {
    const comments = extractComments();
    sendResponse(comments);
  }
  return true; // Keep channel open for async response if needed
});

function extractComments() {
  const comments = [];
  // YouTube comment selectors (subject to change)
  // #content-text is the standard selector for the comment text div
  const elements = document.querySelectorAll('#content-text');
  
  elements.forEach(el => {
    const text = el.innerText.trim();
    if (text) {
      comments.push(text);
    }
  });
  
  // Limit to 50 comments to avoid payload issues
  return comments.slice(0, 50);
}
