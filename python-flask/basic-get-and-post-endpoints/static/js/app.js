const randomUserDiv = document.querySelector(".random-user");
const apiUrl = "https://randomuser.me/api";

const fetchRandomUser = async () => {
  try {
    const response = await fetch(apiUrl);
    const data = await response.json();
    const user = data.results[0];
    console.log(user);
    randomUserDiv.innerHTML = `<pre>${JSON.stringify(user, null, 2)}</pre>`;
  } catch (error) {
    console.error(error);
    randomUserDiv.innerHTML = "<p>Error loading User data.</p>";
  }
};

fetchRandomUser();
