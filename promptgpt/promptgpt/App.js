import React, { useState } from 'react';
import axios from 'axios';

const App = () => {
  const [userPrompt, setUserPrompt] = useState('');
  const [optimizedPrompt, setOptimizedPrompt] = useState('');

  const handleInputChange = (event) => {
    setUserPrompt(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('/generate', { user_prompt: userPrompt });
      setOptimizedPrompt(response.data.optimized_prompt);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="App">
      <form onSubmit={handleSubmit}>
        <label>
          User Prompt:
          <input type="text" value={userPrompt} onChange={handleInputChange} />
        </label>
        <input type="submit" value="Generate" />
      </form>
      {optimizedPrompt && <div>Optimized Prompt: {optimizedPrompt}</div>}
    </div>
  );
}

export default App;
