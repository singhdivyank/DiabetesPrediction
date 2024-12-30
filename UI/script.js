document.getElementById("submit-btn").addEventListener("click", async () => {
    const glucose = parseFloat(document.getElementById("input1").value).toFixed(1);
    const bmi = parseFloat(document.getElementById("input2").value).toFixed(1);
    const insulin = parseFloat(document.getElementById("input3").value).toFixed(1);
    const age = parseInt(document.getElementById("input4").value);
    
    const body = {
        glucose: glucose,
        insulin: insulin,
        bmi: bmi,
        age: age
    };
    
    // TODO: replace with ECS endpoint
    const apiUrl = ``;
    
    try {
      const response = await fetch(apiUrl, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(body)
      });
  
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
  
      const data = await response.json();
  
      const responseDialog = document.getElementById("response-dialog");
      document.getElementById("response-text").innerText = JSON.stringify(data, null, 2);
      responseDialog.showModal();
    } catch (error) {
      alert(`Error: ${error.message}`);
    }
  });
  
  document.getElementById("close-dialog").addEventListener("click", () => {
    document.getElementById("response-dialog").close();
  });
  