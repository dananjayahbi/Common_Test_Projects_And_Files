var generateSummaryBtn = document.getElementById("generate-summary");
var textInput = document.getElementById("text-input");
var summaryEl = document.getElementById("summary");

generateSummaryBtn.addEventListener("click", function() {
  var text = textInput.value;
  var summary = getSummary(text);
  summaryEl.innerHTML = summary;
});

function getSummary(text) {
  var sentences = text.split(/[.!?]/);
  var importantSentences = [];
  for (var i = 0; i < sentences.length; i++) {
    if (sentences[i].length > 5) {
      importantSentences.push(sentences[i]);
    }
  }
  var summary = importantSentences.join(". ");
  return summary;
}
