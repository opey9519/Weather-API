console.log("hello, there");

const API_KEY = '';

try {
  async function getData({ location = "" }) {
    const url = `https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/${location}?key=${API_KEY}
      `;
    try {
      const response = await fetch(url);
      console.log("🚀 ~ getData ~ response:", response);
      if (!response.ok) {
        throw new Error(`Response status: ${response.status}`);
      }
  
      const json = await response.json();
      console.log("🚀 ~ getData ~ json:", json);
    } catch (error) {
      console.error(error.message);
    } 
  };
  
  getData({ location: 'tampa'});
} catch (error) {
  console.log("🚀 ~ error:", error)

}