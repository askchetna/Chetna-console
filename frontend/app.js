
document.addEventListener('DOMContentLoaded', function() {
    const modeSelect = document.getElementById('mode');
    const inputTextarea = document.getElementById('input');
    const generateBtn = document.getElementById('generateBtn');
    const outputArea = document.getElementById('outputArea');
    const output = document.getElementById('output');
    const loading = document.getElementById('loading');

    // Sample inputs for each mode
    const sampleInputs = {
        proposal: "Need a web development project for a local restaurant. They want online ordering, customer management, and delivery tracking. Budget is $15,000 and timeline is 3 months.",
        business: "SaaS platform for small businesses to manage their social media content across multiple platforms. Target market is local businesses with 1-50 employees. Subscription-based revenue model.",
        support: "Getting a Python ImportError: No module named 'flask' when trying to run my web application. The error occurs on line 3 of app.py where I import Flask."
    };

    // Update placeholder text when mode changes
    modeSelect.addEventListener('change', function() {
        const mode = modeSelect.value;
        inputTextarea.placeholder = `Example: ${sampleInputs[mode]}`;
        
        // Auto-fill with sample if textarea is empty
        if (!inputTextarea.value.trim()) {
            inputTextarea.value = sampleInputs[mode];
        }
    });

    // Initialize with default sample
    inputTextarea.placeholder = `Example: ${sampleInputs.proposal}`;
    inputTextarea.value = sampleInputs.proposal;

    generateBtn.addEventListener('click', async function() {
        const mode = modeSelect.value;
        const inputText = inputTextarea.value.trim();

        if (!inputText) {
            alert('Please enter some input text.');
            return;
        }

        // Show loading, hide output
        loading.classList.remove('hidden');
        outputArea.classList.add('hidden');
        generateBtn.disabled = true;
        generateBtn.textContent = 'Generating...';

        try {
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    mode: mode,
                    input: inputText
                })
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();

            // Hide loading, show output
            loading.classList.add('hidden');
            outputArea.classList.remove('hidden');
            output.textContent = data.reply;
            
            // Add fade-in animation
            outputArea.classList.add('fade-in');

            // Scroll to output
            outputArea.scrollIntoView({ behavior: 'smooth' });

        } catch (error) {
            loading.classList.add('hidden');
            alert(`Error: ${error.message}`);
            console.error('Error:', error);
        } finally {
            generateBtn.disabled = false;
            generateBtn.textContent = 'Generate Response';
        }
    });

    // Allow Enter+Shift to submit
    inputTextarea.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' && e.shiftKey) {
            e.preventDefault();
            generateBtn.click();
        }
    });
});
// Frontend JavaScript for ChetnaGPT Web Interface
const generateBtn = document.getElementById('generateBtn');
const loadingDiv = document.getElementById('loading');
const outputArea = document.getElementById('outputArea');
const outputDiv = document.getElementById('output');
const modeSelect = document.getElementById('mode');
const userInput = document.getElementById('userInput');

generateBtn.addEventListener('click', async () => {
    const mode = modeSelect.value;
    const input = userInput.value.trim();
    
    if (!input) {
        alert('Please enter your input before generating a response.');
        return;
    }
    
    // Show loading state
    generateBtn.disabled = true;
    loadingDiv.classList.remove('hidden');
    outputArea.classList.add('hidden');
    
    try {
        const response = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                mode: mode,
                input: input
            })
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        
        // Display the response
        outputDiv.textContent = data.reply;
        outputArea.classList.remove('hidden');
        
    } catch (error) {
        console.error('Error:', error);
        outputDiv.textContent = `Error: ${error.message}. Please try again.`;
        outputArea.classList.remove('hidden');
    } finally {
        // Hide loading state
        loadingDiv.classList.add('hidden');
        generateBtn.disabled = false;
    }
});

// Add quick example functionality
document.addEventListener('click', (e) => {
    if (e.target.closest('.bg-white.p-3')) {
        const exampleDiv = e.target.closest('.bg-white.p-3');
        const exampleText = exampleDiv.querySelector('p').textContent;
        const title = exampleDiv.querySelector('h4').textContent;
        
        // Set the mode based on the example
        if (title.includes('Proposal')) {
            modeSelect.value = 'proposal';
        } else if (title.includes('Business')) {
            modeSelect.value = 'business';
        } else if (title.includes('Tech')) {
            modeSelect.value = 'support';
        }
        
        // Set the input text
        userInput.value = exampleText;
        
        // Scroll to top
        window.scrollTo({ top: 0, behavior: 'smooth' });
    }
});

// Health check on page load
fetch('/health')
    .then(response => response.json())
    .then(data => {
        if (data.ok) {
            console.log('✅ ChetnaGPT API is healthy');
        }
    })
    .catch(error => {
        console.error('❌ API health check failed:', error);
    });
