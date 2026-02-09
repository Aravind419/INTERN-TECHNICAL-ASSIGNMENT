import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  // State to store the facts data from the API
  const [facts, setFacts] = useState([]);

  // State to track loading status
  const [loading, setLoading] = useState(true);

  // State to track any errors
  const [error, setError] = useState(null);

  // API URL - Django backend endpoint
  // Uses environment variable, defaults to production Render URL
  const API_URL = process.env.REACT_APP_API_URL || 'https://intern-technical-assignment.onrender.com/api/facts/';

  // useEffect hook - runs when component mounts
  useEffect(() => {
    // Function to fetch facts from Django API
    const fetchFacts = async () => {
      try {
        setLoading(true);

        // Make GET request to Django API
        const response = await fetch(API_URL);

        // Check if response is successful
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        // Parse JSON response
        const data = await response.json();

        // Set facts from the response data
        setFacts(data.data);
        setLoading(false);

        console.log('✅ Facts fetched successfully:', data);

      } catch (err) {
        console.error('❌ Error fetching facts:', err);
        setError(err.message);
        setLoading(false);
      }
    };

    // Call the fetch function
    fetchFacts();
  }, [API_URL]); // Run when component mounts or API_URL changes

  // Show loading message while fetching
  if (loading) {
    return (
      <div className="App">
        <div className="loading">
          <div className="spinner"></div>
          <p>Loading facts...</p>
        </div>
      </div>
    );
  }

  // Show error message if something went wrong
  if (error) {
    return (
      <div className="App">
        <div className="error">
          <h2>⚠️ Error</h2>
          <p>{error}</p>
          <p className="help-text">
            Make sure the Django backend is running at {API_URL}
          </p>
        </div>
      </div>
    );
  }

  // Main render - display the facts
  return (
    <div className="App">
      <header className="App-header">
        <h1>🎯 Interesting Facts</h1>
        <p className="subtitle">Powered by Django REST Framework + React</p>
      </header>

      <main className="facts-container">
        {facts.length === 0 ? (
          <p className="no-data">No facts available</p>
        ) : (
          <div className="facts-grid">
            {facts.map((fact) => (
              <div key={fact.id} className="fact-card">
                <div className="fact-header">
                  <span className="fact-id">#{fact.id}</span>
                  <span className="fact-category">{fact.category}</span>
                </div>
                <p className="fact-text">{fact.fact}</p>
              </div>
            ))}
          </div>
        )}
      </main>

      <footer className="App-footer">
        <p>
          Total Facts: <strong>{facts.length}</strong>
        </p>
      </footer>
    </div>
  );
}

export default App;
