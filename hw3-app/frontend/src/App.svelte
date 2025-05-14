<script lang="ts">
  import { onMount } from "svelte";
  import Column from "./components/Column.svelte";
  import CommentSection from "./components/CommentSection.svelte";

  let apiKey = "";
  let url = "";
  let articles: any[] = [];

  onMount(async () => {
    try {
      const res = await fetch("/api/key");
      const data = await res.json();
      apiKey = data.apiKey;
      url = `https://api.nytimes.com/svc/search/v2/articlesearch.json?q=(Sacramento,Davis)%sort=newest&api-key=${apiKey}`;
    } catch (error) {
      console.error("Failed to fetch API key:", error);
    }

    fetch(url)
      .then((response) => response.json())
      .then((data) => {
        // console.log(data);
        console.log(data.response.docs);
        articles = data.response.docs;
      })
      .catch((error) => {
        console.error("Error fetching data >~<: ", error);
      });
  });

  const months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
  ];
  const days = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
  ];

  const currDate = new Date();
  // getMonth() returns an integer 0-11.
  // Using the output of getMonth() to index
  // an array of month names allows us to get
  // corresponding month name.
  let currMonth = months[currDate.getMonth()];
  // Same logic described above applies here.
  let currDay = days[currDate.getDay()];
</script>

<main>
  <header>
    <section class="header-section">
      <!--
      Webpage Title
      -->
      <h1>The New York Times</h1>
      <!--
      Dynamic Current Date Display
      -->
      <p id="curr-date">
        {currDay +
          ", " +
          currMonth +
          " " +
          currDate.getDate() +
          ", " +
          currDate.getFullYear()}
      </p>
    </section>
  </header>

  <main>
    <section class="articles-section">
      <Column articles={articles.slice(0, 2)} />
      <Column articles={articles.slice(2, 4)} />
      <Column articles={articles.slice(4, 6)} />
    </section>
    <CommentSection />
  </main>
</main>
