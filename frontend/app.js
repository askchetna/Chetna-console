
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
