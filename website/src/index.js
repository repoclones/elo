// Variable to store user data
let userData = {};

// Function to fetch user data from /api/user_list and store it in userData
async function fetchUserData() {
    try {
        const response = await fetch('/api/user_list');
        userData = await response.json();
    } catch (error) {
        console.error('Error fetching user data:', error);
    }
}
// Function to search for usernames and show results
function searchUsernames(query) {
    const searchResults = [];
    for (const username in userData) {
        if (username.toLowerCase().includes(query.toLowerCase())) {
            searchResults.push({ username, elo: userData[username] });
            if (searchResults.length === 20) {
                break;
            }
        }
    }
    return searchResults;
}

// Function to show search results in a modal
function showSearchResultsModal(results) {
    const searchResultsContainer = document.getElementById('searchResults');
    searchResultsContainer.innerHTML = '';

    results.forEach(result => {
        const resultElement = document.createElement('div');
        resultElement.className = 'search-result';
        resultElement.dataset.username = result.username;
        resultElement.textContent = result.username;
        searchResultsContainer.appendChild(resultElement);
    });

    const searchModal = document.getElementById('searchModal');
    searchModal.style.display = 'flex'; // Show the search modal

    // Close the search modal when clicked outside the modal content
    searchModal.addEventListener('click', event => {
        if (event.target === searchModal) {
            searchModal.style.display = 'none'; // Hide the search modal
            searchBox.style.zIndex = ''; // Reset the z-index of search box
        }
    });
}

// Function to show user card modal
function showUserCardModal(username) {
    fetch(`/api/user/${username}`)
        .then(response => response.json())
        .then(data => {
            const userCard = document.getElementById('userCard');
            userCard.innerHTML = `
                <h2>${username}</h2>
                <p>ELO: ${data.elo}</p>
                <p>Number of messages: ${data.messages.length}</p>
                <div class="message-list">
                    <h3>Messages:</h3>
                    <ul>
                        ${data.messages.map(message => `<li>${message[0]}</li>`).join('')}
                    </ul>
                </div>
            `;

            const userCardModal = document.getElementById('userCardModal');
            userCardModal.classList.remove('hidden');
            userCardModal.classList.add('flex'); // Add the flex class

            // Add event listener to listen for the Escape key
            document.addEventListener('keydown', event => {
                if (event.key === 'Escape') {
                    closeUserCardModal();
                }
            });
        })
        .catch(error => {
            console.error('Error fetching user card data:', error);
        });

    const userCardModal = document.getElementById('userCardModal');
    userCardModal.style.display = 'flex';
    const searchModal = document.getElementById('searchModal');
    searchModal.style.display = 'flex';
    searchBox.style.zIndex = '-1'; // Hide the search modal
}

// Add event listener to select user from search results
document.addEventListener('click', event => {
    if (event.target.classList.contains('search-result')) {
        const username = event.target.dataset.username;
        showUserCardModal(username);
    }
});

// Add event listener to search box
const searchBox = document.getElementById('searchBox');
searchBox.addEventListener('input', () => {
    const query = searchBox.value;
    if (query === '') {
        const searchModal = document.getElementById('searchModal');
        searchModal.style.display = 'none';
        searchBox.style.zIndex = ''; // Reset the z-index of search box
    } else {
        const searchResults = searchUsernames(query);
        showSearchResultsModal(searchResults);
    }
});

// Add event listener to select user from search results
document.addEventListener('click', event => {
    if (event.target.classList.contains('search-result')) {
        const username = event.target.dataset.username;
        showUserCardModal(username);
    }
});

// Close the search modal when clicked outside the modal content
document.addEventListener('click', event => {
    const searchModal = document.getElementById('searchModal');
    if (event.target === searchModal) {
        searchModal.classList.add('hidden');
        searchModal.classList.remove('flex'); // Remove the flex class
        searchBox.style.zIndex = ''; // Reset the z-index of search box
    }
});

// Keyboard navigation for search results
let selectedSearchIndex = -1;
searchBox.addEventListener('keydown', event => {
    const searchResults = document.querySelectorAll('.search-result');
    if (searchResults.length > 0) {
        if (event.key === 'ArrowDown' || event.key === 'ArrowUp') {
            event.preventDefault();
            searchResults[selectedSearchIndex]?.classList.remove('bg-blue-100', 'text-blue-700');
            if (event.key === 'ArrowDown') {
                selectedSearchIndex = (selectedSearchIndex + 1) % searchResults.length;
            } else if (event.key === 'ArrowUp') {
                selectedSearchIndex = (selectedSearchIndex - 1 + searchResults.length) % searchResults.length;
            }
            searchResults[selectedSearchIndex].classList.add('bg-blue-100', 'text-blue-700');
        } else if (event.key === 'Enter') {
            event.preventDefault();
            const username = searchResults[selectedSearchIndex]?.dataset.username;
            if (username) {
                showUserCardModal(username);
            }
        }
    }
});

// Close the user card modal
const closeUserCardButton = document.getElementById('closeUserCard');
closeUserCardButton.addEventListener('click', () => {
    closeUserCardModal();
});

function closeUserCardModal() {
    const userCardModal = document.getElementById('userCardModal');
    userCardModal.style.display = 'none';

    const searchModal = document.getElementById('searchModal');
    searchModal.style.display = 'flex'; // Show the search modal
    searchBox.style.zIndex = 20;
}

// Fetch user data when the page is loaded
fetchUserData();


document.addEventListener('DOMContentLoaded', () => {
    const searchBox = document.getElementById('searchBox');
    const searchButton = document.getElementById('searchButton');
    const topOverall = document.getElementById('topOverall');
    const topLast = document.getElementById('topLast');

    // You can add your search box functionality here

    // Example data for demonstration
    const overallData = {
        "User1": 1000,
        "User5": 1000,
        "User6": 1000,
        "User7": 850,
        "User8": 1000,
        "User9": 720,
        "User0": 850,
        "Usrr3": 720,
        "Usbr2": 850,
        "Us2r3": 720,
    };

    const lastData = {
        "Us7r4": 300,
        "User1": 1000,
        "Us4r1": 1000,
        "Us9r1": 1000,
        "Us6r2": 850,
        "Usar3": 720,
        "Uswr2": 850,
        "Usrr3": 720,
        "Usqr5": 280,
        "Urer6": 250,

    };

    // Function to render leaderboard
    const renderLeaderboard = (container, data) => {
        const leaderboard = document.createElement('div');
        leaderboard.className = 'bg-green-main rounded-lg p-4 shadow-md';

        for (const [username, points] of Object.entries(data)) {
            const entry = document.createElement('div');
            entry.className = 'flex justify-between items-center mb-2';

            const usernameElement = document.createElement('span');
            usernameElement.className = 'font-semibold';
            usernameElement.textContent = username;

            const pointsElement = document.createElement('span');
            pointsElement.textContent = points;

            entry.appendChild(usernameElement);
            entry.appendChild(pointsElement);

            leaderboard.appendChild(entry);
        }

        container.appendChild(leaderboard);
    };

    // Render leaderboards
    renderLeaderboard(topOverall, overallData);
    renderLeaderboard(topLast, lastData);
});

