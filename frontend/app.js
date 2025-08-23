
document.addEventListener('DOMContentLoaded', function() {
    const modeSelect = document.getElementById('mode');
    const inputTextarea = document.getElementById('input');
    const generateBtn = document.getElementById('generateBtn');
    const outputArea = document.getElementById('outputArea');
    const output = document.getElementById('output');
    const loading = document.getElementById('loading');

    // Check if all elements exist
    if (!generateBtn || !outputArea || !output || !loading) {
        console.error('Some required DOM elements are missing');
        return;
    }

    // Sample inputs for each mode
    const sampleInputs = {
        proposal: "Restaurant: online ordering + CRM + delivery, $15k, 3 months",
        business: "AI fitness app, millennials, subscription ₹299/month",
        support: "npm ERR! module not found: react-dom"
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

        // Log the request
        console.log("POST /chat", { mode, input: inputText.slice(0, 120) + "..." });

        // Show loading, hide output
        loading.classList.remove('hidden');
        outputArea.classList.add('hidden');
        generateBtn.disabled = true;
        generateBtn.innerHTML = 'Generating...';

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

            // Render the response with HTML escaping and line breaks
            const safe = (data.reply || "")
                .replace(/&/g, "&amp;")
                .replace(/</g, "&lt;")
                .replace(/\n/g, "<br>");
            output.innerHTML = safe;

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
            generateBtn.innerHTML = 'Generate Response';
        }
    });

    // Allow Enter+Shift to submit
    inputTextarea.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' && e.shiftKey) {
            e.preventDefault();
            generateBtn.click();
        }
    });

    // Add click functionality to test examples
    document.addEventListener('click', (e) => {
        if (e.target.closest('.bg-white.p-3.rounded.border')) {
            const exampleDiv = e.target.closest('.bg-white.p-3.rounded.border');
            const exampleText = exampleDiv.querySelector('p').textContent.replace(/"/g, '');
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
            inputTextarea.value = exampleText;

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
});
