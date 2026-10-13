const labels = {
  qa: {label:'Your question', title:'Answer', placeholder:'For example: What is photosynthesis?', button:'Generate answer'},
  explain: {label:'Topic to explain', title:'Topic explanation', placeholder:'For example: Explain Newton’s laws in simple words...', button:'Explain topic'},
  quiz: {label:'Quiz topic or notes', title:'Practice quiz', placeholder:'Paste your notes or enter a topic for 3 multiple-choice questions...', button:'Create quiz'},
  summarize: {label:'Text to summarize', title:'Summary', placeholder:'Paste your lesson or study notes here...', button:'Summarize notes'},
  learn: {label:'Your learning goal', title:'Recommended learning path', placeholder:'For example: I want to learn Python from beginner level...', button:'Build learning path'}
};
let selectedTask = 'qa';
const form = document.querySelector('#study-form');
const input = document.querySelector('#study-input');
const submitBtn = document.querySelector('#submit-btn');
const resultCard = document.querySelector('#result-card');
const resultContent = document.querySelector('#result-content');
const charCount = document.querySelector('#char-count');

document.querySelectorAll('.task').forEach(button => button.addEventListener('click', () => {
  selectedTask = button.dataset.task;
  document.querySelectorAll('.task').forEach(item => item.classList.toggle('active', item === button));
  const info = labels[selectedTask];
  document.querySelector('#input-label').textContent = info.label;
  input.placeholder = info.placeholder;
  submitBtn.innerHTML = `${info.button} <span>→</span>`;
}));
input.addEventListener('input', () => { charCount.textContent = `${input.value.length} / 20000`; });

function showText(text) {
  resultContent.replaceChildren();
  resultContent.textContent = text;
}
function showQuiz(data) {
  resultContent.replaceChildren();
  (data.questions || []).forEach((q, index) => {
    const card = document.createElement('div'); card.className = 'quiz-question';
    const heading = document.createElement('h3'); heading.textContent = `${index + 1}. ${q.question}`; card.append(heading);
    const feedback = document.createElement('p'); feedback.className = 'quiz-feedback'; feedback.hidden = true;
    (q.options || []).forEach(option => {
      const label = document.createElement('label'); label.className = 'quiz-option';
      const radio = document.createElement('input'); radio.type = 'radio'; radio.name = `question-${index}`;
      radio.addEventListener('change', () => {
        feedback.hidden = false;
        const correct = option === q.answer;
        feedback.className = `quiz-feedback ${correct ? 'correct' : 'incorrect'}`;
        feedback.textContent = `${correct ? 'Correct!' : `Correct answer: ${q.answer}`} ${q.explanation || ''}`;
      });
      label.append(radio, document.createTextNode(option)); card.append(label);
    });
    card.append(feedback); resultContent.append(card);
  });
}
form.addEventListener('submit', async event => {
  event.preventDefault();
  const text = input.value.trim(); if (!text) { input.focus(); return; }
  submitBtn.disabled = true; submitBtn.textContent = 'Working…';
  resultCard.hidden = false; document.querySelector('#result-title').textContent = labels[selectedTask].title;
  showText('EduGenie is preparing your result…');
  try {
    const response = await fetch('/api/task', {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify({task:selectedTask, text})});
    const data = await response.json();
    if (!response.ok) throw new Error(data.detail || 'Something went wrong. Please try again.');
    if (selectedTask === 'quiz') showQuiz(data.result); else showText(typeof data.result === 'string' ? data.result : JSON.stringify(data.result, null, 2));
  } catch (error) { showText(`Could not generate a result. ${error.message}\n\nCheck your internet connection and GEMINI_API_KEY in the .env file.`); }
  finally { submitBtn.disabled = false; submitBtn.innerHTML = `${labels[selectedTask].button} <span>→</span>`; }
});
document.querySelector('#copy-btn').addEventListener('click', async () => {
  try { await navigator.clipboard.writeText(resultContent.innerText); document.querySelector('#copy-btn').textContent = 'Copied!'; setTimeout(() => document.querySelector('#copy-btn').textContent = 'Copy result', 1200); }
  catch { document.querySelector('#copy-btn').textContent = 'Select text to copy'; }
});
