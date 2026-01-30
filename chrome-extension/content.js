// Listen for messages from popup.js
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "getComments") {
    const comments = extractComments();
    sendResponse(comments);
  }
  return true; // Keep channel open for async response
});

/**
 * Extracts comments from YouTube page
 * Uses #content-text selector which contains comment text
 */
function extractComments() {
  const comments = [];
  
  // Selector for YouTube comments
  // Note: YouTube may change its DOM structure, may need to adapt
  const elements = document.querySelectorAll('#content-text');
  
  // Iterate through all found comments
  elements.forEach(el => {
    const text = el.innerText.trim();
    // Only keep non-empty comments
    if (text && text.length > 0) {
      comments.push(text);
    }
  });
  
  // Limit to 50 comments to avoid payloads that are too large
  // TODO: Maybe increase this limit or make it configurable?
  return comments.slice(0, 50);
}
