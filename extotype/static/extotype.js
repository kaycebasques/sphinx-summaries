function createSection() {
  if (document.querySelector('#ai')) {
    return;
  }
  const section = document.createElement('section');
  section.id = 'ai';
  const title = document.createElement('h2');
  title.id = 'ai-title';
  title.textContent = 'TODO';
  const content = document.createElement('div');
  content.id = 'ai-content';
  content.textContent = 'Calculating...';
  section.appendChild(title);
  section.appendChild(content);
  const siblingNode = document.querySelector('#search-results');
  const parentNode = siblingNode.parentNode;
  parentNode.insertBefore(section, siblingNode);
}

function getQuery() {
  const params = new URLSearchParams(window.location.search);
  return params.get('q');
}

window.addEventListener('load', () => {
  createSection();
});
