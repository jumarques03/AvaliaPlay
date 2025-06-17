// URL base da sua API FastAPI
const API_BASE_URL = 'http://127.0.0.1:8000/docs';

// Função para mostrar mensagens
function showMessage(message, type = 'success') {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${type}`;
    messageDiv.textContent = message;
    
    const container = document.querySelector('.container');
    container.insertBefore(messageDiv, container.firstChild);
    
    setTimeout(() => {
        messageDiv.remove();
    }, 5000);
}

// Função para adicionar jogo
document.getElementById('addGameForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const gameData = {
        nome: document.getElementById('gameName').value,
        categoria: document.getElementById('gameCategory').value,
        descricao: document.getElementById('gameDescription').value
    };

    try {
        const response = await fetch(`${API_BASE_URL}/adicionar/jogo`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(gameData)
        });

        const result = await response.json();
        
        if (response.ok) {
            showMessage(result.mensagem, 'success');
            document.getElementById('addGameForm').reset();
        } else {
            showMessage(result.mensagem || 'Erro ao adicionar jogo', 'error');
        }
    } catch (error) {
        showMessage('Erro de conexão. Verifique se sua API está rodando em http://localhost:8000', 'error');
        console.error('Erro:', error);
    }
});

// Função para adicionar avaliação
document.getElementById('addReviewForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const reviewData = {
        nome_jogo: document.getElementById('reviewGameName').value,
        nota: parseInt(document.getElementById('reviewRating').value),
        comentario: document.getElementById('reviewComment').value
    };

    try {
        const response = await fetch(`${API_BASE_URL}/adicionar/avaliacao`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(reviewData)
        });

        const result = await response.json();
        
        if (response.ok) {
            showMessage('Avaliação adicionada com sucesso!', 'success');
            document.getElementById('addReviewForm').reset();
        } else {
            showMessage(result.mensagem || 'Erro ao adicionar avaliação', 'error');
        }
    } catch (error) {
        showMessage('Erro de conexão. Verifique se sua API está rodando em http://localhost:8000', 'error');
        console.error('Erro:', error);
    }
});

// Função para carregar jogos
async function loadGames() {
    const loading = document.getElementById('loading');
    const container = document.getElementById('gamesContainer');
    
    loading.classList.add('show');
    container.innerHTML = '';

    try {
        const response = await fetch(`${API_BASE_URL}/jogos`);
        const result = await response.json();
        
        loading.classList.remove('show');
        
        if (result.mensagem) {
            container.innerHTML = `<p style="text-align: center; color: #c084fc; font-size: 1.2rem;">${result.mensagem}</p>`;
            return;
        }

        if (result.jogos) {
            result.jogos.forEach(item => {
                const gameCard = createGameCard(item);
                container.appendChild(gameCard);
            });
        }
    } catch (error) {
        loading.classList.remove('show');
        showMessage('Erro de conexão. Verifique se sua API está rodando em http://localhost:8000', 'error');
        console.error('Erro:', error);
    }
}

// Função para criar card do jogo
function createGameCard(item) {
    const card = document.createElement('div');
    card.className = 'game-card';
    
    const stars = generateStars(item.media_avaliacoes);
    const reviewsHtml = item.avaliacoes.map(review => `
        <div class="review">
            <div class="review-rating">${generateStars(review.nota)} ${review.nota}/10</div>
            <div class="review-comment">${review.comentario}</div>
        </div>
    `).join('');

    card.innerHTML = `
        <div class="game-name">${item.jogo.nome}</div>
        <div class="game-category">${item.jogo.categoria}</div>
        <div class="game-description">${item.jogo.descricao}</div>
        <div class="rating">
            <span class="rating-stars">${stars}</span>
            <span class="rating-value">
                ${item.media_avaliacoes ? `${item.media_avaliacoes.toFixed(1)}/10` : 'Sem avaliações'}
            </span>
        </div>
        ${item.avaliacoes.length > 0 ? `
            <div class="reviews">
                <strong style="color: #ddd6fe;">Avaliações:</strong>
                ${reviewsHtml}
            </div>
        ` : ''}
    `;
    
    return card;
}

// Função para gerar estrelas
function generateStars(rating) {
    if (!rating) return '☆☆☆☆☆';
    
    const fullStars = Math.floor(rating / 2);
    const halfStar = rating % 2 >= 1;
    const emptyStars = 5 - fullStars - (halfStar ? 1 : 0);
    
    return '★'.repeat(fullStars) + (halfStar ? '☆' : '') + '☆'.repeat(emptyStars);
}

// Carregar jogos quando a página carrega
window.addEventListener('load', () => {
    loadGames();
});