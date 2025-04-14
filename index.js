
document.getElementById("weatherform").addEventListener("submit", async function(e) {
  e.preventDefault() // Prevent form from submitting
  const city = document.getElementById("city").value;

  try {
    const res = await fetch(`http://127.0.0.1:5000/weather/${city}`)
    const data = await res.json()
    const resultDiv = document.getElementById("result");
    console.log(data)
    if (data.temp) {
      resultDiv.textContent = `The temperature in ${city} is ${data.temp}`
    }
    else {
      resultDiv.textContent = `Error: ${data.error}`
    }
  }
  catch (err) {
    console.log(`Error: ${err}`)
    document.getElementById("result").textContent = "Something went wrong"
  }
})